import telebot

from __init_bot__ import bot
from commands.register import register


def Answer1(message):
    text1 = ('Сколько у тебя опыта в веб-дизайне?')

    AnswerButtons = telebot.util.quick_markup(
        {
            'До 6 месяцев': {'callback_data': 'Answer1_1'},
            '6 месяцев-1 год': {'callback_data': 'Answer1_2'},
            '1-3 года': {'callback_data': 'Answer1_3'},
            '3+ лет': {'callback_data': 'Answer1_4'}
        }
    )
    bot.send_message(message.chat.id, text1, reply_markup=AnswerButtons)
    register(message.chat.id)