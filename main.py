import os
import yt_dlp
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher


# ================= MENU =================
def show_menu(update):
    keyboard = [
        ["🎮 Special Mode", "📥 YouTube"],
        ["🎵 Audio Extract", "🎬 OTT"],
        ["🤖 AI Chat", "❓ Help"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("🔥 Power Combo Bot\nSelect option:", reply_markup=reply_markup)


# ================= START + GREETING =================
def start(update: Update, context: CallbackContext):
    show_menu(update)

def greeting(update: Update, context: CallbackContext):
    show_menu(update)


# ================= BUTTON HANDLER =================
def handle_buttons(update: Update, context: CallbackContext):
    text = update.message.text

    if text == "🎮 Special Mode":
        update.message.reply_text(
            "🎮 Play Game:\nhttps://power-game-production.up.railway.app"
        )

    elif text == "📥 YouTube":
        context.user_data["mode"] = "youtube"
        update.message.reply_text("📥 Send YouTube link.")

    elif text == "🎵 Audio Extract":
        context.user_data["mode"] = "audio"
        update.message.reply_text("🎵 Send video file.")

    elif text == "🎬 OTT":
        update.message.reply_text(
            "🎬 OTT Links:\n"
            "Hotstar: https://www.hotstar.com\n"
            "Zee5: https://www.zee5.com\n"
            "SonyLiv: https://www.sonyliv.com\n"
            "Live Cricket: https://www.hotstar.com/in/sports/cricket"
        )

    elif text == "🤖 AI Chat":
        context.user_data["mode"] = "ai"
        update.message.reply_text("🤖 AI Mode Activated. Ask anything.")

    elif text == "❓ Help":
        update.message.reply_text("👤 Developer: mr.divakar00")

    else:
        handle_modes(update, context)


# ================= MODE LOGIC =================
def handle_modes(update: Update, context: CallbackContext):
    mode = context.user_data.get("mode")

    # ===== AI MODE =====
    if mode == "ai":
        update.message.reply_text(f"🤖 AI: You said -> {update.message.text}")

    # ===== YOUTUBE DOWNLOAD =====
    elif mode == "youtube":
        url = update.message.text
        update.message.reply_text("⏳ Downloading...")
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'video.%(ext)s'
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            for file in os.listdir():
                if file.startswith("video"):
                    update.message.reply_video(open(file, "rb"))
                    os.remove(file)
                    break
        except:
            update.message.reply_text("❌ Download failed.")

    else:
        update.message.reply_text("Use menu buttons only.")


# ================= AUDIO EXTRACT =================
def audio_extract(update: Update, context: CallbackContext):
    mode = context.user_data.get("mode")
    if mode == "audio" and update.message.video:
        file = update.message.video.get_file()
        file.download("video.mp4")

        os.system("ffmpeg -i video.mp4 -q:a 0 -map a audio.mp3")

        update.message.reply_audio(open("audio.mp3", "rb"))

        os.remove("video.mp4")
        os.remove("audio.mp3")


# ================= HANDLERS =================
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.regex("^(hi|hello|hey|hii|Hi|Hello)$"), greeting))
dp.add_handler(MessageHandler(Filters.video, audio_extract))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_buttons))

updater.start_polling()
updater.idle()
