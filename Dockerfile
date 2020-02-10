FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

RUN pip install --upgrade pip

WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]