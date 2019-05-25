# coding=<UTF-8>
# !usr/bin/env python3

import telebot
from telebot import apihelper

bot = telebot.TeleBot('836764194:AAHd4hDv6wvLNXrLqQcQbnVq0Kv1HVvIl1g')
apihelper.proxy = {'https': 'socks5://110.49.101.58:1080'}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """/start and /help."""
    bot.reply_to(message, 'Howdy, how are you doing?')


bot.polling()


