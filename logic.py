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


def _exchenge(arg_1, arg_2):
    data = _load_data()
    index_best = 0
    index_loose = 0
    exch_best = None
    exch_loose = None
    for inx, price in enumerate(data):
        if arg_1 == 'buy':
            money = _buy(arg_2)
            if inx == 0:
                exch_best = price[money]
                exch_loose = price[money]
            if price[money] < exch_best:
                exch_best = price[money]
                index_best = inx
            if price[money] > exch_loose:
                exch_loose = price[money]
                index_loose = inx
        if arg_1 == 'sell':
            money = _sell(arg_2)
            if inx == 0:
                exch_best = price[money]
                exch_loose = price[money]
            if price[money] > exch_best:
                exch_best = price[money]
                index_best = inx
            if price[money] < exch_loose:
                exch_loose = price[money]
                index_loose = inx

    return index_best, exch_best, data, index_loose, exch_loose


def sell_buy(arg_1, arg_2):
    index_best, exch_best, data, index_loose, exch_loose = _exchenge(arg_1, arg_2)
    return data[index_best]['name'], exch_best, data[index_best]['website']


def calc(arg_1, arg_2, arg_3):
    index_best, exch_best, data, index_loose, exch_loose = _exchenge(arg_1, arg_3)
    if arg_3 == 'RUB':
        return data[index_best]['name'], (float(arg_2) * exch_best) / 100, \
               data[index_loose]['name'], (float(arg_2) * exch_loose) / 100
    else:
        return data[index_best]['name'], float(arg_2) * exch_best, \
               data[index_loose]['name'], float(arg_2) * exch_loose


def list_sell_buy(arg_1, arg_2):
    data = _load_data()
    if arg_1 == 'sell':
        sell = sorted([[i[_sell(arg_2)], i['name']] for i in data], reverse=True)
        sell = [str(i[0]) + ' ' + str(i[1]) + '\n' for i in sell]
        return ''.join(sell)
    if arg_1 == 'buy':
        buy = sorted([[i[_buy(arg_2)], i['name']] for i in data])
        buy = [str(i[0]) + ' ' + str(i[1]) + '\n' for i in buy]
        return ''.join(buy)


if __name__ == '__main__':
    arg_1 = 'buy'
    arg_2 = 'RUB'
    print(list_sell_buy(arg_1, arg_2))
