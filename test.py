#!/usr/bin/env python
# coding: utf-8
from parse import AvitoParser


url = 'https://www.avito.ru/kasimov/avtomobili/vaz_lada'
query = AvitoParser(url)
res = query.result()
