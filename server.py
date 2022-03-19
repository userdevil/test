import telebot

bot = telebot.TeleBot("5159256749:AAGXCe1j3yxC-x-i3yBKwznj_-bOIk7JyMw")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
