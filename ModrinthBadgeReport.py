import argparse
import fnmatch
import gzip
import os
import re

from dotenv import load_dotenv

load_dotenv()

import ModrinthApi

def validateOut(directory):
    return validateDirectory(directory, True)

def validateDirectory(directory, createDirectory=False):
    if not os.path.isdir(directory):
        if createDirectory:
            os.makedirs(directory)
        else:
            raise argparse.ArgumentTypeError(f"{d} is not a directory")

    if not directory.endswith('/'):
        directory += '/'

    return directory

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--directory', type=validateDirectory, required=True, help='Input directory. Must contain access.log, access-log-1.gz, etc.')
parser.add_argument('-od', '--out_directory', type=validateOut, default='out/', help='Output directory. Will store csv reports here.')
parser.add_argument('-pr', '--project_report', type=str, default='projects.csv', help='Name of project report csv file.')
parser.add_argument('-ar', '--author_report', type=str, default='authors.csv', help='Name of authors report csv file.')
args = parser.parse_args()

projectsCsv = open(args.out_directory + args.project_report, 'w')
authorsCsv = open(args.out_directory + args.author_report, 'w')
pattern = re.compile(r'GET /(.*?\.svg) ')
itemPattern = re.compile(r'(((full|short|small)_)|(versions/(.*?_(?=.*?_))?))?(?P<item>.*?)((_.*)|\.svg)')
projectMatch = []
resolveTitle = []
projects = []
authorMatch = []
resolveAuthor = []
authors = []

def parseFile(filename, gz=False):
    print('Analyzing ' + filename)

    if not gz:
        with open(args.directory + filename, 'r') as file:
            for line in file.read().split('\n'):
                parseLine(line)
    else:
        with gzip.open(args.directory + filename, 'rt') as file:
            for line in file:
                parseLine(line)

def parseLine(line):
    match = pattern.search(line)
    
    if match:
        matchString = match.group(1)

        if "author/" in matchString:
            authorMatch.append(matchString)
        else:
            projectMatch.append(matchString)

# Parse files in log directory
for filename in os.listdir(args.directory):
    if fnmatch.fnmatch(filename, 'access*'):
        if filename.endswith('.gz'):
            parseFile(filename, True)
        else:
            parseFile(filename)

# Generate projects csv
for item in set(projectMatch):
    resolveTitle.append(itemPattern.search(item).group('item'))

for project in set(resolveTitle):
    title, slug = ModrinthApi.getTitleAndSlug(project)
    projects.append(title + ', ' + slug)

projectsCsv.write('title, slug\n')

for projectInfo in set(projects):
    projectsCsv.write(projectInfo + '\n')

projectsCsv.close()

# Generate authors csv
for itemString in set(authorMatch):
    item = itemString.split('/', 1)[-1]
    results = itemPattern.search(item).group('item')
    resolveAuthor.append(results)

for author in set(resolveAuthor):
    username, avatar = ModrinthApi.getAuthorUsernameAndAvatar(author)
    authors.append(username + ', ' + avatar)

authorsCsv.write('username, avatar\n')

for authorInfo in set(authors):
    authorsCsv.write(authorInfo + '\n')

projectsCsv.close()
