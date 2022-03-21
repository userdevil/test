import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import pytube

TELEGRAM_TOKEN = '5159256749:AAGXCe1j3yxC-x-i3yBKwznj_-bOIk7JyMw'
stream = ""
bot = telebot.TeleBot(TELEGRAM_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    
    try:
        yt = pytube.YouTube(message)
        stream = yt.streams.filter(file_extension='mp4').first().url
        tit = yt.title
   except:
        print("An exception occurred")
        bot.reply_to(message, stream.text)

bot.infinity_polling()
