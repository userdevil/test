import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

TELEGRAM_TOKEN = '5159256749:AAGXCe1j3yxC-x-i3yBKwznj_-bOIk7JyMw'
msg = ""
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = message
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

if msg == "hi":
    @bot.message_handler(func=lambda message: True)
    def echo_message(message):
        r = "hello" 
        bot.reply_to(message, r.text)

bot.infinity_polling()
