import requests
import time
from datetime import datetime
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = '5245409735:AAH4IX_xxue3-lB1YTUEH1bxz1TqEFl9bFs'
stream = ""
bot = telebot.TeleBot(TELEGRAM_TOKEN)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def test_send_message():
        text = 'CI Test Message'
        ret_msg = bot.send_message(CHAT_ID, text)
        assert ret_msg.message_id

if current_time=='22:38:00':
    test_send_message()


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
      for quote in quotes:
            stream = quote
      while True:
            bot.send_message(message.chat.id, stream)
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
