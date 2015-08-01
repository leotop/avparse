#!/usr/bin/env python
# coding: utf-8
__author__ = 'midiblack'

import requests


url = 'https://www.avito.ru/ryazan/avtomobili/chevrolet/lacetti/hetchbek'

class Cars(object):

    def __init__(self, url):

        self.url = url+'?p='

    def page_Counter(self):

        temp = requests.head(url+'?p=1')
        return str(temp)


c = Cars(url)
if '200' in c.page_Counter():
    print 'Wow yeees!'
else:
    print 'Nooo'