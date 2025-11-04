"""
Application settings using Pydantic's BaseSettings.

These settings are loaded from environment variables if present,
otherwise default values are used.  Copy ``.env.example`` to ``.env``
and adjust the values for your environment.
"""

from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application configuration.

    Attributes correspond to environment variables with the same name.
    """

    database_url: str = "sqlite:///./nutrisigno.db"
    agnos_api_key: str = "changeme"
    secret_key: str = "changeme"
    mercado_pago_token: str = "changeme"

    class Config:
        env_prefix = "NUTRISIGNO_"
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    """Retrieve the cached settings object."""
    return Settings()