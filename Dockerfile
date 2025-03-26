FROM python:3.11.4-buster

MAINTAINER Luca Francesca <luca@lucafrancesca.me>

ADD requirements.txt /usr/local/bin/

RUN pip install -r /usr/local/bin/requirements.txt

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

CMD flask run --host=0.0.0.0 --port=1234
