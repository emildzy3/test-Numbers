FROM python:3.10.5-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /server
COPY ../sync_script/requirements.txt /server/
RUN apt-get update && apt-get install -y git libpq-dev postgresql-client
RUN pip install -r requirements.txt

COPY ./server /server



