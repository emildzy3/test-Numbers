FROM python:3.10.5-slim

RUN apt-get update && apt-get install -y git libpq-dev postgresql-client

WORKDIR /server

COPY ./page_web/requirements.txt /server/


RUN pip install -r requirements.txt


COPY ./page_web /server
