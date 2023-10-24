from dataclasses import dataclass
from datetime import datetime


@dataclass(kw_only=True)
class SecretDTO:
    secret_id: int
    name: str
    value: str
    iv: str
    created_at: datetime


@dataclass(kw_only=True)
class SecretShortDTO:
    name: str
    value: str
    created_at: datetime
