import time
import torch

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModel

app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/multi-qa-mpnet-base-cos-v1")
model = AutoModel.from_pretrained("sentence-transformers/multi-qa-mpnet-base-cos-v1")
model = torch.ao.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
model.load_state_dict(torch.load("model.wts", weights_only=True))
model.eval()
model = torch.compile(model)


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    embedding: list[float]
    server_time: float


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    t = time.perf_counter()

    inputs = tokenizer(request.text, truncation=True, padding="max_length", return_tensors="pt")
    with torch.inference_mode():
        _ = model(**inputs)

    t = time.perf_counter() - t

    # Return mock embedding. For real application it needs to be computed from
    # the last hidden state.
    return PredictResponse(embedding=[0, 0, 0], server_time=t)
