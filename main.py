import os
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher


# ================= MENU =================
def start(update: Update, context: CallbackContext):
    keyboard = [
        ["🎮 Special Mode", "📥 YouTube"],
        ["🎵 Audio Extract", "🎬 OTT"],
        ["🤖 AI Chat", "❓ Help"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("🔥 Welcome to Power Combo Bot\nSelect option:", reply_markup=reply_markup)


# ================= BUTTON HANDLER =================
def handle_buttons(update: Update, context: CallbackContext):
    text = update.message.text

    if text == "🎮 Special Mode":
        update.message.reply_text("🎮 Play Game:\nhttps://power-game-production.up.railway.app")

    elif text == "📥 YouTube":
        update.message.reply_text("📥 Send YouTube link to download.")

    elif text == "🎵 Audio Extract":
        update.message.reply_text("🎵 Send video link to extract audio.")

    elif text == "🎬 OTT":
        update.message.reply_text("🎬 OTT Links:\nHotstar\nZee5\nSonyLiv\nLive Cricket")

    elif text == "🤖 AI Chat":
        update.message.reply_text("🤖 AI Mode Activated. Ask anything.")

    elif text == "❓ Help":
        update.message.reply_text("👤 Developer: mr.divakar00")

    else:
        update.message.reply_text("Use menu buttons only.")


# ================= HANDLERS =================
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_buttons))


# ================= RUN =================
updater.start_polling()
updater.idle()
