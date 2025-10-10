import os
import joblib

from sklearn.datasets import load_iris
from sklearn.ensemble import HistGradientBoostingClassifier


def load_data():
    """Lads and returns the iris dataset."""
    return load_iris()  # type: ignore


def train_model(X_train, y_train):
    """Trains simple classification model and returns it."""
    clf = HistGradientBoostingClassifier(random_state=0)
    clf.fit(X_train, y_train)
    return clf


def save_model(clf, path: str):
    """Saves the trained model to file using joblib."""
    with open(path, "wb") as file:
        joblib.dump(clf, file, protocol=5)


def main():
    iris = load_data()
    X, y = iris.data, iris.target_names[iris.target]
    clf = train_model(X, y)
    save_model(clf, path=os.path.join("models", "iris.pkl"))


if __name__ == "__main__":
    main()
