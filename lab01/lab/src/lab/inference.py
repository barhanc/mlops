import joblib
import numpy as np


def load_model(path: str):
    """Loads the trained model from file."""
    with open(path, "rb") as file:
        clf = joblib.load(file)
    return clf


def predict(clf, inp: dict[str, float]) -> str:
    """Uses the model to make predictions, returning predicted class as a string"""
    x = list(inp.values())
    x = np.array(x).reshape(1, -1)
    y = clf.predict(x)
    return y[0]
