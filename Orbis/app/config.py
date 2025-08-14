import os
from pathlib import Path
from functools import lru_cache

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine

basedir = Path(__file__).parents[1]
load_dotenv(basedir / ".env")


class Settings(BaseSettings):
    name: str = os.getenv("SERVICE_NAME", "template-backend-service")
    version: str = "0.1.0"
    commit: str = os.getenv("COMMIT", "unknown")
    branch: str = os.getenv("BRANCH", "unknown")
    build_time: str = os.getenv("BUILD_TIME", "unknown")
    build_number: str = os.getenv("BUILD_NUMBER", "unknown")
    build_tags: tuple = tuple(os.getenv("BUILD_TAGS", "").split())

    env: str = os.getenv("ENV", "dev")
    debug: bool = bool(int(os.getenv("DEBUG", "1")))
    allowed_origins: tuple[str] = tuple(os.getenv("CORS_ORIGINS", "*").split(","))

    engine_url = f"{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    engine_str: str = f"{os.getenv('DB_DIALECT')}+{os.getenv('DB_DRIVER')}://{engine_url}" \
        if os.getenv("DB_HOST") else "sqlite+aiosqlite:///:memory:"
    supports_schema = bool(int(os.getenv("DB_SUPPORTS_SCHEMA", "0")))
    master_api_key: str = os.getenv("MASTER_API_KEY", "12345678-unsafe-master-key")

    class subservices:  # noqa
        pass


@lru_cache()
def get_settings():
    return Settings()


@lru_cache()
def get_engine(schema: str):
    settings = get_settings()
    if settings.supports_schema:
        engine = create_async_engine(
            settings.engine_str,
            execution_options={"schema_translate_map": {None: schema}}
        )
    else:
        engine = create_async_engine(settings.engine_str)
    return engine
