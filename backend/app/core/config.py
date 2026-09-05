from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore",
        case_sensitive=False,
    )

    environment: str = Field(default="local", alias="ROLEREADY_ENV")
    api_title: str = Field(default="RoleReady API", alias="ROLEREADY_API_TITLE")
    cors_origins: str = Field(default="http://localhost:3000", alias="ROLEREADY_CORS_ORIGINS")

    openai_api_key: Optional[str] = Field(default=None, alias="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-4.1-mini", alias="OPENAI_MODEL")

    development_auth_username: Optional[str] = Field(default=None, alias="DEVELOPMENT_AUTH_USERNAME")
    development_auth_password: Optional[str] = Field(default=None, alias="DEVELOPMENT_AUTH_PASSWORD")

    google_client_id: Optional[str] = Field(default=None, alias="GOOGLE_CLIENT_ID")
    google_client_secret: Optional[str] = Field(default=None, alias="GOOGLE_CLIENT_SECRET")
    google_redirect_uri: Optional[str] = Field(default=None, alias="GOOGLE_REDIRECT_URI")

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

    @property
    def openai_enabled(self) -> bool:
        return bool(self.openai_api_key)

    @property
    def google_oauth_configured(self) -> bool:
        return bool(self.google_client_id and self.google_client_secret and self.google_redirect_uri)


@lru_cache
def get_settings() -> Settings:
    return Settings()
