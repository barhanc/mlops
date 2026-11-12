# MLOps

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-24.0+-2496ED.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An end-to-end curriculum covering modern Machine Learning Operations (MLOps), data engineering, distributed serving, automated CI/CD pipelines, cloud infrastructure, and LLM systems. Based on the [MLOps Course at AGH University](https://github.com/j-adamczyk/MLOps_course_AGH) by Jakub Adamczyk.

## Overview

<details open>
<summary><b>Lab 1: MLOps Foundations & Serving</b></summary>

- **Focus**: Professional software engineering hygiene for machine learning projects.
- **Key Concepts**:
  - Reproducible dependency and virtual environment management with `uv` and `pyproject.toml`.
  - Static code analysis, linting, formatting, and automated pre-commit hooks (`ruff`).
  - Building production-ready REST APIs for model inference using **FastAPI** with Pydantic validation.
  - Multi-stage **Docker** containerization for compact, reproducible production deployment images.
- **Directory**: [`lab01/`](./lab01/)
</details>

<details>
<summary><b>Lab 2: Databases & Columnar Storage</b></summary>

- **Focus**: Comparing transactional databases with analytical query engines and columnar data formats.
- **Key Concepts**:
  - Relational database querying and connection pooling with **PostgreSQL** (`psycopg`).
  - In-process vectorized analytical SQL querying with **DuckDB**.
  - Benchmarking query throughput, compression, and memory consumption across CSV, SQLite, and **Apache Parquet**.
- **Directory**: [`lab02/`](./lab02/)
</details>

<details>
<summary><b>Lab 3: High-Performance Data Processing with Polars</b></summary>

- **Focus**: Scalable feature preprocessing replacing legacy pandas workflows.
- **Key Concepts**:
  - The **Polars** expression engine: Vectorized column operations built on Apache Arrow in Rust.
  - Eager vs. Lazy execution (`LazyFrame`): Query graph optimization, predicate pushdown, and projection pushdown.
  - Handling out-of-core datasets with streaming execution.
- **Directory**: [`lab03/`](./lab03/)
</details>

<details>
<summary><b>Lab 4: Vector Databases & Semantic Search</b></summary>

- **Focus**: Indexing and querying high-dimensional embedding spaces for semantic retrieval.
- **Key Concepts**:
  - Vector similarity search in relational systems with PostgreSQL and **pgvectorscale**.
  - Dedicated distributed vector database deployment and collection management with **Milvus**.
  - Comparing Approximate Nearest Neighbor (ANN) index architectures: Hierarchical Navigable Small World (HNSW) vs. Inverted File (IVF).
- **Directory**: [`lab04/`](./lab04/)
</details>

<details>
<summary><b>Lab 5: Data & Model Versioning</b></summary>

- **Focus**: End-to-end reproducibility, data provenance, and experiment governance.
- **Key Concepts**:
  - Decoupling code versioning (Git) from large data artifact versioning using **DVC** (Data Version Control).
  - Building modular, cached data preparation and training pipelines (`dvc.yaml`).
  - Tracking hyperparameters, loss curves, and evaluation metrics with **MLflow Tracking**.
  - Registering and transitioning models through deployment stages in the **MLflow Model Registry**.
- **Directory**: [`lab05/`](./lab05/)
</details>

<details>
<summary><b>Lab 6: Data-Centric AI & Model Testing</b></summary>

- **Focus**: Systematic quality assurance for datasets and trained model behavior.
- **Key Concepts**:
  - Finding dataset label errors and corruptions automatically using **Cleanlab**'s Confident Learning algorithms.
  - Automated behavioral and vulnerability testing for ML models with **Giskard** (data leakage, performance bias, robustness).
  - Model interpretability and feature attribution using **SHAP** (Shapley Additive Explanations) and **Captum**.
- **Directory**: [`lab06/`](./lab06/)
</details>

<details>
<summary><b>Lab 7: Model Optimization for Inference</b></summary>

- **Focus**: Compressing deep learning models for low-latency, high-throughput production serving.
- **Key Concepts**:
  - Post-training weight quantization (INT8) and operator fusion in PyTorch.
  - Exporting PyTorch computation graphs to the **ONNX** (Open Neural Network Exchange) open standard.
  - Executing and benchmarking runtime inference with **ONNX Runtime** Execution Providers.
- **Directory**: [`lab07/`](./lab07/)
</details>

<details>
<summary><b>Lab 8: Monitoring & Drift Detection</b></summary>

- **Focus**: Post-deployment observability and maintaining model performance over time.
- **Key Concepts**:
  - Quantifying covariate shift and data drift across input features using **Evidently AI** (Kolmogorov-Smirnov test, Population Stability Index - PSI).
  - Generating automated data health and drift report dashboards.
  - Estimating real-world performance degradation without ground truth labels using **NannyML** (Confidence-Based Performance Estimation - CBPE).
- **Directory**: [`lab08/`](./lab08/)
</details>

<details>
<summary><b>Lab 9: Introduction to Cloud Computing for ML</b></summary>

- **Focus**: Architecting and hosting scalable ML workloads on Amazon Web Services (AWS).
- **Key Concepts**:
  - Storing and partitioning datasets and model weights in **Amazon S3**.
  - Pushing production Docker containers to **Amazon Elastic Container Registry (ECR)**.
  - Deploying containerized prediction microservices on **Amazon ECS** with **AWS Fargate** serverless compute.
  - Managing least-privilege security policies with **AWS IAM** and operational monitoring with **CloudWatch**.
- **Directory**: [`lab09/`](./lab09/)
</details>

<details>
<summary><b>Lab 10: Infrastructure as Code (IaC) with Terraform</b></summary>

- **Focus**: Declarative, automated, and version-controlled infrastructure provisioning.
- **Key Concepts**:
  - Writing modular **Terraform** configuration files (`.tf`) using HCL syntax.
  - Provisioning and configuring **Amazon S3** buckets with lifecycle policies, encryption, versioning, and aliases.
  - Creating reusable Terraform child modules and managing infrastructure state across environments.
  - Integrating multi-provider configurations (AWS and GitHub providers).
- **Directory**: [`lab10/`](./lab10/)
</details>

<details>
<summary><b>Lab 11: Deployment & CI/CD</b></summary>

- **Focus**: Continuous integration and deployment automation for machine learning systems.
- **Key Concepts**:
  - Defining automated **GitHub Actions** workflows triggered on pull requests and releases.
  - Running automated unit tests, code linters, and model checks in CI runners.
  - Building container images with Docker Buildx and pushing images to container registries.
- **Directory**: [`lab11/`](./lab11/)
</details>

<details>
<summary><b>Lab 12: Pipeline Orchestration with Apache Airflow</b></summary>

- **Focus**: Complex workflow scheduling, retries, and automated DAG execution.
- **Key Concepts**:
  - Authoring Directed Acyclic Graphs (**DAGs**) in Python for multi-step ML pipelines.
  - Orchestrating tasks using Airflow operators (PythonOperator, BashOperator, DockerOperator).
  - Managing task dependencies, concurrency, XCom communication, and handling automated failure alerts and retries.
- **Directory**: [`lab12/`](./lab12/)
</details>

<details>
<summary><b>Lab 13: LLMOps & Modern AI Systems</b></summary>

- **Focus**: Serving, controlling, and integrating Generative AI and Large Language Models.
- **Key Concepts**:
  - Dynamic model quantization for memory-efficient local LLM inference.
  - Manual and automated tool-calling workflows for language models.
  - Connecting models to external tools and context using the **Model Context Protocol (MCP)** (clients and custom servers).
  - Validating structured outputs and enforcing safety and format guardrails via **Guardrails AI**.
- **Directory**: [`lab13/`](./lab13/)
</details>

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/barhanc/mlops.git
cd mlops
```

### 2. Running Individual Labs

Individual lab directories (e.g. `lab01/`, `lab02/`, `lab03/`) are self-contained and managed with [uv](https://docs.astral.sh/uv/) or dedicated `pyproject.toml` configurations:

```bash
# Example: Navigating to Lab 3 (Polars)
cd lab03

# Sync environment with uv
uv sync

# Launch JupyterLab
uv run jupyter lab
```

For containerized modules (e.g. `lab01`, `lab04`, `lab12`), refer to the local `README.md` inside each lab directory for `docker-compose up` and service commands.

## Course References

- Original problem statements and course syllabus: [j-adamczyk/MLOps_course_AGH](https://github.com/j-adamczyk/MLOps_course_AGH) by Jakub Adamczyk.
