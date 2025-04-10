import telebot

from __init_bot__ import bot


def Answer6(call):
    text = 'За какой срок сайт должен быть готов?'
    buttons = telebot.util.quick_markup(
        {
            '2-4 недели': {'callback_data': 'Answer6_1'},
            '1 месяц': {'callback_data': 'Answer6_2'},
            '2+ месяца': {'callback_data': 'Answer6_3'}
        }
    )
    bot.send_message(call.message.chat.id, text, reply_markup=buttons)