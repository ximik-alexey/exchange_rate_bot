#!/usr/bin/python 3.8
# -*- coding: utf-8 -*-

# install
# pip3 install pyTelegramBotAPI

import telebot
import config
import logic




bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    help_text = 'Для просмотра выгодной продажи валюты введите:\nsell USD или sell RUB или sell EUR\n\nДля просмотра выгодной покупки валюты введите:\nbuy USD или buy RUB или buy EUR\n\nДля просмотра команд введите - help'
    bot.reply_to(message, help_text)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message)
    try:
        n_1, n_2 = message.text.split()
        act, money = n_1.lower(), n_2.upper()
        if (act == 'sell' or act == 'buy') and (money == 'USD' or money == 'EUR' or money == 'RUB'):
            if act == 'sell':
                kurs, bank, link = logic.maximum_sell(money)
                bot.send_message(message.from_user.id, f' {money}: {kurs} в банке {bank}, сайт {link}')
            elif act == 'buy':
                kurs, bank, link = logic.minimum_bay(money)
                bot.send_message(message.from_user.id, f' {money}: {kurs} в банке {bank}, сайт {link}')
        else:
            send_welcome(message)
    except (ValueError, UnboundLocalError):
        send_welcome(message)


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=1)