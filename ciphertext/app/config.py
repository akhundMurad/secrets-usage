import os
from dataclasses import dataclass
from pathlib import Path
from typing import Type, TypeVar

from dotenv import load_dotenv

load_dotenv("config/.envfile")

T = TypeVar("T")


@dataclass(frozen=True, kw_only=True)
class TokenSettings:
    secret_key: str
    algorithm: str
    expires_minutes: int

    @classmethod
    def load_from_env(cls) -> "TokenSettings":
        return cls(
            secret_key=get_from_env("TOKEN_SECRET_KEY"),
            algorithm=get_from_env("TOKEN_ALGORITHM", "HS256"),
            expires_minutes=get_from_env("TOKEN_EXPIRES_MINUTES", 60, int),
        )


@dataclass(frozen=True, kw_only=True)
class DatabaseSettings:
    connection_string: str

    @classmethod
    def load_from_env(cls) -> "DatabaseSettings":
        return cls(connection_string=get_from_env("DATABASE_CONNECTION_STRING"))


@dataclass(frozen=True, kw_only=True)
class AccessSettings:
    load_images_access_token: str

    @classmethod
    def load_from_env(cls) -> "AccessSettings":
        return cls(load_images_access_token=get_from_env("LOAD_IMAGES_ACCESS_TOKEN"))


@dataclass(frozen=True, kw_only=True)
class StorageSettings:
    base_dir: Path

    @classmethod
    def load_from_env(cls) -> "StorageSettings":
        return cls(base_dir=get_from_env("STORAGE_BASE_DIR", type_=Path))


def get_from_env(var_name: str, default: T | None = None, type_: Type[T] = str) -> T:  # type: ignore [assignment]
    value = os.getenv(var_name, default)
    if not value:
        raise RuntimeError(f"There is no {var_name} in the environment.")
    return type_(value)  # type: ignore [call-arg]
