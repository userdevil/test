import requests
import time
from telegram import*
from datetime import datetime
from telegram.ext import*

bot = Bot("5245409735:AAH4IX_xxue3-lB1YTUEH1bxz1TqEFl9bFs")
print(bot.get_me())

# list of quotes
quotes = [
    'https://www.youtube.com/watch?v=8FAUEv_E_xQ',
    'https://www.youtube.com/watch?v=jmwU1iAC-IE',
    'https://www.youtube.com/watch?v=ATElufr0OiE',
    'https://www.youtube.com/watch?v=tYSrY4iPX6w',
    'https://www.youtube.com/watch?v=w7Fjxf62t8E'
]
updater = Updater("5245409735:AAH4IX_xxue3-lB1YTUEH1bxz1TqEFl9bFs")
updater = Updater("5245409735:AAH4IX_xxue3-lB1YTUEH1bxz1TqEFl9bFs",use_context = True)
dispatcher = updater.dispatcher
CHAT_ID = update.effective_chat.id

# loop through the quotes
for quote in quotes:
    url = 'https://api.telegram.org/bot5245409735:AAH4IX_xxue3-lB1YTUEH1bxz1TqEFl9bFs/sendMessage?chat_id="{}"&text="{}"'.format(CHAT_ID,quote)
    requests.get(url)
    # sends new quotes every 20seconds
    time.sleep(30)
