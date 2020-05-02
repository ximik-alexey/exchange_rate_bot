#!/usr/bin/python 3.8
# -*- coding: utf-8 -*-

import telebot
import config
import logic




bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    help_text = 'Для просмотра выгодной продажи валюты введите:\nsell USD или sell RUB или sell EUR\n\n' \
                'Для просмотра выгодной покупки валюты введите:\nbuy USD или buy RUB или buy EUR\n\n' \
                'Для просмотра курса одной валюты во всех банках в порядке выгодности введите:\n' \
                'list sell USD или list buy EUR\n\n' \
                'Для конвертации волюты введите:\nsell 120 USD или buy 1350 RUB\n\n' \
                'Для просмотра команд введите - help \n\n'
    bot.reply_to(message, help_text)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        if len(message.text.split()) == 2:
            act, money = message.text.split()
            act, money = act.lower(), money.upper()
            if (act == 'sell' or act == 'buy') and (money == 'USD' or money == 'EUR' or money == 'RUB'):
                bank, kurs, link = logic.sell_buy(act, money)
                bot.send_message(message.from_user.id, f' {money}: {kurs} в банке {bank}, сайт {link}')
            else:
                send_welcome(message)

        elif len(message.text.split()) == 3:
            arg_1, arg_2, arg_3 = message.text.split()
            arg_1, arg_3 = arg_1.lower(), arg_3.upper()
            if arg_2.isdigit():
                pass
            else:
                arg_2 = arg_2.lower()
            if (arg_1 == 'sell') \
                    and arg_2.isdigit() \
                    and (arg_3 == 'USD' or arg_3 == 'EUR' or arg_3 == 'RUB'):
                best_name, best_exchange, loose_name, loose_exchange = logic.calc(arg_1, arg_2, arg_3)
                bot.send_message(message.from_user.id, f'лучший курс: {round(best_exchange, 2)} BYN\n'
                                                       f'в банке {best_name}\n'
                                                       f'худший курс: {round(loose_exchange, 2)} BYN\n'
                                                       f'в банке {loose_name}')
            elif (arg_1 == 'buy') \
                    and arg_2.isdigit() \
                    and (arg_3 == 'USD' or arg_3 == 'EUR' or arg_3 == 'RUB'):
                best_name, best_exchange, loose_name, loose_exchange = logic.calc(arg_1, arg_2, arg_3)
                bot.send_message(message.from_user.id, f'лучший курс: {round(best_exchange, 2)} BYN\n'
                                                       f'в банке {best_name}\n'
                                                       f'худший курс: {round(loose_exchange, 2)} BYN\n'
                                                       f'в банке {loose_name}')

            elif arg_1 == 'list' \
                    and (arg_2 == 'sell' or arg_2 == 'buy') \
                    and (arg_3 == 'USD' or arg_3 == 'EUR' or arg_3 == 'RUB'):
                text = logic.list_sell_buy(arg_2, arg_3)
                bot.send_message(message.from_user.id, text)
            else:
                send_welcome(message)
        else:
            send_welcome(message)
    except (ValueError, UnboundLocalError, TypeError):
        send_welcome(message)


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=1)

# EOF
