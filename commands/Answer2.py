import telebot

from __init_bot__ import bot


def Answer2(call: telebot.types.CallbackQuery):
    text = 'Теперь давай определимся с типом сайта:'
    buttons = telebot.util.quick_markup(
        {
            'Лендинг': {'callback_data': 'Answer2_1'},
            'Корпоративный сайт': {'callback_data': 'Answer2_2'},
            'Интернет-магазин': {'callback_data': 'Answer2_3'},
            'Портфолио': {'callback_data': 'Answer2_4'},
            'Блог': {'callback_data': 'Answer2_5'}
        }
    )
    bot.send_message(call.message.chat.id, text, reply_markup=buttons)