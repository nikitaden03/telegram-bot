# coding=<UTF-8>
# !usr/bin/env python3


from pprint import pprint
import telebot
from telebot import apihelper
from telebot import types
from subject import *

apihelper.proxy = {'https': 'socks5://207.97.174.134:1080'}
bot = telebot.TeleBot('836764194:AAHd4hDv6wvLNXrLqQcQbnVq0Kv1HVvIl1g')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """/start and /help."""
    bot.send_message(message.chat.id, '''
    Привет, я Telegram-bot!\nЗдесь ты можешь поделиться готовой домашкой или получить ее!
    \n/giveHW - Поделится домашкой\n/getHW - Получить домашку''')


@bot.message_handler(commands=['getHW'])
def get_home_work(messgae):
    """Начало обработки функции getHW"""

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(bio, geo, art, his, ikb, lit, math, phys, chm, com)
    bot.send_message(messgae.chat.id, 'Отлично, ты хочешь получить готовое решение домашки!\nВыбери предмет:\n\n',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.send_message(call.message.chat.id, call.data)


bot.polling()
