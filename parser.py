from __future__ import print_function
import re

from os import listdir
from os.path import isfile, join

__author__ = 'raygomez'

RESOURCES = 'babynames'

files = [join(RESOURCES,f) for f in listdir(RESOURCES) if isfile(join(RESOURCES,f))]
size = len(files)
males = {}
females = {}
years = []

name_regex = re.compile('<tr align="right"><td>(\w+)</td><td>(\w+)</td><td>(\w+)</td>')
header_regex = re.compile('<h3 align="center">Popularity in (\d+)</h3>')
other_header_regex = re.compile('<h2>Popularity in (\d+)</h2>')

for index, f in enumerate(files):
    with open(f) as f:
        text = f.read()
        try:
            year_result = re.findall(header_regex, text)
            years.append(year_result[0])
        except IndexError:
            year_result = re.findall(other_header_regex, text)
            years.append(year_result[0])

        for results in re.findall(name_regex, text):
            rank = results[0]

            name = results[1]
            if name not in males:
                male = {'name': name, 'rank' : ['']*size}
                males[name] = male
            males[name]['rank'][index] = rank

            name = results[2]
            if name not in females:
                female = {'name': name, 'rank' : ['']*size}
                females[name] = female
            females[name]['rank'][index] = rank

with open('male.csv', 'w') as f:
    f.write("{},{}\n".format('Name', ','.join(years)))
    for name in sorted(males.iteritems()):
        f.write('{},{}\n'.format(name[1]['name'], ','.join(name[1]['rank'])))

with open('female.csv', 'w') as f:
    f.write("{},{}\n".format('Name', ','.join(years)))
    for name in sorted(females.iteritems()):
        f.write('{},{}\n'.format(name[1]['name'], ','.join(name[1]['rank'])))