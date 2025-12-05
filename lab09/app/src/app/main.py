import os

from pydantic import BaseModel
from fastapi import FastAPI

from app.inference import Inference


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    prediction: str


app = FastAPI()
model = Inference(
    sklearn_model_path=os.path.join("artifacts", "classifier.joblib"),
    sentence_transformer_path=os.path.join("artifacts", "sentence_transformer.model"),
)


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    return PredictResponse(prediction=model.predict(request.text))
