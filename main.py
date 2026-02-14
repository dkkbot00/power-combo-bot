import os

TOKEN = os.getenv("BOT_TOKEN")

print("TOKEN VALUE:", TOKEN)

if not TOKEN:
    raise ValueError("BOT_TOKEN not found!")

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
