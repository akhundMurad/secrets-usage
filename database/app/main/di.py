from rodi import ActivationScope, Container, ServiceLifeStyle
from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.business_logic.services.secrets_service import SecretsService
from app.data_access.persistence.secrets_gateway import SecretsGateway
from app.data_access.persistence.uow import UoW
from app.main.config import ApplicationSettings, DatabaseSettings


def build_container() -> Container:
    container = Container()

    container.register(SecretsService)
    container.register(SecretsGateway)
    container.register(UoW)
    container.register_factory(
        ApplicationSettings.load_from_env,
        ApplicationSettings,
        life_style=ServiceLifeStyle.SCOPED,
    )
    container.register_factory(
        DatabaseSettings.load_from_env,
        DatabaseSettings,
        life_style=ServiceLifeStyle.SCOPED,
    )
    container.register_factory(
        provide_sqlachemy_session, Session, life_style=ServiceLifeStyle.SCOPED
    )
    container.register_factory(
        provide_sqlalchemy_engine, Engine, life_style=ServiceLifeStyle.SINGLETON
    )
    container.register_factory(
        provide_sqlalchemy_sessionmaker,
        sessionmaker,
        life_style=ServiceLifeStyle.SCOPED,
    )

    return container


def provide_sqlalchemy_engine(scope: ActivationScope) -> Engine:
    settings = scope.get(DatabaseSettings)
    return create_engine(settings.connection_string)


def provide_sqlalchemy_sessionmaker(scope: ActivationScope) -> sessionmaker:
    engine = scope.get(Engine)
    return sessionmaker(bind=engine)


def provide_sqlachemy_session(scope: ActivationScope) -> Session:
    session_maker = scope.get(sessionmaker)
    return session_maker()
