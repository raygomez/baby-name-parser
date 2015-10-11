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


def add_name_to_list(list_of_names, name, rank, i):
    if name not in list_of_names:
        item = {'name': name, 'rank': [''] * size}
        list_of_names[name] = item
    list_of_names[name]['rank'][i] = rank


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

            add_name_to_list(males, results[1], rank, index)
            add_name_to_list(females, results[2], rank, index)

def write_names(filename, list_of_names):
    with open(filename, 'w') as f:
        f.write("{},{}\n".format('Name', ','.join(years)))
        for name in sorted(list_of_names.iteritems()):
            f.write('{},{}\n'.format(name[1]['name'], ','.join(name[1]['rank'])))

write_names('male.csv', males)
write_names('female.csv', females)
