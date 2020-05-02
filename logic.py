#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def _load_data():
    with open('data_file.json', 'r') as file:
        data = json.load(file)
    return data


def _buy(arg):
    if arg == 'USD':
        return 'dollar_buy'
    elif arg == 'EUR':
        return 'euro_bay'
    elif arg == 'RUB':
        return 'rubl_by'


def _sell(arg):
    if arg == 'USD':
        return 'dollar_sell'
    elif arg == 'EUR':
        return 'euro_sell'
    elif arg == 'RUB':
        return 'rubl_sell'


def minimum_buy(arg):
    data = _load_data()
    money = _buy(arg)
    index = 0
    exch = None
    for inx, price in enumerate(data):
        if inx == 0:
            exch = price[money]
        if price[money] < exch:
            exch = price[money]
            index = inx
    return data[index]['name'], exch, data[index]['website']


def maximum_sell(arg):
    data = _load_data()
    money = _sell(arg)
    index = 0
    exch = None
    for inx, price in enumerate(data):
        if inx == 0:
            exch = price[money]
        if price[money] > exch:
            exch = price[money]
            index = inx
    return data[index]['name'], exch, data[index]['website']
