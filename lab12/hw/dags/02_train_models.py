import pickle
import pendulum
import numpy as np
import polars as pl

from airflow.sdk import dag, task, ObjectStoragePath
from airflow.providers.postgres.hooks.postgres import PostgresHook

from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

from sklearn.svm import SVR
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import RandomForestRegressor


@dag()
def train_models():
    @task
    def train(
        model_name: str,
        data_base: ObjectStoragePath,
        models_base: ObjectStoragePath,
        target: str,
        logical_date: pendulum.DateTime,
    ) -> dict:

        # --- Fetch datasets from S3 and combine
        dfs = []
        for path in data_base.iterdir():
            with path.open("rb") as file:
                dfs.append(pl.read_parquet(file))
        df: pl.DataFrame = pl.concat(dfs).sort("Date")

        # --- Feature engineering
        df = df.with_columns(
            [
                pl.col("Date").dt.weekday().alias("day_of_week"),
                pl.col("Date").dt.day().alias("day_of_month"),
                pl.col(target).shift(1).alias(f"{target}_lag_1"),
                pl.col(target).shift(7).alias(f"{target}_lag_7"),
                pl.col(target).log1p(),
            ]
        ).drop_nulls()

        # --- Split into train and test
        last_month = df["Date"].max().strftime("%Y-%m")  # type:ignore
        train_df = df.filter(pl.col("Date").dt.to_string("%Y-%m") != last_month)
        test_df = df.filter(pl.col("Date").dt.to_string("%Y-%m") == last_month)

        y_train = train_df[target].to_pandas()
        X_train = train_df.drop(["Date", target]).to_pandas()

        y_test = test_df[target].to_pandas()
        X_test = test_df.drop(["Date", target]).to_pandas()

        # --- Train model
        match model_name:
            case "svr":
                model = make_pipeline(StandardScaler(), SVR())
            case "ridge":
                model = make_pipeline(StandardScaler(), RidgeCV())
            case "rf":
                rf = RandomForestRegressor(random_state=0)
                model = GridSearchCV(rf, param_grid={"n_estimators": [50, 100], "max_depth": [None, 10]})
            case _:
                raise ValueError(f"Unknown model name: {model_name}")

        model.fit(X_train, y_train)

        # --- Evaluate on test dataset
        y_test = np.expm1(y_test)
        y_pred = np.expm1(model.predict(X_test))
        metrics = {
            "test_mae": mean_absolute_error(y_test, y_pred),
            "test_mape": mean_absolute_percentage_error(y_test, y_pred),
        }

        # --- Save model temporarily
        model_path = models_base / f"{model_name}_{logical_date.isoformat()}.pkl"
        with model_path.open("wb") as file:
            pickle.dump(model, file, protocol=pickle.HIGHEST_PROTOCOL)  # type:ignore

        return {
            "model_name": model_name,
            "train_size": len(train_df),
            "train_date": logical_date.isoformat(),
            **metrics,
        }

    @task
    def select_best_model(results: list[dict], models_base: ObjectStoragePath) -> None:
        best = min(results, key=lambda r: r["test_mae"])
        best = best["model_name"] + "_" + best["train_date"]

        for path in models_base.iterdir():
            if not path.name.startswith(best):
                path.unlink()

    @task
    def save_metrics(results: list[dict]) -> None:
        fields = list(results[0].keys())
        rows = [tuple(r[field] for field in fields) for r in results]
        pg_hook = PostgresHook(postgres_conn_id="postgres_storage")
        pg_hook.insert_rows(table="training_results", rows=rows, target_fields=fields)

    DATA_S3 = ObjectStoragePath("s3://aws_default@taxi-data/")
    MODELS_S3 = ObjectStoragePath("s3://aws_default@ml-models/")

    results = train.partial(
        data_base=DATA_S3,
        models_base=MODELS_S3,
        target="Taxi Rides Count",
    ).expand(model_name=["svr", "ridge", "rf"])

    select_best_model(results, MODELS_S3)  # type:ignore
    save_metrics(results)  # type:ignore


train_models()
