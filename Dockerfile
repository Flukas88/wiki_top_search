FROM ubuntu:latest
  
MAINTAINER Luca Francesca <luca@lucafrancesca.me>

RUN apt-get update -y && apt-get install --no-install-recommends -y python-pip python-dev build-essential && rm -rf /var/lib/apt/lists/* 

ADD requirements.txt /usr/local/bin/

RUN pip install setuptools && pip install -r /usr/local/bin/requirements.txt

ENV BASE_DIR=/srv

ENV APP_DIR=$BASE_DIR/application/

ADD ./src $APP_DIR/src

COPY ./static/status_style.css $APP_DIR/static/status_style.css

COPY ./static/style_cobalt.css $APP_DIR/static/style.css 

ADD ./templates $APP_DIR/templates

ADD main.py $APP_DIR

ENV FLASK_APP=main.py

VOLUME $APP_DIR

WORKDIR $APP_DIR
CMD flask run --host=0.0.0.0
