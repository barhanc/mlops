from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_predict_positive():
    response = client.post("/predict", json={"text": "You're great!"})
    assert response.status_code == 200
    assert response.json() == {"prediction": "positive"}


def test_predict_neutral():
    response = client.post("/predict", json={"text": "This is a horse"})
    assert response.status_code == 200
    assert response.json() == {"prediction": "neutral"}


def test_predict_negative():
    response = client.post("/predict", json={"text": "You're so lazy and irresponsible"})
    assert response.status_code == 200
    assert response.json() == {"prediction": "negative"}


def test_predict_invalid_text_returns_ok():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 200
    assert response.json().get("prediction").startswith("ERROR")
