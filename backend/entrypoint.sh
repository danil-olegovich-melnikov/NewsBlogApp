#!/bin/bash

python3 manage.py makemigrations &&
python3 manage.py migrate &&
python3 manage.py runserver 0.0.0.0:8000 &&
celery -A config worker -l info &&
celery -A config beat -l info
#command: ["celery", "-A", "config", "worker", "-l", "info"]
