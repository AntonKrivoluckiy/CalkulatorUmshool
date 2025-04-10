import telebot

from __init_bot__ import bot
from commands.Answer1 import Answer1


@bot.message_handler(commands=['start'])
def hello(message: telebot.types.Message):
    text = (f'Привет, {message.chat.first_name}! Я помогу тебе рассчитать стоимость твоего '
            f'первого сайта. Ответь на несколько вопросов, и я дам '
            f'тебе примерный расчет.')
    bot.send_message(message.chat.id, text)
    Answer1(message)