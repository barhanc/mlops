# MLOps: Production Machine Learning Engineering 🚀⚙️

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-24.0+-2496ED.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Terraform](https://img.shields.io/badge/Terraform-1.7+-844FBA.svg?style=flat&logo=terraform&logoColor=white)](https://www.terraform.io/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-232F3E.svg?style=flat&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Airflow](https://img.shields.io/badge/Apache_Airflow-2.8+-017CEE.svg?style=flat&logo=apache-airflow&logoColor=white)](https://airflow.apache.org/)
[![MLflow](https://img.shields.io/badge/MLflow-2.11+-0194E2.svg?style=flat&logo=mlflow&logoColor=white)](https://mlflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An end-to-end curriculum covering modern Machine Learning Operations (MLOps), data engineering, distributed serving, automated CI/CD pipelines, cloud infrastructure, and LLM systems. Based on the [MLOps Course at AGH University](https://github.com/j-adamczyk/MLOps_course_AGH) by Jacek Adamczyk.

---

## 📑 Overview

| Lab | Module | Core Technologies | Key Concepts & Skills |
| :---: | :--- | :--- | :--- |
| [**01**](./lab01/) | **MLOps Foundations & Serving** | FastAPI, Docker, Ruff, Pre-commit, Git | Dependency management with `uv`, code quality gates, microservice REST API serving, containerization |
| [**02**](./lab02/) | **Databases & Columnar Storage** | PostgreSQL, DuckDB, Apache Parquet | OLTP vs. OLAP database paradigms, vector execution with DuckDB, efficient storage formats |
| [**03**](./lab03/) | **High-Performance Data Processing** | Polars, Apache Arrow | Rust-backed DataFrames, query optimizer, lazy evaluation execution graphs, memory efficiency |
| [**04**](./lab04/) | **Vector Databases & Semantic Search** | pgvectorscale, SQLAlchemy, Milvus | High-dimensional embedding indexing (HNSW, DiskANN), vector similarity queries, RAG retrieval pipelines |
| [**05**](./lab05/) | **Data & Model Versioning** | DVC, MLflow Tracking & Registry | Reproducible data pipelines with DVC, experiment tracking, metric visualization, model artifact staging |
| [**06**](./lab06/) | **Data-Centric AI & Model Testing** | Cleanlab, Giskard, Captum, SHAP | Automated label error detection, out-of-distribution (OOD) tests, adversarial robustness, model explainability |
| [**07**](./lab07/) | **Inference Optimization** | PyTorch, ONNX, ONNX Runtime | Post-training quantization, TorchScript graph tracing, hardware acceleration, latency benchmarking |
| [**08**](./lab08/) | **Monitoring & Drift Detection** | Evidently AI, NannyML | Data drift, concept drift, feature distribution divergence (PSI, KS-test), CBPE performance estimation |
| [**09**](./lab09/) | **Cloud Computing for ML** | AWS (S3, ECR, ECS, Lambda, IAM) | Cloud architecture for ML, serverless model serving, container registry management, security policies |
| [**10**](./lab10/) | **Infrastructure as Code (IaC)** | Terraform, AWS Provider | Declarative infrastructure provisioning, remote state management, reproducible cloud ML environments |
| [**11**](./lab11/) | **CI/CD Automation** | GitHub Actions, Docker Buildx | Automated linting, test suites, multi-arch Docker image builds, automated deployment pipelines |
| [**12**](./lab12/) | **Pipeline Orchestration** | Apache Airflow, Docker Compose | Directed Acyclic Graphs (DAGs), scheduling, dependency resolution, automated retraining and batch inference |
| [**13**](./lab13/) | **LLMOps & Modern AI Systems** | vLLM, Model Context Protocol (MCP), Guardrails | High-throughput PagedAttention LLM serving, tool use with MCP, hallucination control and output validation |

---

## 🔬 Detailed Lab Breakdown

<details open>
<summary><b>Lab 1: MLOps Foundations & Serving</b></summary>

- **Focus**: Professional software engineering hygiene for machine learning projects.
- **Key Concepts**:
  - Reproducible dependency and virtual environment management with `uv` and `pyproject.toml`.
  - Static code analysis, linting, formatting, and automated pre-commit hooks (`ruff`).
  - Building production-ready REST APIs for model inference using **FastAPI** with Pydantic request/response validation.
  - Multi-stage **Docker** containerization for compact, reproducible production deployment images.
- **Directory**: [`lab01/`](./lab01/)
</details>

<details>
<summary><b>Lab 2: Databases & Columnar Storage</b></summary>

- **Focus**: Comparing transactional databases with modern analytical query engines and columnar data formats.
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

- **Focus**: Indexing and querying high-dimensional embedding spaces for Retrieval-Augmented Generation (RAG).
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
  - Executing and benchmarking optimized runtime inference with **ONNX Runtime** Execution Providers.
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
  - Deploying scalable containerized prediction microservices on **Amazon ECS** (Elastic Container Service) and serverless inference with **AWS Lambda**.
  - Managing least-privilege security policies with **AWS IAM**.
- **Directory**: [`lab09/`](./lab09/)
</details>

<details>
<summary><b>Lab 10: Infrastructure as Code (IaC) with Terraform</b></summary>

- **Focus**: Declarative, automated, and version-controlled cloud infrastructure provisioning.
- **Key Concepts**:
  - Writing modular **Terraform** configuration files (`.tf`) for AWS cloud resources.
  - Managing remote state backends with state locking via DynamoDB and S3.
  - Provisioning compute instances (EC2), security groups, networking (VPC/Subnets), and storage for ML services.
- **Directory**: [`lab10/`](./lab10/)
</details>

<details>
<summary><b>Lab 11: Deployment & CI/CD</b></summary>

- **Focus**: Continuous integration and deployment automation for machine learning systems.
- **Key Concepts**:
  - Defining automated **GitHub Actions** workflows triggered on pull requests and releases.
  - Running automated unit tests, code linters, and model regression checks in CI runners.
  - Building multi-platform container images with Docker Buildx and pushing signed images to registries.
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
  - High-throughput LLM serving using **vLLM** with PagedAttention and continuous batching.
  - Connecting models to external tools and context using the **Model Context Protocol (MCP)**.
  - Validating structured JSON outputs and enforcing safety, compliance, and hallucination guardrails via Guardrails AI.
- **Directory**: [`lab13/`](./lab13/)
</details>

---

## 🚀 Getting Started

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

---

## 📖 Course References

- Original problem statements and course syllabus: [j-adamczyk/MLOps_course_AGH](https://github.com/j-adamczyk/MLOps_course_AGH) by Jacek Adamczyk.
