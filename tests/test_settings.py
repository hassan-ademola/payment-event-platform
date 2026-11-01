import pytest

from payment_event_platform.settings import Settings


def test_environment_variables_override_defaults(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("APP_NAME", "Test Platform")
    monkeypatch.setenv("APP_ENV", "testing")
    monkeypatch.setenv(
        "DATABASE_URL",
        "postgresql://localhost:5432/test_db",
    )

    settings = Settings()

    assert settings.app_name == "Test Platform"
    assert settings.environment == "testing"
    assert settings.database_url == (
        "postgresql://localhost:5432/test_db"
    )