from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Payment Event Platform"

    environment: str = Field(
        default="local",
        validation_alias="APP_ENV",
    )

    database_url: str | None = Field(
        default=None,
        validation_alias="DATABASE_URL",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )