import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import token
from logic import *

bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: True)
def handle_message(message, сommands=['Коля']):
    print(message.text)
    bot.send_message(message.chat.id, input())
    global i
    i=message.chat.id
    f = open('xyzz.txt','w')  
    f.write(str(i))  
    f.close()  

bot.infinity_polling(none_stop=True)