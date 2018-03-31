FROM python:3.6-alpine3.7

RUN apk --no-cache add --virtual .builddeps gcc gfortran musl-dev     && pip install numpy==1.14.0     && apk del .builddeps     && rm -rf /root/.cache

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt

ADD . /opt/webapp/
WORKDIR /opt/webapp

RUN adduser -D myuser
USER myuser

CMD gunicorn --bind 0.0.0.0:$PORT wsgi
