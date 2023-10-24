from base64 import b64decode, b64encode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from app.business_logic.dto.secrets import SecretShortDTO
from app.business_logic.errors import BusinessLogicError
from app.data_access.persistence.secrets_gateway import SecretsGateway
from app.data_access.persistence.uow import UoW
from app.main.config import ApplicationSettings


class SecretsService:
    def __init__(
        self,
        application_settings: ApplicationSettings,
        secrets_gateway: SecretsGateway,
        uow: UoW,
    ) -> None:
        self._application_settings = application_settings
        self._secrets_gateway = secrets_gateway
        self._uow = uow

    def create_secret(self, *, name: str, plain_value: str) -> None:
        with self._uow as uow:
            aes = AES.new(
                key=bytes(self._application_settings.secret_key, encoding="utf-8"),
                mode=AES.MODE_CBC,
            )
            plain_value_buffer = bytes(plain_value, encoding="utf-8")
            padded = pad(plain_value_buffer, AES.block_size)
            encrypted_value = aes.encrypt(padded)
            self._secrets_gateway.insert(
                name=name,
                value=b64encode(encrypted_value).decode(),
                iv=b64encode(aes.iv).decode(),
            )
            uow.commit()

    def get_secret_by_name(self, *, name: str) -> SecretShortDTO:
        with self._uow as uow:
            secret = self._secrets_gateway.find_by_name(name=name)
            if not secret:
                raise BusinessLogicError
            iv = b64decode(secret.iv)
            value = b64decode(secret.value)
            aes = AES.new(
                key=bytes(self._application_settings.secret_key, encoding="utf-8"),
                mode=AES.MODE_CBC,
                iv=iv,
            )
            decrypted_value = unpad(aes.decrypt(value), AES.block_size).decode()
            uow.commit()

        return SecretShortDTO(
            name=secret.name, value=decrypted_value, created_at=secret.created_at
        )
