FROM tiangolo/uwsgi-nginx:python3.7

COPY ./app.py /app/app.py
COPY ./deploy/uwsgi/prod.ini /app/uwsgi.ini

WORKDIR /app
