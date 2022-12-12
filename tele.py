import os
import telebot

API_KEY = '5697884156:AAEn9rrsQLQGQ5Kr0p-L65lIbi8IYE8vgWY'

bot = telebot.Telebot(API_KEY)

@bot.message_handler(commands=['start'])
 def start(message):
    bot.replay_to(message, "Hello sir, How can i help you...?")
    
    bot.polling()

