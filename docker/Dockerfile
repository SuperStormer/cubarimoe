FROM ghcr.io/astral-sh/uv:python3.13-alpine

RUN apk update && apk upgrade --no-cache && apk add libpq-dev gcc libc-dev

RUN addgroup -S cubari && adduser -S cubari -G cubari && mkdir /cubarimoe && chown cubari:cubari /cubarimoe
USER cubari

WORKDIR /cubarimoe
COPY uv.lock pyproject.toml ./
RUN uv sync --locked
COPY . ./

CMD ["uv", "run", "./docker/init.sh"]