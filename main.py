import os
import yt_dlp
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")

# ===== MENU =====
menu_keyboard = [
    ["🎮 Special Mode", "📥 YouTube"],
    ["🎵 Audio Extract", "🎬 OTT"],
    ["🤖 AI Chat", "❓ Help"]
]
reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)

# ===== START =====
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🔥 Power Combo Bot Activated!\nUse menu below:",
        reply_markup=reply_markup
    )

# ===== MESSAGE HANDLER =====
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text

    if text == "🎮 Special Mode":
        update.message.reply_text(
            "🎮 Play Game:\nhttps://power-game-production.up.railway.app"
        )

    elif text == "📥 YouTube":
        update.message.reply_text("📥 Send YouTube video link to download.")

    elif text == "🎵 Audio Extract":
        update.message.reply_text("🎵 Send video link to extract audio.")

    elif text == "🎬 OTT":
        update.message.reply_text(
            "🎬 OTT Links:\n"
            "Hotstar: https://www.hotstar.com\n"
            "Zee5: https://www.zee5.com\n"
            "SonyLiv: https://www.sonyliv.com\n"
            "Live Cricket: https://www.hotstar.com/in/sports/cricket"
        )

    elif text == "🤖 AI Chat":
        update.message.reply_text("🤖 AI Mode Activated. (Demo mode)")

    elif text == "❓ Help":
        update.message.reply_text("👤 Developer: mr.divakar00")

    elif "youtube.com" in text or "youtu.be" in text:
        download_video(update, context, text)

    else:
        update.message.reply_text("Use menu buttons only.")

# ===== YOUTUBE DOWNLOAD =====
def download_video(update: Update, context: CallbackContext, url):
    update.message.reply_text("⏳ Downloading...")

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for file in os.listdir():
            if file.startswith("video"):
                update.message.reply_video(open(file, 'rb'))
                os.remove(file)
                break

    except Exception as e:
        update.message.reply_text("❌ Download failed.")

# ===== MAIN =====
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
