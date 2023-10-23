from logging import getLogger

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.data_access.errors import DataAccessError

logger = getLogger(__name__)


class UoW:
    def __init__(self, session: Session) -> None:
        self._session = session

    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()

    def __enter__(self) -> "UoW":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.rollback()
        self._session.close()
        if exc_type:
            logger.error("Handled exception: %s - %s", exc_type, exc_val)
        if issubclass(type(exc_val), SQLAlchemyError):
            raise DataAccessError("Integrity error on the database side.")
