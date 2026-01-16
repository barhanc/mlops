import requests
import pandas as pd

from airflow.sdk import dag, task, ObjectStoragePath


API = "https://archive-api.open-meteo.com/v1/archive"
base = ObjectStoragePath("s3://aws_default@weather-data/")


@dag()
def weather_data_s3_integration():
    @task
    def get_data() -> dict:
        print("Fetching data from API")
        # New York temperature in 2025
        params = {
            "latitude": 40.7143,
            "longitude": -74.006,
            "start_date": "2025-01-01",
            "end_date": "2025-12-31",
            "hourly": "temperature_2m",
            "timezone": "auto",
        }
        resp = requests.get(API, params=params)
        resp.raise_for_status()

        data = resp.json()
        data = {"time": data["hourly"]["time"], "temperature": data["hourly"]["temperature_2m"]}
        return data

    @task
    def transform(data: dict) -> pd.DataFrame:
        df = pd.DataFrame(data)
        df["temperature"] = df["temperature"].clip(lower=-20, upper=50)
        return df

    @task
    def save_data(df: pd.DataFrame, **context) -> None:
        print("Saving the data")
        logical_date = context["logical_date"]

        # ensure the bucket exists
        base.mkdir(exist_ok=True)

        path = base / f"ny_temp_{logical_date.format('YYYYMMDD')}.csv"
        with path.open("wb") as file:
            df.to_csv(file, index=False)

    data = get_data()
    df = transform(data)  # type:ignore
    save_data(df)  # type:ignore


weather_data_s3_integration()
