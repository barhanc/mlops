ARG AIRFLOW_IMAGE_NAME=apache/airflow:3.1.5-python3.11
FROM ${AIRFLOW_IMAGE_NAME}

USER root
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN mkdir -p /opt/airflow/.uv-cache && chown -R airflow:root /opt/airflow/.uv-cache

WORKDIR /opt/airflow
COPY pyproject.toml uv.lock ./

RUN uv pip install --system pyproject.toml --group airflow_common
RUN chown -R airflow:root /opt/airflow

USER airflow