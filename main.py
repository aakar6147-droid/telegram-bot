import telebot
import google.generativeai as genai

TELEGRAM_BOT_TOKEN = "8920441173:AAEBcEzFpfFySbW9hfEmbuFX_5J4QLZjQu8"
GEMINI_API_KEY = "AQ.Ab8RN6Kpc2Khv6W7z_3lpz5LEekAD-3niz2jMnwWjhNNZ366Ow"

genai.configure(api_key=GEMINI_API_KEY)
# Using standard flash model configuration
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سڵاو! من بۆتی جێمنی (Gemini) م. چۆن دەتوانم یارمەتیت بدەم؟")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"هەڵەیەک ڕوویدا: {e}")

print("Bot is running with Gemini...")
bot.infinity_polling()
