#!/usr/bin/env bash
set -e

echo "Applying migrations…"
python manage.py migrate --noinput

echo "Starting Django on 0.0.0.0:8000"
python manage.py runserver 0.0.0.0:8000