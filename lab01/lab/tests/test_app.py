# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from fastapi.testclient import TestClient
from lab.app import app

client = TestClient(app)


def test_welcome_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict():
    response = client.post(
        "/predict",
        json={"sepal_length": 0.0, "sepal_width": 0.0, "petal_length": 0.0, "petal_width": 0.0},
    )
    assert response.status_code == 200
    assert response.json() == {"prediction": "setosa"}
