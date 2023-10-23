from falcon import Request, Response, status_codes

from app.business_logic.errors import BusinessLogicError
from app.data_access.errors import DataAccessError
from app.presentation.errors import PresentationError


def handle_data_access_level_exception(
    req: Request, resp: Response, exception: DataAccessError, params: dict
) -> None:
    resp.media = {
        "type": "DataAccessException",
        "subtype": type(exception).__name__,
        "message": str(exception),
    }
    resp.status = status_codes.HTTP_BAD_REQUEST


def handle_business_logic_level_exception(
    req: Request, resp: Response, exception: BusinessLogicError, params: dict
) -> None:
    resp.media = {
        "type": "BusinessLogicError",
        "subtype": type(exception).__name__,
        "message": str(exception),
    }
    resp.status = status_codes.HTTP_BAD_REQUEST


def handle_presentation_level_exception(
    req: Request, resp: Response, exception: PresentationError, params: dict
) -> None:
    resp.media = {
        "type": "PresentationError",
        "subtype": type(exception).__name__,
        "message": str(exception),
    }
    resp.status = status_codes.HTTP_CONFLICT


def handle_generic_exception(
    req: Request, resp: Response, exception: Exception, params: dict
) -> None:
    resp.media = {
        "type": "Exception",
        "subtype": "Exception",
        "message": "An error occur, please retry.",
    }
    resp.status = status_codes.HTTP_INTERNAL_SERVER_ERROR
