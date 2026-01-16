import requests
import datetime
import pendulum
import pandas as pd

from airflow.sdk import dag, task


@dag(
    schedule=datetime.timedelta(days=7),
    catchup=True,
    start_date=pendulum.datetime(2025, 1, 1, tz="America/New_York"),
    end_date=pendulum.datetime(2025, 2, 1, tz="America/New_York"),
    max_active_runs=1,
)
def weather_data_backfilling():
    @task
    def get_data(**context) -> dict:
        logical_date: pendulum.DateTime = context["logical_date"]
        start_date = logical_date
        end_date = logical_date.add(days=6)
        print(f"Fetching data from {start_date} to {end_date}")

        url = (
            "https://archive-api.open-meteo.com/v1/archive?"
            "latitude=40.7143&longitude=-74.006"
            f"&start_date={start_date.to_date_string()}"
            f"&end_date={end_date.to_date_string()}"
            "&hourly=temperature_2m"
            "&timezone=auto"
        )

        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()

        return {"time": data["hourly"]["time"], "temperature": data["hourly"]["temperature_2m"]}

    @task
    def transform(data: dict) -> pd.DataFrame:
        df = pd.DataFrame(data)
        df["time"] = pd.to_datetime(df["time"])
        df = df.set_index("time")
        df = df["temperature"].resample("D").agg(["max", "min"])
        df.columns = ["temp_max", "temp_min"]
        return df

    @task
    def save_data(df: pd.DataFrame) -> None:
        print("Saving the data")
        df.to_csv("data_ny_temp.csv", mode="a", header=False)

    data = get_data()
    df = transform(data)  # type: ignore
    save_data(df)  # type: ignore


weather_data_backfilling()
