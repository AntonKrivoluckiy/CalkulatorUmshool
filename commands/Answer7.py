from __init_bot__ import bot
from commands.create_buttons import create_buttons_for_Answer7
from commands.register import user_summ


def Answer7(call, user_id):
    text = 'Выбери дополнительные услуги (можно несколько):'
    if user_summ[user_id]['m_question'] == '':
        buttons = create_buttons_for_Answer7(user_id)
        bot.send_message(call.message.chat.id, text, reply_markup=buttons)
    else:
        buttons_ = create_buttons_for_Answer7(user_id)
        bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=buttons_
        )