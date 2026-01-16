import os
import json
import datetime

from dotenv import load_dotenv
from airflow.sdk import dag, task

load_dotenv()


@dag(schedule=datetime.timedelta(minutes=1))
def scheduling_dataset_gathering_with_venvs():

    @task.virtualenv(
        requirements=["twelvedata", "pendulum", "lazy-object-proxy", "cloudpickle"],
        serializer="cloudpickle",
    )
    def get_data(*, logical_date) -> dict:
        from twelvedata import TDClient

        td = TDClient(apikey=os.environ["TWELVEDATA_API_KEY"])
        ts = td.exchange_rate(symbol="USD/EUR", date=logical_date.isoformat())
        return ts.as_json()  # type: ignore

    @task
    def save_data(data: dict) -> None:
        print("Saving the data")

        if not data:
            raise ValueError("No data received")

        with open("data.jsonl", "a+") as file:
            file.write(json.dumps(data))
            file.write("\n")

    data = get_data()  # type: ignore
    save_data(data)


scheduling_dataset_gathering_with_venvs()
