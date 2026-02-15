import os
import asyncio
from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import yt_dlp

# ================= CONFIG ================= #

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 5238180335   # 👈 Apna Telegram user ID daalo

# ================= MENU ================= #

def main_menu():
    keyboard = [
        ["📥 YouTube Info", "🎵 Audio Extract"],
        ["🎬 OTT Links", "🎮 Special Mode"],
        ["❓ Help"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ================= START ================= #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # Admin log
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"👤 New User:\nName: {user.first_name}\nUsername: @{user.username}\nID: {user.id}"
    )

    await update.message.reply_text(
        "🔥 Welcome to Power Combo Bot 🔥\n\nSelect option below 👇",
        reply_markup=main_menu()
    )

# ================= HELP ================= #

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📩 Contact Insta: mr.divakar00\nAdmin: @Mr_anssh00"
    )

# ================= OTT ================= #

async def ott_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Official OTT Platforms:\n\n"
        "🔥 Hotstar:\nhttps://www.hotstar.com\n\n"
        "🎥 Zee5:\nhttps://www.zee5.com\n\n"
        "📺 SonyLIV:\nhttps://www.sonyliv.com\n\n"
        "🏏 Cricket Live:\nhttps://www.hotstar.com/in/sports/cricket"
    )

# ================= SPECIAL MODE ================= #

async def special_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Play Power Game Here:\n"
        "https://power-game-production.up.railway.app"
    )

# ================= YOUTUBE INFO ================= #

async def youtube_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📥 Send YouTube link.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Auto start if hi/hello
    if text in ["hi", "hello", "hey", "hii"]:
        await update.message.reply_text(
            "🔥 Welcome Back!\nChoose option 👇",
            reply_markup=main_menu()
        )
        return

    # If link detected
    if text.startswith("http"):
        await update.message.reply_text("🔎 Fetching video info...")

        try:
            ydl_opts = {'quiet': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(text, download=False)

                title = info.get("title", "Unknown")
                duration = info.get("duration", 0)

            await asyncio.sleep(1.5)

            await update.message.reply_text(
                f"🎬 Title: {title}\n⏱ Duration: {duration} sec"
            )

        except Exception:
            await update.message.reply_text(
                "❌ Sorry bhai, link process nahi ho paya."
            )

        return

    # Default
    await update.message.reply_text(
        "⚡ Please select option from menu.",
        reply_markup=main_menu()
    )

# ================= AUDIO EXTRACT ================= #

async def audio_extract(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 Send video file to extract audio."
    )

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = await update.message.video.get_file()
    await video.download_to_drive("video.mp4")

    await update.message.reply_text("🔄 Extracting audio...")

    os.system("ffmpeg -i video.mp4 -vn -ab 192k audio.mp3")

    await update.message.reply_audio(audio=open("audio.mp3", "rb"))

# ================= MAIN ================= #

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))

app.add_handler(MessageHandler(filters.Regex("📥 YouTube Info"), youtube_info))
app.add_handler(MessageHandler(filters.Regex("🎵 Audio Extract"), audio_extract))
app.add_handler(MessageHandler(filters.Regex("🎬 OTT Links"), ott_links))
app.add_handler(MessageHandler(filters.Regex("🎮 Special Mode"), special_mode))

app.add_handler(MessageHandler(filters.VIDEO, handle_video))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

print("Bot running...")
app.run_polling()
