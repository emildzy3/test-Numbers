FROM python:3.10.5-slim

RUN apt-get update && apt-get install -y git libpq-dev postgresql-client

WORKDIR /tg_bot

COPY ./tg_bot/requirements.txt /tg_bot/

RUN pip install -r requirements.txt


COPY ./tg_bot /tg_bot
