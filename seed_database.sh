#!/bin/bash

rm db.sqlite3
rm -rf ./pawfectapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations pawfectapi
python3 manage.py migrate pawfectapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

