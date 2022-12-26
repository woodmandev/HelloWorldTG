from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TG_TOKEN="5808341596:AAHSHyUYnpgsMc5DOazWgm2Aq7CmtzT5ZI4"

def start(update, context):
    print('user enter start')
    update.message.reply_text("start using bot")

def help(update, context):
    print('user enter help')
    update.message.reply_text("you need help?")
def getMessage(update, context):
    userText = update.message.text
    print(userText)
    update.message.reply_text(f'You say: "{userText}"')

def main ():
    updater = Updater(TG_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.text, getMessage))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()