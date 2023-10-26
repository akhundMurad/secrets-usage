import os

from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient


def get_credentials() -> ClientSecretCredential:
    return ClientSecretCredential(
        tenant_id=os.getenv("AZURE_TENANT_ID"),
        client_id=os.getenv("AZURE_CLIENT_ID"),
        client_secret=os.getenv("AZURE_CLIENT_SECRET"),
    )


def get_secret_client() -> SecretClient:
    credentials = get_credentials()

    return SecretClient(vault_url=os.getenv("AZURE_VAULT_URL"), credential=credentials)
