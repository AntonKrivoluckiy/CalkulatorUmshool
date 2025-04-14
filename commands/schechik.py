from __init_bot__ import bot
from commands.Answer1 import Answer1
from commands.Answer2 import Answer2
from commands.Answer3 import Answer3
from commands.Answer4 import Answer4
from commands.Answer5 import Answer5
from commands.Answer6 import Answer6
from commands.Answer7 import Answer7
from commands.create_buttons import user_button_states
from commands.prise import Preparing
from commands.register import user_summ, register


@bot.callback_query_handler(func=lambda call: True)
def schetchick(call):
    user_id = call.message.chat.id

    if user_id not in user_summ:
        register(user_id)

    #Answer1
    if call.data == 'Answer1_1':
        user_summ[user_id]['percent'] += 0
        Answer2(call)
    if call.data == 'Answer1_2':
        user_summ[user_id]['percent'] += 0.05
        Answer2(call)
    if call.data == 'Answer1_3':
        user_summ[user_id]['percent'] += 0.1
        Answer2(call)
    if call.data == 'Answer1_4':
        user_summ[user_id]['percent'] += 0.15
        Answer2(call)

    #Answer2
    if call.data == 'Answer2_1':
        user_summ[user_id]['summ'] += 5000
        Answer3(call)
    if call.data == 'Answer2_2':
        user_summ[user_id]['summ'] += 8000
        Answer3(call)
    if call.data == 'Answer2_3':
        user_summ[user_id]['summ'] += 12000
        Answer3(call)
    if call.data == 'Answer2_4':
        user_summ[user_id]['summ'] += 7000
        Answer3(call)
    if call.data == 'Answer2_5':
        user_summ[user_id]['summ'] += 9000
        Answer3(call)

    #Answer3
    if call.data == 'Answer3_1':
        user_summ[user_id]['summ'] += 2000
        Answer4(call)
    if call.data == 'Answer3_2':
        user_summ[user_id]['summ'] += 4000
        Answer4(call)
    if call.data == 'Answer3_3':
        user_summ[user_id]['summ'] += 6000
        Answer4(call)
    if call.data == 'Answer3_4':
        user_summ[user_id]['summ'] += 8000
        Answer4(call)

    #Answer4
    if call.data == 'Answer4_1':
        user_summ[user_id]['summ'] += 2000
        Answer5(call)
    if call.data == 'Answer4_2':
        user_summ[user_id]['summ'] += 5000
        Answer5(call)
    if call.data == 'Answer4_3':
        user_summ[user_id]['summ'] += 7000
        Answer5(call)

    #Answer5
    if call.data == 'Answer5_1':
        user_summ[user_id]['summ'] += 2000
        Answer6(call)
    if call.data == 'Answer5_2':
        user_summ[user_id]['summ'] += 5000
        Answer6(call)
    if call.data == 'Answer5_3':
        user_summ[user_id]['summ'] += 10000
        Answer6(call)

    #Answer6
    if call.data == 'Answer6_1':
        user_summ[user_id]['summ'] += 5000
        Answer7(call, user_id)
    if call.data == 'Answer6_2':
        user_summ[user_id]['summ'] += 3000
        Answer7(call, user_id)
    if call.data == 'Answer6_3':
        user_summ[user_id]['summ'] += 2000
        Answer7(call, user_id)

    #Answer7
    if call.data in ['SEO-оптимизация', 'Копирайтинг', 'Поддержка и обновления', 'Подключение аналитики']:

        button_number = call.data
        if button_number in user_button_states[user_id]:
            user_button_states[user_id][button_number] = not user_button_states[user_id][button_number]
        else:
            user_button_states[user_id][button_number] = True

        if call.data == 'SEO-оптимизация':
            user_summ[user_id]['m_question'] += '1'
            if user_button_states[user_id]['SEO-оптимизация']:
                user_summ[user_id]['summ'] += 3000
            if not user_button_states[user_id]['SEO-оптимизация']:
                user_summ[user_id]['summ'] -= 3000
            Answer7(call, user_id)

        if call.data == 'Копирайтинг':
            user_summ[user_id]['m_question'] += '1'
            if user_button_states[user_id]['Копирайтинг']:
                user_summ[user_id]['summ'] += 2000
            if not user_button_states[user_id]['Копирайтинг']:
                user_summ[user_id]['summ'] -= 2000
            Answer7(call, user_id)

        if call.data == 'Поддержка и обновления':
            user_summ[user_id]['m_question'] += '1'
            if user_button_states[user_id]['Поддержка и обновления']:
                user_summ[user_id]['summ'] += 2500
            if not user_button_states[user_id]['Поддержка и обновления']:
                user_summ[user_id]['summ'] -= 2500
            Answer7(call, user_id)

        if call.data == 'Подключение аналитики':
            user_summ[user_id]['m_question'] += '1'
            if user_button_states[user_id]['Подключение аналитики']:
                user_summ[user_id]['summ'] += 1500
            if not user_button_states[user_id]['Подключение аналитики']:
                user_summ[user_id]['summ'] -= 1500
            Answer7(call, user_id)

    if call.data == 'Пропустить':
        Preparing(call)

    #Preparing
    if call.data == 'Restart':
        bot.send_message(call.message.chat.id, 'Хорошо, давай пересчитаем еще раз:')
        Answer1(call.message)
    if call.data == 'la grand final':
        bot.send_message(call.message.chat.id, 'Отлично! Переходи по ссылке и создавай свои сайты быстро, просто и удобно\n\nhttps://t.me/vebdumschol25')