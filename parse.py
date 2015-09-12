#!/usr/bin/env python
# coding: utf-8

import requests
import mailerdaemon


class AvitoParser(object):

    def __init__(self, url):

        self.url = url
        self.total = len(self.get_cars()) #Кол-во найденных машин


    def paginator(self):
        pages = []
        for i in range(1, 10):
            current = ('%s?p=%s' % (self.url, i))
            req = requests.get(current)
            if req.status_code == 200:
                pages.append(current)

        return pages # return array of pagelinks

    def get_cars(self):
        #Вернет список ссылок
        cars = []
        for page in self.paginator():
            currentpage = requests.get(page).text.split('\n')
            for line in currentpage:
                if '<div class=\"description\">' in line:
                    cars.append('http://avito.ru%s' % line.split('"')[5])

        return cars

    def cars_of_year(self):
        #Вернет словарь вида key(Год): value(Ссылка)
        cars_data = {}
        for key in self.get_cars():
            year = key.split('_')[2]
            if year not in cars_data:
                cars_data[year] = [key]
            cars_data[year] += [key]

        return cars_data


url = 'https://www.avito.ru/ryazan/avtomobili/chevrolet/lacetti/hetchbek'
cars = AvitoParser(url)
msg = ''

mailerdaemon.mail(msg)