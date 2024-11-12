from flask import Flask, render_template
from flask import render_template
from flask import request
from flask import send_file
from os import getenv
import re
from PIL import ImageFont

import ModrinthApi

api = Flask(__name__, static_folder='website', static_url_path='')

ENV = getenv('ENV')

CACHE_AGE = 10800

if ENV and ENV != "prod":
    api.debug = True
    CACHE_AGE = 0

@api.route('/')
def website():
    return send_file('website/index.html')

@api.route('/<project>.svg')
@api.route('/<style>_<project>.svg')
@api.route('/<style>_<project>_<suffix>.svg')
@api.route('/<style>_<project>_<prefix>_<suffix>.svg')
def downloads(project, style='full', suffix=None, prefix=None):
    downloads = ModrinthApi.getDownloadsProject(project)
    downloadsText = formatDownloads(downloads, style, prefix, suffix)
    args = request.args.copy()
    args['logo'] = True

    return createBadge('', downloadsText, False, args)

@api.route('/versions/<project>.svg')
@api.route('/versions/<project>_<style>.svg')
@api.route('/versions/<text>_<project>_<style>.svg')
def supported_versions(project, style='all', text='Available for'):
    versions = ModrinthApi.getVersions(project)
    versionsText = versions[0] if style == 'latest' else ' | '.join(str(version) for version in versions)

    return createBadge(text, versionsText, True, request.args)

@api.route('/author/<name>.svg')
@api.route('/author/<style>_<name>.svg')
@api.route('/author/<style>_<name>_<suffix>.svg')
@api.route('/author/<style>_<name>_<prefix>_<suffix>.svg')
def author(name, style='full', suffix=None, prefix=None):
    downloads = ModrinthApi.getDownloadsAuthor(name)
    downloadsText = formatDownloads(downloads, style, prefix, suffix)
    args = request.args.copy()
    args['logo'] = True

    return createBadge('', downloadsText, False, args)

@api.after_request
def addHeader(response):
    response.cache_control.max_age = CACHE_AGE
    response.direct_passthrough = False

    return response

def createBadge(leftText, rightText, invertColors, requestArgs):
    template = 'shield.svg'
    horizPadding = 6
    leftColor, rightColor = getColors(invertColors)
    logo = hasLogo(requestArgs)
    leftMargin = 4
    logoWidth = 0

    if logo == True:
        logoWidth = 18

    totalLogoWidth = logoWidth + leftMargin
    rightTextWidth = getLength(rightText)
    textWidth = getLength(leftText)
    badgeStyle = getBadgeStyle(requestArgs)
    leftWidth = textWidth + 2 * horizPadding + logoWidth
    rightWidth = rightTextWidth + 2 * horizPadding

    if logo == False:
        leftMargin = -5

    offsetLeft = 10 * (leftMargin + 0.5 * leftWidth + horizPadding)
    versionsMargin = (textWidth - 1) + totalLogoWidth + horizPadding
    offsetRight = 10 * (versionsMargin + 0.5 * rightWidth) + 30

    return renderBadgeTemplate(template, rightText=rightText, leftText=leftText,
            widthLeft=leftWidth, widthRight=rightWidth,
            totalWidth=leftWidth + rightWidth, offsetLeft=offsetLeft,
            leftTextWidth=textWidth * 10, rightTextWidth=rightTextWidth * 10,
            offsetRight=offsetRight, leftColor=leftColor, rightColor=rightColor,
            badgeStyle=badgeStyle, logo=logo), 200, {'Content-Type': 'image/svg+xml'}

def renderBadgeTemplate(template, **kwargs):
    renderedTemplate = render_template(template, **kwargs)
    renderedTemplate = re.sub(r">\s+<", "><", renderedTemplate)
    renderedTemplate = renderedTemplate.strip()

    return renderedTemplate

def getBadgeStyle(args):
    badgeStyle = 'rounded'

    if request.args.get('badge_style') == 'flat':
        badgeStyle = 'flat'

    return badgeStyle

def hasLogo(args):
    return 'logo' in args

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

def getLength(text):
    imageFont = ImageFont.truetype(getenv('FONT'), 11)

    length = round(imageFont.getlength(text))
    return length + 1 if length % 2 == 0 else length

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
