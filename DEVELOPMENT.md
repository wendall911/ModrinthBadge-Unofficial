## Install Dependencies Fedora / Rocky Linux 8/9 / RHEL 8/9
  1. dnf install dejavu-sans-fonts python3-pillow python3-gunicorn python3-dotenv python3-flask

## Run app
  1. $ gunicorn ModrinthBadge:api -c gunicorn.conf.py

## Deployment Information
  1. create dotenv
    1. set values
  1. https://docs.gunicorn.org/en/stable/deploy.html

