FROM alpine:3.1

RUN apk add --update python py-pip

WORKDIR /app

ADD requirements.txt /app
RUN pip install -r requirements.txt

ADD . /app
