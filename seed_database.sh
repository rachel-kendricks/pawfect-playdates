#!/bin/bash

rm db.sqlite3
rm -rf ./pawfectapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations pawfectapi
python3 manage.py migrate pawfectapi
python3 manage.py loaddata users
python3 manage.py loaddata token
python3 manage.py loaddata size
python3 manage.py loaddata play_style
python3 manage.py loaddata pet
python3 manage.py loaddata like


