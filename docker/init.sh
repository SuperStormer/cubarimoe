#!/bin/sh
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
gunicorn -c docker/gunicorn_config.py cubarimoe.wsgi:application