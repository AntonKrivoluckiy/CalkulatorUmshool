import telebot

from __init_bot__ import bot


def Answer5(call):
    text = ('Какой уровень функциональности тебе нужен?: \n\n'
            'Стандартный - просто страницы + форма обратной связи.\n'
            'Дополнительные функции - блог, авторизация, интеграция с CRM.\n'
            'Продвинутые - интернет-магазин, сложные фильтры, чаты.')
    buttons = telebot.util.quick_markup(
        {
            'Стандартный': {'callback_data': 'Answer5_1'},
            'Дополнительные функции': {'callback_data': 'Answer5_2'},
            'Продвинутые': {'callback_data': 'Answer5_3'}
        }
    )
    bot.send_message(call.message.chat.id, text, reply_markup=buttons)