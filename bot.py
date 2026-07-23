import os
import asyncio
import random

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("8870694306:AAFmVW4WSXgjoz2H2KIPlApPPkYGD5rcFsY")

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
