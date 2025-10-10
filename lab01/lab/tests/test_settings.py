from lab.settings import Settings


def test_settings_load_correct():
    settings = Settings()  # type: ignore
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "lab"
    assert settings.API_KEY == "test-api-key"
