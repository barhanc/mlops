import torch
import joblib

from cleantext import clean
from sentence_transformers import SentenceTransformer


def _load_sklearn_model(path: str):
    with open(path, "rb") as file:
        model = joblib.load(file)
    return model


def _load_sentence_transformer(path: str) -> SentenceTransformer:
    return SentenceTransformer(model_name_or_path=path)


def _get_device():
    if torch.cuda.is_available():
        return "cuda"
    if torch.mps.is_available():
        return "mps"
    return "cpu"


class Inference:
    sentiment_map = {0: "negative", 1: "neutral", 2: "positive"}

    def __init__(self, sklearn_model_path: str, sentence_transformer_path: str):
        self._sklearn_model = _load_sklearn_model(sklearn_model_path)
        self._sentence_transformer = _load_sentence_transformer(sentence_transformer_path)
        self._device = _get_device()

    def _validate_input(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Expected input to be a string")
        if len(text.strip()) < 3:
            raise ValueError("Text is too short to analyze")

        return text

    def _preprocess(self, text: str) -> str:
        text = self._validate_input(text)
        text = clean(text)
        return text

    def predict(self, text: str) -> str:
        try:
            text = self._preprocess(text)
            embeddings = self._sentence_transformer.encode([text], device=self._device)
            sentiment = self._sklearn_model.predict(embeddings)
            sentiment = sentiment[0]

            return self.sentiment_map[sentiment]

        except Exception as e:
            return f"ERROR: {e}"
