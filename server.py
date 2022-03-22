import requests
import time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = '5245409735:AAH4IX_xxue3-lB1YTUEH1bxz1TqEFl9bFs'
stream = "hi"
bot = telebot.TeleBot(TELEGRAM_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
      for quote in quotes:
            stream = quote
      while True:
            bot.send_message(message,stream)
            time.sleep(4)
 
# list of quotes
quotes = [
    'https://www.youtube.com/watch?v=8FAUEv_E_xQ',
    'https://www.youtube.com/watch?v=jmwU1iAC-IE',
    'https://www.youtube.com/watch?v=ATElufr0OiE',
    'https://www.youtube.com/watch?v=tYSrY4iPX6w',
    'https://www.youtube.com/watch?v=w7Fjxf62t8E'
]
bot.infinity_polling()
