FROM python:3.13-alpine

RUN apk update && apk upgrade --no-cache && apk add libpq-dev gcc libc-dev 

RUN pip install uv>=0.7.9

RUN addgroup -S cubari && adduser -S cubari -G cubari && mkdir -p /cubarimoe/static && chown cubari:cubari /cubarimoe /cubarimoe/static
USER cubari

WORKDIR /cubarimoe
COPY uv.lock pyproject.toml ./
RUN uv sync --locked
COPY . ./

CMD ["uv", "run", "./docker/init.sh"]