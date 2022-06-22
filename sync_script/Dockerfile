FROM python:3.10.5-slim

WORKDIR /script

COPY requirements.txt /script/

#RUN apt-get update && apt-get install -y git libpq-dev postgresql-client && apt-get install -y python3-pip
RUN pip install -r requirements.txt
#RUN chmod +x /sync_script/get_data_sheet.py
COPY ./ /script
#CMD ["python3", "/sync_script/get_data_sheet.py"]

