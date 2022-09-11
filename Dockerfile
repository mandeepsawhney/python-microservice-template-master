FROM python:3.7 as build

RUN pip install pipenv

COPY ./ /app
WORKDIR /app

RUN pipenv lock -r > requirements.txt

FROM python:3.7-alpine

COPY --from=build /app/requirements.txt /app/
COPY app.py config.py extensions.py /app/
COPY src /app/src/
COPY .git /app/.git

WORKDIR /app

RUN \
  apk update && \
  apk add --no-cache postgresql-libs git curl && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps

ENV FLASK_RUN_PORT 3080
ENV WORKER_COUNT 4

ENTRYPOINT gunicorn -w $WORKER_COUNT --log-level info --forwarded-allow-ips='*' -b :$FLASK_RUN_PORT app:app
