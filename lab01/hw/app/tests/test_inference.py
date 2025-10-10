from app import model


def test_load_sklearn():
    assert model._sklearn_model is not None


def test_load_sentence_transformer():
    assert model._sentence_transformer is not None
