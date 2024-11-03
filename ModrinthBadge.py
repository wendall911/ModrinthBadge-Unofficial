from flask import Flask, render_template
from flask import render_template
from flask import request
from flask import send_file
from os import getenv
from PIL import ImageFont

import ModrinthApi

api = Flask(__name__, static_folder='website', static_url_path='')

ENV = getenv('ENV')

CACHE_AGE = 10800

if ENV and ENV != "prod":
    api.debug = True
    CACHE_AGE = 0

FONT = ImageFont.truetype(getenv('FONT'), 15)

@api.route('/')
def website():
    return send_file('website/index.html')

@api.route('/<project>.svg')
@api.route('/<style>_<project>.svg')
@api.route('/<style>_<project>_<suffix>.svg')
@api.route('/<style>_<project>_<prefix>_<suffix>.svg')
def downloads(project, style='full', suffix=None, prefix=None):
    template = 'modrinthShield.svg'
    leftColor, rightColor = getColors()
    downloads = ModrinthApi.getDownloadsProject(project)
    replacement = formatDownloads(downloads, style, prefix, suffix)
    badgeStyle = getBadgeStyle(request.args)

    width = getValueWidth(replacement, 0.9)

    return createBadge(template, downloads=replacement, width=width,
            totalWidth=(30 + width), offset=(30.5 + width / 2),
            leftColor=leftColor, rightColor=rightColor,
            badgeStyle=badgeStyle), 200, {'Content-Type': 'image/svg+xml'}

@api.route('/versions/<project>.svg')
@api.route('/versions/<project>_<style>.svg')
@api.route('/versions/<text>_<project>_<style>.svg')
def supported_versions(project, style='all', text='Available for'):
    template = 'shield.svg'
    leftColor, rightColor = getColors(True)
    versions = ModrinthApi.getVersions(project)
    versions_text = versions[0] if style == 'latest' else ' | '.join(str(version) for version in versions)
    version_width = getValueWidth(versions_text, 0.82)
    text_width = FONT.getlength(text)
    badgeStyle = getBadgeStyle(request.args)

    return createBadge(template, versions=versions_text, text=text,
            widthText=text_width, widthVersions=version_width,
            totalWidth=(version_width + text_width), offsetText=text_width / 2,
            offsetVersions=version_width / 2, leftColor=leftColor, rightColor=rightColor,
            badgeStyle=badgeStyle), 200, {'Content-Type': 'image/svg+xml'}

@api.route('/author/<name>.svg')
@api.route('/author/<style>_<name>.svg')
@api.route('/author/<style>_<name>_<suffix>.svg')
@api.route('/author/<style>_<name>_<prefix>_<suffix>.svg')
def author(name, style='full', suffix=None, prefix=None):
    template = 'modrinthShield.svg'
    leftColor, rightColor = getColors()
    downloads = ModrinthApi.getDownloadsAuthor(name)
    replacement = formatDownloads(downloads, style, prefix, suffix)
    width = getValueWidth(replacement, 0.9)
    badgeStyle = getBadgeStyle(request.args)

    return createBadge(template, downloads=replacement, width=width,
            totalWidth=(30 + width), offset=(30.5 + width / 2),
            leftColor=leftColor, rightColor=rightColor,
            badgeStyle=badgeStyle), 200, {'Content-Type': 'image/svg+xml'}

@api.after_request
def addHeader(response):
    response.cache_control.max_age = CACHE_AGE
    response.add_etag()

    return response

def createBadge(template, **kwargs):
    return render_template(template, **kwargs)

def getBadgeStyle(args):
    badgeStyle = 'rounded'

    if request.args.get('badge_style') == 'flat':
        badgeStyle = 'flat'

    return badgeStyle

def formatDownloads(downloads, style, prefix, suffix):
    replacement = ''

    if style == 'short' and downloads != '404':
        parts = downloads.split(',')
        first = parts[0][0]
        padding = '0' * (len(parts[0]) - 1)
        post_fix = ('M+' if len(parts) > 2 else ('k+' if len(parts) > 1 else ''))
        replacement += first + padding + post_fix
    else:
        replacement += downloads

    if prefix:
        replacement = prefix + ' ' + replacement

    if suffix:
        replacement += ' ' + suffix

    return replacement.strip()

def getValueWidth(text, offset):
    return max(FONT.getlength(text) * offset, 50)

def getColors(invert=False): 
    green = '1BD96A'
    greenAlt = '14A24F'
    dark = '2D2D2D'

    if invert: 
        return dark, greenAlt
    else:
        return green, dark

if __name__ == '__main__':
    api.run()
