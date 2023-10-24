#!/bin/bash

poetry run alembic upgrade head

poetry run gunicorn "app.presentation.api.wsgi:build_wsgi()" --bind 0.0.0.0:8000 --log-level debug
