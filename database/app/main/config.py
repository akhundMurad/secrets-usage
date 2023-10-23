import os
from dataclasses import dataclass
from typing import Type, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, kw_only=True)
class ApplicationSettings:
    secret_key: str

    @classmethod
    def load_from_env(cls) -> "ApplicationSettings":
        return cls(secret_key=get_from_env("SECRET_KEY"))


@dataclass(frozen=True, kw_only=True)
class DatabaseSettings:
    connection_string: str

    @classmethod
    def load_from_env(cls) -> "DatabaseSettings":
        return cls(connection_string=get_from_env("DATABASE_CONNECTION_STRING"))


def get_from_env(var_name: str, default: T | None = None, type_: Type[T] = str) -> T:  # type: ignore [assignment]
    value = os.getenv(var_name, default)
    if not value:
        raise RuntimeError(f"There is no {var_name} in the environment.")
    return type_(value)  # type: ignore [call-arg]
