from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import BOT_TOKEN, ADMIN_ID
from database import add_user, get_total_users


updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


# ===== MENU =====
menu = ReplyKeyboardMarkup(
    [
        ["🎮 Special Mode", "📥 YouTube"],
        ["🎵 Audio Extract", "🎬 OTT"],
        ["🤖 AI Chat", "❓ Help"]
    ],
    resize_keyboard=True
)


# ===== START =====
def start(update: Update, context: CallbackContext):
    user = update.effective_user

    add_user(user.id, user.username)

    update.message.reply_text(
        "🔥 POWER COMBO BOT 🔥\n\nSelect option:",
        reply_markup=menu
    )


# ===== ADMIN COMMAND =====
def users(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        total = get_total_users()
        update.message.reply_text(f"👥 Total Users: {total}")
    else:
        update.message.reply_text("❌ Unauthorized")


# ===== MESSAGE HANDLER =====
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    if text in ["hi", "hello", "hey"]:
        start(update, context)

    elif "special" in text:
        update.message.reply_text(
            "🎮 Play Game:\nhttps://power-game-production.up.railway.app"
        )

    elif "help" in text:
        update.message.reply_text(
            "👤 Developer: mr.divakar00"
        )

    else:
        update.message.reply_text("Use menu options.")


# ===== HANDLERS =====
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("users", users))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))


# ===== RUN =====
updater.start_polling()
updater.idle()
