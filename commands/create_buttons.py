from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from commands.register import user_summ, user_button_states


def create_buttons_for_Answer7(user_id):
    buttons = InlineKeyboardMarkup()

    for i in ['SEO-оптимизация', 'Копирайтинг', 'Поддержка и обновления', 'Подключение аналитики']:
        text = i
        if user_button_states[user_id].get(i, False):
            text = '✅ ' + text
        else:
            text = i
        buttons.add(InlineKeyboardButton(text, callback_data=f'{i}'))

    if user_summ[user_id]['m_question']:
        text = 'Дальше'
    else:
        text = 'Пропустить'
    buttons.add(InlineKeyboardButton(text, callback_data=f'{text}'))

    return buttons
