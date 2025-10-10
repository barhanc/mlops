import os
import lab.inference
from fastapi import FastAPI
from lab.api.models.iris import PredictRequest, PredictResponse


app = FastAPI()
model = lab.inference.load_model(os.path.join("models", "iris.joblib"))


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    prediction = lab.inference.predict(model, request.model_dump())
    return PredictResponse(prediction=prediction)
