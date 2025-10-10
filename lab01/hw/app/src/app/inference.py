# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import joblib

from cleantext import clean
from sentence_transformers import SentenceTransformer


def load_sklearn_model(path: str):
    with open(path, "rb") as file:
        model = joblib.load(file)
    return model


def load_sentence_transformer(path: str) -> SentenceTransformer:
    return SentenceTransformer(model_name_or_path=path)


class SentimentAnalyzer:
    sentiment_map = {0: "negative", 1: "neutral", 2: "positive"}

    def __init__(self, sklearn_model_path: str, sentence_transformer_path: str):
        self._sklearn_model = load_sklearn_model(sklearn_model_path)
        self._sentence_transformer = load_sentence_transformer(sentence_transformer_path)

    def predict(self, text: str) -> str:
        text = clean(text)

        embeddings = self._sentence_transformer.encode([text])
        sentiment = self._sklearn_model.predict(embeddings)
        sentiment = sentiment[0]

        return self.sentiment_map[sentiment]
