#!/usr/bin/env python
# coding: utf-8

import requests


def status_code(url):

    req = requests.get(url)

    return req.status_code


def pager(url):

    pages = []
    for i in range(1, 10):
        current = ('%s?p=%s' % (url, i))
        if status_code(current) == 200:
            pages.append(current)

    return pages


def get_cars(url):

    cars = []
    for page in pager(url):
        currentpage = requests.get(page).text.split('\n')
        for line in currentpage:
            if '<div class=\"description\">' in line:
                cars.append('http://avito.ru%s' % line.split('"')[5])

        return cars

url = 'https://www.avito.ru/ryazan/avtomobili/chevrolet/lacetti/hetchbek'
cars = get_cars(url)

d = {}
for key in cars:
    year = key.split('_')[2]
    if year not in d:
        d[year] = [key]
    d[year] += [key]

print len(d['2008'])
