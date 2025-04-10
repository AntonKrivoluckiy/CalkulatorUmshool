user_summ = {}

def register(user_id):
    if user_id not in user_summ:
        user_summ[user_id] = {}
    user_summ[user_id]['summ'] = 0
    user_summ[user_id]['percent'] = 0
    user_summ[user_id]['m_question'] = ''
