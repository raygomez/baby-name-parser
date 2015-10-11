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

soup = BeautifulSoup(open('babynames/baby1990.html'), 'lxml')
print(soup.h3.get_text())
table = soup.find_all('table')[1]
for tr in table.find_all('tr'):
    if tr.has_attr('align') and tr['align'] == 'right':
        td = tr.find_all('td')
        print(td[0].string,td[1].string,td[2].string)
