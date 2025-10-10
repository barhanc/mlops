import os

from pydantic import BaseModel
from fastapi import FastAPI

from app.inference import SentimentAnalyzer


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    prediction: str


app = FastAPI()
model = SentimentAnalyzer(
    sklearn_model_path=os.path.join("models", "classifier.joblib"),
    sentence_transformer_path=os.path.join("models", "sentence_transformer.model"),
)


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the Sentiment Analyzer API"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    prediction = model.predict(request.model_dump().get("text"))
    return PredictResponse(prediction=prediction)
