import telebot

from __init_bot__ import bot


def Answer4(call):
    text = ('Какой уровень дизайна ты хочешь видеть на своем сайте? \n\n'
            'Простой - стандартные блоки, минимум анимации. \n'
            'Средний - кастомные элементы, базовые анимации. \n'
            'Сложный - уникальный UI, сложные анимации.')
    buttons = telebot.util.quick_markup(
        {
            'Простой': {'callback_data': 'Answer4_1'},
            'Средний': {'callback_data': 'Answer4_2'},
            'Сложный': {'callback_data': 'Answer4_3'}
        }
    )
    bot.send_message(call.message.chat.id, text, reply_markup=buttons)