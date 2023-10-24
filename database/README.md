# Storing in the dedicated database

## Usage

1. Run server

```bash
docker-compose build
docker-compose up
```

2. Create a secret

```bash
curl --request POST --location 'http://0.0.0.0:8000/secrets' \
--header 'Content-Type: application/json' \
--data '{"name": "pass", "plain_value": "67551363-5574-40a9-a72b-8fe16afd75b4"}'
```

3. Get a secret

```bash
curl --location 'http://0.0.0.0:8000/secrets?secret_name=pass'
```
