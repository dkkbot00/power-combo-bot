import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 5238180335   # 👈 Yaha apna Telegram ID daalo

# Menu
menu_keyboard = [
    ["🎮 Special Mode", "📥 YouTube"],
    ["🎵 Audio Extract", "🎬 OTT"],
    ["🤖 AI Chat", "❓ Help"]
]

reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)

# Notify admin
def notify_admin(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = f"""
🚀 New User Activity

👤 Name: {user.first_name}
🔗 Username: @{user.username}
🆔 ID: {user.id}
💬 Message: {update.message.text}
"""
    context.bot.send_message(chat_id=ADMIN_ID, text=message)

# Start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Use menu options.", reply_markup=reply_markup)
    notify_admin(update, context)

# Menu Handler
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text

    notify_admin(update, context)

    if text == "🎮 Special Mode":
        update.message.reply_text("🎮 Play Game:\nhttps://power-game-production.up.railway.app")

    elif text == "📥 YouTube":
        update.message.reply_text("Send YouTube link.")

    elif text == "🎵 Audio Extract":
        update.message.reply_text("Send video link to extract audio.")

    elif text == "🎬 OTT":
        update.message.reply_text(
            "Hotstar: https://www.hotstar.com\n"
            "Zee5: https://www.zee5.com\n"
            "SonyLiv: https://www.sonyliv.com\n"
            "Live Cricket: https://www.hotstar.com/sports"
        )

    elif text == "🤖 AI Chat":
        update.message.reply_text("AI Mode Activated. Ask anything.")

    elif text == "❓ Help":
        update.message.reply_text("Developer: mr.divakar00")

    else:
        update.message.reply_text("Use menu buttons only.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
