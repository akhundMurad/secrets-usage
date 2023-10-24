from dataclass_factory import Factory
from falcon import HTTP_201, Request, Response
from rodi import Container

from app.business_logic.services.secrets_service import SecretsService


class SecretsController:
    def __init__(self, container: Container) -> None:
        self._container = container
        self._factory = Factory()

    def on_post(self, req: Request, resp: Response) -> None:
        service = self._container.resolve(SecretsService)
        service.create_secret(
            name=req.media["name"], plain_value=req.media["plain_value"]
        )
        resp.status = HTTP_201

    def on_get(self, req: Request, resp: Response) -> None:
        secret_name = req.get_param("secret_name", required=True)
        service = self._container.resolve(SecretsService)
        secret = service.get_secret_by_name(name=secret_name)
        resp.media = self._factory.dump(secret)
