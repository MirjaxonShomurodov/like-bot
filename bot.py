# export 
from telegram import Update
from telegram.ext import (
    CallbackContext, 
    Updater, 
    CommandHandler, 
    MessageHandler,
    Filters
    )
import os
TOKEN = os.environ["TOKEN"]
def start(update:Update,context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id,"Welcome to Bot!")

def echo(update:Update,context:CallbackContext):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id

    # count = "Like: 1\nDislike: 1"
    count=1
    if count=="👍":
        count= f"Like: {count+1}\nDislike: {count+1}"
        return count
    bot.sendMessage(chat_id,count)

updater = Updater(token = TOKEN)
updater.dispatcher.add_handler(CommandHandler("start",start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()