from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TG_TOKEN="5808341596:AAHSHyUYnpgsMc5DOazWgm2Aq7CmtzT5ZI4"

def start(update, context):
    update.message.reply_text("start using bot")

def help(update, context):
    update.message.reply_text("you need help?")

def main ():
    updater = Updater(TG_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()