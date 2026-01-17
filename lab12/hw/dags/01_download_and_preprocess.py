import pendulum
import polars as pl

from airflow.sdk import dag, task, ObjectStoragePath


@dag(
    schedule="@monthly",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    end_date=pendulum.datetime(2025, 12, 31, tz="UTC"),
    catchup=True,
    max_active_runs=4,
)
def download_and_preprocess():
    @task
    def get_yellow_taxi_data(*, data_base, logical_date: pendulum.DateTime) -> None:

        url = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
        date = logical_date.format("YYYY-MM")
        fname = f"yellow_tripdata_{date}.parquet"

        df = pl.scan_parquet(source=url + fname)
        df = (
            df.with_columns(pl.col("tpep_pickup_datetime").dt.date().alias("Date"))
            .group_by("Date")
            .len()
            .rename({"len": "Taxi Rides Count"})
            .sort("Date")
            .filter(pl.col("Date").dt.to_string("%Y-%m") == date)
            .collect()
        )

        print("---> Fetched data:\n", df.head())

        path = data_base / fname
        with path.open("wb") as file:
            df.write_parquet(file)

    DATA_S3 = ObjectStoragePath("s3://aws_default@taxi-data/")
    get_yellow_taxi_data(data_base=DATA_S3)  # type: ignore


download_and_preprocess()
