import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# ================= CONFIG =================
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ⚠️ Abhi temporarily 0 rakha hai
# /getid se apna ID nikaal ke yaha daalna
ADMIN_ID = 0

if not BOT_TOKEN:
    print("❌ BOT_TOKEN missing")
    exit()

updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


# ================= MENU =================
menu = ReplyKeyboardMarkup(
    [
        ["🎮 Special Mode", "📥 YouTube"],
        ["🎵 Audio Extract", "🎬 OTT"],
        ["🤖 AI Chat", "❓ Help"]
    ],
    resize_keyboard=True
)


# ================= START =================
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🔥 POWER COMBO BOT 🔥\n\nSelect option:",
        reply_markup=menu
    )


# ================= GET ID =================
def getid(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text(f"🆔 Your Telegram ID:\n{user.id}")


# ================= USERS (ADMIN ONLY) =================
def users(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        update.message.reply_text("👑 Admin access granted.\n(User system coming next phase)")
    else:
        update.message.reply_text("❌ You are not admin.")


# ================= MESSAGE HANDLER =================
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


# ================= HANDLERS =================
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("getid", getid))
dispatcher.add_handler(CommandHandler("users", users))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))


# ================= RUN =================
updater.start_polling()
updater.idle()
