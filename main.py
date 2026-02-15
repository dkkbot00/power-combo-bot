import os
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

# =========================
# TOKEN (Railway Variable)
# =========================
TOKEN = os.getenv("BOT_TOKEN")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher


# =========================
# START MENU
# =========================
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🎮 Game Zone", callback_data='game')],
        [InlineKeyboardButton("📥 Downloader", callback_data='download')],
        [InlineKeyboardButton("🎬 OTT Search", callback_data='ott')],
        [InlineKeyboardButton("🤖 AI Mode", callback_data='ai')],
        [InlineKeyboardButton("🌐 Special Mode", callback_data='special')],
        [InlineKeyboardButton("❓ Help", callback_data='help')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "🔥 *Power Combo Bot*\n\nChoose an option:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


# =========================
# BUTTON HANDLER
# =========================
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'game':
        keyboard = [
            [InlineKeyboardButton("🤖 Play With AI", callback_data='ai_game')],
            [InlineKeyboardButton("🔙 Back", callback_data='back')]
        ]
        query.edit_message_text(
            "🎮 *Game Zone*\nChoose mode:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    elif query.data == 'ai_game':
        user_score = random.randint(1, 10)
        ai_score = random.randint(1, 10)

        if user_score > ai_score:
            result = "🏆 You Win!"
        elif user_score < ai_score:
            result = "🤖 AI Wins!"
        else:
            result = "⚖ Draw!"

        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='back')]]

        query.edit_message_text(
            f"🎲 Your Score: {user_score}\n🤖 AI Score: {ai_score}\n\n{result}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == 'download':
        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='back')]]
        query.edit_message_text(
            "📥 Send YouTube link to download.\n\n(Downloader system connect karna baki hai)",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == 'ott':
        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='back')]]
        query.edit_message_text(
            "🎬 Send movie name to search OTT.\n\n(OTT API connect karna baki hai)",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == 'ai':
        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='back')]]
        query.edit_message_text(
            "🤖 AI Mode Activated!\nAsk anything...",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == 'special':
        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='back')]]
        query.edit_message_text(
            "🌐 Special Mode\nMini browser game coming soon 🚀",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == 'help':
        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='back')]]
        query.edit_message_text(
            "❓ Help Menu\n\nUse /start to open main menu.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == 'back':
        keyboard = [
            [InlineKeyboardButton("🎮 Game Zone", callback_data='game')],
            [InlineKeyboardButton("📥 Downloader", callback_data='download')],
            [InlineKeyboardButton("🎬 OTT Search", callback_data='ott')],
            [InlineKeyboardButton("🤖 AI Mode", callback_data='ai')],
            [InlineKeyboardButton("🌐 Special Mode", callback_data='special')],
            [InlineKeyboardButton("❓ Help", callback_data='help')]
        ]

        query.edit_message_text(
            "🔥 *Power Combo Bot*\n\nChoose an option:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )


# =========================
# MESSAGE HANDLER
# =========================
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    if "youtube.com" in text or "youtu.be" in text:
        update.message.reply_text("📥 Downloader system not connected yet.")

    elif len(text) > 0:
        update.message.reply_text(f"🤖 AI Reply:\nYou said: {text}")


# =========================
# HANDLERS
# =========================
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(button))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))


# =========================
# RUN BOT
# =========================
updater.start_polling()
updater.idle()
