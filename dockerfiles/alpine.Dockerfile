#FROM tiangolo/uwsgi-nginx-flask:python3.7
FROM tiangolo/meinheld-gunicorn:python3.7-alpine3.8

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

RUN pip install --upgrade pip

RUN apk update \
    && apk add --no-cache --virtual build-deps gcc postgresql-dev python3-dev musl-dev \
    && pip install psycopg2 \
    && apk add --no-cache jpeg-dev zlib-dev libjpeg \
    && apk add --no-cache g++ freetype-dev jpeg-dev

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]