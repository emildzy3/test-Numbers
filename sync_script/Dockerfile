FROM python:3.10.5-slim

RUN apt-get update && apt-get install -y git libpq-dev postgresql-client

WORKDIR /script

COPY ./sync_script/requirements.txt /script/

RUN pip install -r requirements.txt


COPY ./sync_script /script
