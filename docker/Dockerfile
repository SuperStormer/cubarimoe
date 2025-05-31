FROM ghcr.io/astral-sh/uv:python3.13-alpine

RUN apk update && apk upgrade --no-cache && apk add libpq-dev gcc libc-dev

WORKDIR /cubarimoe
COPY uv.lock pyproject.toml ./
RUN uv sync --locked && apk del gcc
COPY . ./

CMD ["uv", "run", "./docker/init.sh"]