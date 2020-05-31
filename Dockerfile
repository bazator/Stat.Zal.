FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y python-pip python-dev python3-dev python3-pip

ENV STATIC_URL /static
ENV STATIC_PATH /home/docker-server/www/app/static
COPY ./requirements.txt /var/www/requirements.txt

WORKDIR /app

COPY . /app
COPY templates /app/templates

RUN python3 -m pip install -r /app/requirements.txt 
ENV FLASK_APP /app/main.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
RUN python3 -m flask init-db
RUN python3 -m flask insert-data polish_names.csv

CMD [ "python3", "/app/main.py" ]
