import telebot

from __init_bot__ import bot
from commands.register import user_summ


def Preparing(call):
    user_id = call.message.chat.id

    final_summ = user_summ[user_id]['summ'] + (user_summ[user_id]['summ'] * user_summ[user_id]['percent'])

    bot.send_message(call.message.chat.id, 'Давай посчитаем...')
    bot.send_message(call.message.chat.id, '⏳ Обрабатываю данные...')
    bot.send_message(call.message.chat.id, f'Предварительная стоимость разработки сайта: {final_summ}')

    buttons = telebot.util.quick_markup(
        {
            'Пересчитать': {'callback_data': 'Restart'},
            'Начать разрабатывать веб-сайты': {'callback_data': 'la grand final'}
        }
    )
    bot.send_message(call.message.chat.id,
                     'Это предварительная оценка. Финальная цена может зависеть от дополнительных деталей проекта и ваших знаний и умений',
                     reply_markup=buttons)