import datetime
import html
import json
import logging
import re
import time
import urllib.request

from flask import Flask
from os import getenv
from urllib.error import HTTPError

logger = logging.getLogger(__name__)
api = Flask(__name__, static_folder='website', static_url_path='')

API_URL = getenv('API') + '/v3'
ENV = getenv('ENV')
CACHE_AGE = 10800

if ENV and ENV != "prod":
    api.debug = True
    CACHE_AGE = 0

def timedLruCache(expireSeconds: int):
    def decorator(func):
        cache = {}

        def wrapper(*args, **kwargs):
            key = (*args, *kwargs.items())
            if key in cache:
                value, timestamp = cache[key]
                if datetime.datetime.now() - datetime.datetime.fromtimestamp(timestamp) < datetime.timedelta(seconds=expireSeconds):
                    api.logger.debug("Retrieving result from cache...")
                    return value
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result

        return wrapper

    return decorator

@timedLruCache(expireSeconds=CACHE_AGE)
def performApiCall():
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('user-agent', 'wendall911/modrinth.roughness.technology/1.0'),
        ('Accept', 'application/json')
    ]

    return opener

def getProject(project):
    project = project.split('?')[0].split('/')[0]
    apiCall = performApiCall()

    try:
        apiResponse = apiCall.open(API_URL + '/project/' + project)
    except HTTPError as e:
        if e.code == 404:
            return {}

    return json.loads(apiResponse.read())

def getDownloadsProject(project):
    apiResponse = getProject(project)

    return '{:,}'.format(int(apiResponse['downloads'])) if apiResponse else '404'

def getVersions(project):
    apiResponse = getProject(project)
    keyVersions = [
        "1.6.4",
        "1.7.10",
        "1.8.9",
        "1.9.4",
        "1.10.2",
        "1.11.2",
        "1.12.2",
        "1.16.5",
        "1.18.2",
        "1.19.2",
        "1.20.1",
        "1.21.1",
        "1.21.9",
        "1.21.10",
        "1.21.11",
        "26.1"
    ]
    if apiResponse:
        gameVersionsList = apiResponse['game_versions']
        return [x for x in gameVersionsList if x in keyVersions][::-1]
    else:
        return ['404']

def getDownloadsAuthor(name):
    apiCall = performApiCall()

    try:
        url = API_URL + '/user/' + name.lower() + '/projects'
        apiResponse = apiCall.open(url)
    except HTTPError as e:
        if e.code == 404:
            return '404'

    results = json.loads(apiResponse.read())
    authorDownloadCount = 0

    for result in results:
        authorDownloadCount += result['downloads']

    return '{:,}'.format(int(authorDownloadCount))

def getAuthorUsernameAndAvatar(name):
    apiCall = performApiCall()

    try:
        url = API_URL + '/user/' + name.lower()
        apiResponse = apiCall.open(url)
    except HTTPError as e:
        if e.code == 404:
            return '404: ' + name, '404'

    if apiResponse:
        results = json.loads(apiResponse.read())
        return html.unescape(results['username']).strip(), html.unescape(results['avatar_url']).strip()
    else:
        return '404: ' + project, '404'

def getTitleAndSlug(project):
    apiResponse = getProject(project)

    if apiResponse:
        return html.unescape(apiResponse['name']).strip(), html.unescape(apiResponse['slug']).strip()
    else:
        return '404: ' + project, '404'
