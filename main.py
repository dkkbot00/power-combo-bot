import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("❌ BOT_TOKEN not found")
    exit()

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher


# 🔥 MAIN MENU
main_menu = ReplyKeyboardMarkup(
    [
        ["🎮 Special Mode", "📥 YouTube Download"],
        ["🎵 Audio Extract", "🎬 OTT Search"],
        ["🤖 AI Chat", "❓ Help"]
    ],
    resize_keyboard=True
)


# ✅ START COMMAND
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🔥 Welcome to POWER COMBO BOT 🔥\n\nSelect an option:",
        reply_markup=main_menu
    )


# ✅ AUTO START ON HI HELLO
def auto_start(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if text in ["hi", "hello", "hey", "hii"]:
        start(update, context)
    else:
        handle_message(update, context)


# ✅ MESSAGE HANDLER
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text

    if text == "🎮 Special Mode":
        update.message.reply_text(
            "🎮 POWER GAME MODE\n\nClick below to play:\n\n"
            "👉 https://power-game-production.up.railway.app"
        )

    elif text == "📥 YouTube Download":
        update.message.reply_text(
            "📥 Send YouTube video link to download."
        )

    elif text == "🎵 Audio Extract":
        update.message.reply_text(
            "🎵 Send YouTube link to extract MP3."
        )

    elif text == "🎬 OTT Search":
        update.message.reply_text(
            "🎬 OTT Platforms:\n\n"
            "🔥 Hotstar: https://www.hotstar.com\n"
            "🎥 Zee5: https://www.zee5.com\n"
            "📺 SonyLiv: https://www.sonyliv.com\n"
            "🏏 Live Cricket: https://www.hotstar.com/in/sports/cricket"
        )

    elif text == "🤖 AI Chat":
        update.message.reply_text(
            "🤖 AI Mode Active\n\nType anything..."
        )

    elif text == "❓ Help":
        update.message.reply_text(
            "📞 Help & Support\n\nInstagram: mr.divakar00"
        )

    else:
        update.message.reply_text(
            "❓ Please select from menu.",
            reply_markup=main_menu
        )


# 🔥 HANDLERS
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_start))


# 🚀 RUN BOT
updater.start_polling()
updater.idle()
