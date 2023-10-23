FROM python:3.11 as python-base

# https://python-poetry.org/docs#ci-recommendations
ENV POETRY_VERSION=1.6.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache


FROM python-base as poetry-base

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}


FROM python-base as app


COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry check
RUN poetry config installer.max-workers 10

RUN poetry install -vvv --no-interaction --no-cache

COPY . /app

RUN groupadd -r backend && useradd -r -g backend backend

RUN chown -R backend /app
RUN chmod u+x /app/entrypoint.sh

USER backend

ENTRYPOINT [ "bash", "/app/entrypoint.sh" ]
