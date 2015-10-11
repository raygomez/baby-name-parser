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

files = [f for f in listdir(RESOURCES) if isfile(join(RESOURCES,f))]
size = len(files)
males = {}
females = {}


for index, f in enumerate(files):

    #print(index, f)
    soup = BeautifulSoup(open(join(RESOURCES,f)), 'lxml')

    try:
        pass
        #print(soup.h3.get_text())
    except AttributeError:
        pass
        #print(soup.h2.get_text())

    table = soup.find_all('table')[1]
    for tr in table.find_all('tr'):
        if tr.has_attr('align') and tr['align'] == 'right':
            td = tr.find_all('td')
            rank = td[0].string

            name = td[1].string
            if name not in males:
                male = {'name': name, 'rank' : [None]*size}
                males[name] = male
            males[name]['rank'][index] = rank

            name = td[2].string
            if name not in females:
                female = {'name': name, 'rank' : [None]*size}
                females[name] = female
            females[name]['rank'][index] = rank

# with open('male.csv', 'w') as f:
#     for name in sorted(males.iteritems()):
#         f.write('{},{}'.format(name['name'], ','.join(name['rank'])))
#

print(females)