#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata category/fixtures/category.json

exec "$@"