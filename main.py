import os
import telebot

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Fala! Eu sou o SwiftBuxx Bot e já tô online! 💛")

@bot.message_handler(func=lambda m: True)
def responder(message):
    bot.reply_to(message, f"Você disse: {message.text}")

print("Bot ligado!")
bot.infinity_polling()
