from __future__ import print_function
from bs4 import BeautifulSoup

__author__ = 'raygomez'

RESOURCES = 'babynames'

class Name(object):
    def __init__(self):
        self.name = ''
        self.gender = ''
        self.years = []
        self.rank = []


from os import listdir
from os.path import isfile, join

files = [join(RESOURCES,f) for f in listdir(RESOURCES) if isfile(join(RESOURCES,f))]
size = len(files)
males = {}
females = {}
years = []

for index, f in enumerate(files):

    soup = BeautifulSoup(open(f), 'lxml')

    try:
        text = soup.h3.get_text()
        year = text[text.rindex(' ')+1:]
        years.append(year)
    except AttributeError:
        text = soup.h2.get_text()
        year = text[text.rindex(' ')+1:]
        years.append(year)

    table = soup.find_all('table')[1]
    for tr in table.find_all('tr'):
        if tr.has_attr('align') and tr['align'] == 'right':
            td = tr.find_all('td')
            rank = td[0].string

            name = td[1].string
            if name not in males:
                male = {'name': name, 'rank' : ['']*size}
                males[name] = male
            males[name]['rank'][index] = rank

            name = td[2].string
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