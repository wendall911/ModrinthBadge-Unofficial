## Create venv
  1. python3 -m venv .
  1. source bin/activate
  1. pip install -r requirements.txt

## Run app
  1. (ModrinthBadge-Unofficial) ModrinthBadge-Unofficial $ ./bin/gunicorn -c gunicorn.conf.py
  1. When finished simply: deactivate

## Deployment Information
  1. create dotenv
    1. set values
  1. https://docs.gunicorn.org/en/stable/deploy.html

