FROM python:3.9.20-slim

COPY . /ecomerce 

WORKDIR /ecomerce

RUN apt update

RUN apt upgrade -y

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install -r requirements.txt

CMD /opt/venv/bin/gunicorn ecomerce.wsgi:application --bind 0.0.0.0:8000