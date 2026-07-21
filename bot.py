from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import requests

TOKEN = 8867639105:AAGlPoaPjC5LLWZz_1dzOguT_eQhO9Lz0fs

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text

    url = f"https://api.deezer.com/search?q={query}"
    data = requests.get(url).json()

    if data["data"]:
        song = data["data"][0]
        text = (
            f"🎵 {song['title']}\n"
            f"👤 {song['artist']['name']}\n"
            f"💿 {song['album']['title']}\n\n"
            f"🎧 {song['link']}"
        )
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("❌ Песня не найдена.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

app.run_polling()
