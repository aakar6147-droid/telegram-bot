import os
import telebot
from openai import OpenAI

TELEGRAM_TOKEN = import telebot
import openai

TELEGRAM_BOT_TOKEN = "8920441173:AAEBcEzFpfFySbW9hfEmbuFX_5J4QLZjQu8"
openai.api_key = "sk-proj-FwuUQUgRM4alTlTZuAUwVbrPZv1AGxxjxKCY4c7H456jFueOHSLn8_c-U9CyMYtF4rJDYO-EeT3BlbkFJixMhWM6XbYcqKYwo1i4wHcssHugspHCZsSVfqgxysyumHcsz0v43mHDTdsQ4IsUop12sDg0AA"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سڵاو! من بۆتی چاتگپت م. چۆن دەتوانم یارمەتیت بدەم؟")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        client = openai.OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message.text}
            ]
        )
        reply = response.choices[0].message.content
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"هەڵەیەک ڕوویدا: {e}")

print("Bot is running...")
bot.infinity_polling()

OPENAI_API_KEY = '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'

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "تۆ یاریدەدەرێکی زیرەکی، بە زمانی کوردی وەڵامی بەکارهێنەران بدەرەوە."},
                {"role": "user", "content": user_text}
            ]
        )
        ai_reply = response.choices[0].message.content
        bot.reply_to(message, ai_reply)
    except Exception as e:
        bot.reply_to(message, "بەداخەوە، کێشەیەک ڕوویدا لە وەڵامدانەوەی AI.")

print("Bot is running...")
bot.infinity_polling()
