from .config import DatabaseSettings
from .vault import get_secret_client


def main() -> None:
    secret_client = get_secret_client()

    database_connection_string = secret_client.get_secret("DATABASE-CONNECTION-STRING")

    print(database_connection_string)

    print(DatabaseSettings.load_from_env())


if __name__ == "__main__":
    main()
