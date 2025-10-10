import os
import argparse
import yaml

from dotenv import load_dotenv
from lab.settings import Settings


def export_envs(environment: str = "dev") -> None:
    if environment not in ("dev", "test", "prod"):
        raise ValueError(f"Unrecognized {environment=}. Should be one of 'dev', 'test', 'prod'")

    load_dotenv(os.path.join("config", f".env.{environment}"))


def export_secrets(path: str) -> None:
    if not path.endswith(".yaml"):
        raise ValueError("Expected YAML file")

    with open(path, encoding="utf-8") as file:
        secrets = yaml.safe_load(file)
        assert "API_KEY" in secrets
        os.environ["API_KEY"] = secrets["API_KEY"]


def main():
    parser = argparse.ArgumentParser(description="Load environment variables from specified.env file.")
    parser.add_argument("--environment", type=str, default="dev", help="The environment to load (dev, test, prod)")
    parser.add_argument("--secrets-path", type=str, default="./secrets.yaml", help="Path to secrets.yaml file")
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets(args.secrets_path)

    settings = Settings()  # type: ignore

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
