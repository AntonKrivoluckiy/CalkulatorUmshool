import telebot

from __init_bot__ import bot


def Answer3(call):
    text = 'Сколько страниц будет у сайта?'
    buttons = telebot.util.quick_markup(
        {
            'До 3-х страниц': {'callback_data': 'Answer3_1'},
            '3-5 страниц': {'callback_data': 'Answer3_2'},
            '5-10 страниц': {'callback_data': 'Answer3_3'},
            '10+ страниц': {'callback_data': 'Answer3_4'}
        }
    )
    bot.send_message(call.message.chat.id, text, reply_markup=buttons)