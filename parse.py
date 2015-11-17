#!/usr/bin/env python
# coding: utf-8

import requests
import smtplib


class AvitoParser(object):

    def __init__(self, url):

        self.url = url


    def paginator(self):
        #Функция определяет количество страниц
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
            cars += ['http://avito.ru%s' % line.split('"')[5] for line in currentpage if '<div class=\"description\">' in line]
        return cars

    def cars_by_year(self):
        #Вернет словарь вида key(Год): value(Ссылка)
        cars_data = {}
        for value in self.get_cars():
            key = value.split('_')[-2]
            if key not in cars_data:
                cars_data[key] = [value]
            cars_data[key] += [value]

        return cars_data

    def get_price(self, url):
        #Получаем стоимость автомобиля по конкретной ссылке
        req = requests.get(url).text.split('\n')
        for line in req:
            if 'price:' in line:
                return line.split(' ')[-1].rstrip(',')

    def get_image(self, url):
        req = requests.get(url).text.split('\n')
        for line in req:
            if '<img src=\"//' in line:
                return 'http:' + line.split('\"')[7]

    def average_price(self):
        price = [self.get_price(x) for x in self.get_cars()]
        total = 0
        for value in price:
            total += int(value)
        return total // len(price)

    def date(self, url):
        req = requests.get(url).text.split('\n')
        for line in req:
            if u'Размещено' in line:
                return line

    def mileage(self, url):
        req = requests.get(url).text.split('\n')
        for line in req:
            if u'Пробег' in line:
                return line.split('\"')[-2].split(';')[-1].strip()

    def result(self):
        """

        :return: словарь {ссылка на машину: [фото, цена, пробег, год, дата размещения]}
        """
        result = {}
        for value in self.get_cars():
            result[value] = [self.get_image(value), self.get_price(value), self.mileage(value),
                             value.split('_')[-2], self.date(value)]

        return result


#Отправляем письмо на to@

def mail(message):

    smtp_server = 'smtp.yandex.ru'
    smtp_port = 465
    smtp_pasword = 'P@ssw0rd'

    uid = 'alx9110@yandex.ru'
    sender = 'mailer-daemon'
    subject = 'avparse request'
    to = 'alx9110@yandex.ru'

    mailer = smtplib.SMTP_SSL(smtp_server, smtp_port)
    mailer.login(uid, smtp_pasword)
    msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/html; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (sender, to, subject)
    msg += message
    mailer.sendmail(uid, to, msg)
