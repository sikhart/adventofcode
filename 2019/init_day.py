import sys
import os
from shutil import copyfile
import requests

day = sys.argv[1]

# Create folder if it does not exist
day_pad = day.zfill(2)
if (not os.path.isdir(day_pad)):
    os.mkdir(day_pad)

# Copy template if script does not exist
pyfile = day_pad+'/'+day_pad+'.py'
if (not os.path.exists(pyfile)):
    copyfile('template.py', pyfile)

# Fetch input if input file does not exist
inputfile = day_pad+'/input'
if (not os.path.exists(inputfile)):
    cookie = open("../aoc_cookie").read().rstrip()
    url = 'https://adventofcode.com/2019/day/'
    if day[0] == '0':
        url += day[1]
    else:
        url += day
    url += '/input'

    r = requests.get(url, cookies=dict({'session': cookie}))
    f = open(inputfile, 'w+')
    f.write(r.content)
    f.close()
