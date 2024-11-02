import multiprocessing
# https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv
from os import getenv

load_dotenv()

IP = getenv('IP')
PORT = getenv('PORT')
ENV = getenv('ENV')

# https://docs.gunicorn.org/en/latest/settings.html#settings
if IP and PORT:
    bind = IP + ":" + PORT
else:
    bind = "127.0.0.1:8000"

if ENV and ENV == "prod":
    workers = multiprocessing.cpu_count() * 2 + 1
    loglevel = 'warning'
else:
    workers = 3
    accessLog = '-'
    loglevel = 'debug'

reload = True
reload_extra_files = ["templates", "website"]
wsgi_app = "ModrinthBadge:api"
