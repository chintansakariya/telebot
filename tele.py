import os
import telebot

API_KEY = os.environ('API_KEY')

bot = telebot.Telebot(API_KEY)

@bot.message_handler(commands=['start'])
 def start(message):
    bot.replay_to(message, "Hello sir, How can i help you...?")
    
    bot.polling()

