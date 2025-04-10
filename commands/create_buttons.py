from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

user_button_states = {}

def create_buttons_for_Answer7(user_id):
    buttons = InlineKeyboardMarkup()

    if user_id not in user_button_states:
        user_button_states[user_id] = {}

    for i in ['SEO-оптимизация', 'Копирайтинг', 'Поддержка и обновления', 'Подключение аналитики', 'Пропустить']:
        text = i
        if user_button_states[user_id].get(i, False):
            text = '✅ ' + text
        else:
            text = i
        buttons.add(InlineKeyboardButton(text, callback_data=f'{i}'))
    return buttons
