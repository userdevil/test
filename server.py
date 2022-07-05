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
      def test_send_message():
        text = 'CI Test Message'
        ret_msg = bot.send_message(CHAT_ID, text)
        assert ret_msg.message_id

      if current_time=='22:43:00':
          test_send_message()
 
# list of quotes
quotes = [
    '/led_on',
    '/led_off',
]
bot.infinity_polling()
