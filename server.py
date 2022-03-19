import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

TELEGRAM_TOKEN = '5159256749:AAGXCe1j3yxC-x-i3yBKwznj_-bOIk7JyMw'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MP4", callback_data="cb_yes"),
                               InlineKeyboardButton("MP3", callback_data="cb_no"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is MP4")
        resp = "https://loader.to/api/button/?url=","message"
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is MP3")
        
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, resp)

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Select formet", reply_markup=gen_markup())

bot.infinity_polling()
