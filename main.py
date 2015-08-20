#!/usr/bin/env python
# coding: utf-8

import requests


def status_code(url):

    req = requests.get(url)

    return req.status_code


def paginator(url):

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


def cars_of_year(links):

    cars_data = {}
    for key in links:
        year = key.split('_')[2]
        if year not in cars_data:
            cars_data[year] = [key]
        cars_data[year] += [key]

    return cars_data

def get_price(links):

    for x in requests.get(links):
        if 'itemprop=\"price\"' in x:
            print x.strip('\n')