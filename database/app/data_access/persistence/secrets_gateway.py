from datetime import datetime

from sqlalchemy.orm import Session

from app.business_logic.dto.secrets import SecretDTO
from app.data_access.persistence.tables import secrets_table


class SecretsGateway:
    def __init__(self, session: Session) -> None:
        self._session = session

    def find_by_name(self, *, name: str) -> SecretDTO | None:
        statement = secrets_table.select().where(secrets_table.c.name == name)
        result = self._session.execute(statement)
        secret = result.first()

        return (
            SecretDTO(
                secret_id=secret.secret_id,
                name=secret.name,
                value=secret.value,
                iv=secret.iv,
                created_at=secret.created_at,
            )
            if secret
            else None
        )

    def insert(self, *, name: str, value: str, iv: str) -> None:
        statement = secrets_table.insert().values(
            name=name, value=value, iv=iv, created_at=datetime.utcnow()
        )
        self._session.execute(statement)
