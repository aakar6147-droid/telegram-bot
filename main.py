import os
import telebot
from openai import OpenAI

TELEGRAM_TOKEN = '8920441173:AAEBcEzFpfFySbw9hFEmbuFX_5J4QLZjQu8'
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
