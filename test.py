#!/usr/bin/env python
# coding: utf-8


from parse import AvitoParser


url = 'https://www.avito.ru/ryazanskaya_oblast/avtomobili/chevrolet/lacetti'

query = AvitoParser(url)
print query.paginator()
