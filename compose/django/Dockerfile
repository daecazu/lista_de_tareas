FROM python:3.6-alpine
LABEL Daniel Eduardo Canon

ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements
# psycopg2 dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements/dev.txt


RUN apk del .tmp-build-deps

RUN mkdir /app
COPY ./app /app
WORKDIR /app
RUN adduser -D django
USER django