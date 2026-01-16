import datetime

from airflow.sdk import dag, task, Variable
from airflow.providers.postgres.hooks.postgres import PostgresHook


POSTGRES_CONN_ID = "postgres_storage"


@dag(schedule=datetime.timedelta(minutes=1))
def scheduling_dataset_gathering_with_venvs_and_connections():

    @task.virtualenv(
        requirements=["twelvedata", "pendulum", "lazy-object-proxy", "cloudpickle"],
        serializer="cloudpickle",
        python_version="3",
        system_site_packages=False,
    )
    def get_data(*, apikey: str, logical_date) -> dict:
        from twelvedata import TDClient

        td = TDClient(apikey)
        ts = td.exchange_rate(symbol="USD/EUR", date=logical_date.isoformat())
        return ts.as_json()  # type: ignore

    @task
    def save_data(data: dict) -> None:
        print("Saving the data")
        if not data:
            raise ValueError("No data received")

        pg_hook = PostgresHook(postgres_conn_id="postgres_storage")
        pg_hook.insert_rows(
            table="exchange_rates",
            rows=[(data["symbol"], data["rate"])],
            target_fields=["symbol", "rate"],
        )

    data = get_data(apikey=Variable.get("TWELVEDATA_API_KEY"))  # type: ignore
    save_data(data)


scheduling_dataset_gathering_with_venvs_and_connections()
