import os
from telegram.ext import Updater, CommandHandler
import time

while True:
    try:
        TOKEN = os.getenv("BOT_TOKEN")

        if not TOKEN:
            print("BOT_TOKEN missing!")
            time.sleep(5)
            continue

        updater = Updater(TOKEN, use_context=True)

        def start(update, context):
            update.message.reply_text("Bot is working!")

        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))

        print("Bot running...")
        updater.start_polling()
        updater.idle()

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
