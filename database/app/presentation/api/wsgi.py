from typing import Callable

from falcon import App
from rodi import Container

from app.business_logic.errors import BusinessLogicError
from app.data_access.errors import DataAccessError
from app.main.di import build_container
from app.presentation.api import controllers, exception_handlers
from app.presentation.errors import PresentationError


def build_wsgi(container_builder: Callable[[], Container] = build_container) -> App:
    app = App()
    container = container_builder()

    app.add_error_handler(
        DataAccessError, exception_handlers.handle_data_access_level_exception
    )
    app.add_error_handler(
        BusinessLogicError, exception_handlers.handle_business_logic_level_exception
    )
    app.add_error_handler(
        PresentationError, exception_handlers.handle_presentation_level_exception
    )
    app.add_error_handler(Exception, exception_handlers.handle_generic_exception)

    app.add_route("/secrets", controllers.SecretsController(container=container))
    return app
