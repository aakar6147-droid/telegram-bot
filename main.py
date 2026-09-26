import telebot
import openai

TELEGRAM_BOT_TOKEN = "8920441173:AAEBcEzFpfFySbW9hfEmbuFX_5J4QLZjQu8"
openai.api_key = "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"

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
