import os
import random
from telegram import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.getenv("BOT_TOKEN")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher


# ================= MAIN MENU =================

def main_menu():
    keyboard = [
        ["🎮 Special Mode"],
        ["📥 YouTube", "🎵 Audio Extract"],
        ["🎬 OTT Links"],
        ["🤖 AI Chat"],
        ["❓ Help"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# ================= START =================

def start(update, context):
    update.message.reply_text(
        "🔥 POWER COMBO BOT 🔥\nChoose option:",
        reply_markup=main_menu()
    )


# ================= MESSAGE HANDLER =================

def handle_message(update, context):
    text = update.message.text.lower()

    # Greeting Auto Start
    if text in ["hi", "hello", "hey", "hii"]:
        start(update, context)

    # Special Mode
    elif "special" in text:
        game_button = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                "🎮 Play Online Game",
                web_app=WebAppInfo(url="https://google.com")
            )]
        ])
        update.message.reply_text(
            "🔥 Special Mode Activated!",
            reply_markup=game_button
        )

    # YouTube
    elif "youtube" in text:
        update.message.reply_text(
            "📥 Send YouTube link.\nChoose:\n🎥 Video\n🎵 Audio"
        )

    # Audio Extract
    elif "audio" in text:
        update.message.reply_text(
            "🎵 Send video link to extract audio."
        )

    # OTT Links
    elif "ott" in text:
        ott_buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔥 Hotstar", url="https://www.hotstar.com")],
            [InlineKeyboardButton("🎥 Zee5", url="https://www.zee5.com")],
            [InlineKeyboardButton("📺 SonyLIV", url="https://www.sonyliv.com")],
            [InlineKeyboardButton("🏏 Live Cricket", url="https://www.hotstar.com/in/sports/cricket")]
        ])
        update.message.reply_text(
            "🎬 OTT Platforms:",
            reply_markup=ott_buttons
        )

    # AI Chat
    elif "ai" in text:
        update.message.reply_text("🤖 AI Mode Activated! Ask me anything.")

    # Help
    elif "help" in text:
        update.message.reply_text(
            "👤 Developer: @mr.divakar00\n"
            "📩 Instagram: mr.divakar00"
        )

    else:
        update.message.reply_text(
            "Type hi to open menu."
        )


# ================= HANDLERS =================

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()
