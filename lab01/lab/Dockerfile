# Dockerfile

# Use a minimal Python image as the base
FROM python:3.12-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    curl libsnappy-dev make gcc g++ libc6-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy files
COPY pyproject.toml uv.lock /app
COPY . .

# Install project dependencies using uv
RUN uv sync --locked

# Expose the application port
EXPOSE 8000

# Run the application with uv
CMD ["uv", "run", "uvicorn", "lab.app:app", "--host", "0.0.0.0", "--port", "8000"]