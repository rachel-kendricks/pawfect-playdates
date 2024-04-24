#!/bin/bash

rm db.sqlite3
rm -rf ./playdatesapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations playdatesapi
python3 manage.py migrate playdatesapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

