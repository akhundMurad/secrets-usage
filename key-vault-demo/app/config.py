from dataclasses import dataclass
from typing import Type, TypeVar

from azure.core.exceptions import ResourceNotFoundError

from .vault import get_secret_client

T = TypeVar("T")


@dataclass(frozen=True, kw_only=True)
class DatabaseSettings:
    connection_string: str

    @classmethod
    def load_from_env(cls) -> "DatabaseSettings":
        return cls(connection_string=get_from_env("DATABASE-CONNECTION-STRING"))


def get_from_env(var_name: str, default: T | None = None, type_: Type[T] = str) -> T:  # type: ignore [assignment]
    secret_client = get_secret_client()

    try:
        secret = secret_client.get_secret(var_name)
        value = secret.value
    except ResourceNotFoundError:
        value = default
    return type_(value)  # type: ignore [call-arg]
