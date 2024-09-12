#!/bin/bash

# Wait for the database to be ready
sleep 5s

# Run Django management commands
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Start uWSGI
uwsgi --ini ./uwsgi.ini
