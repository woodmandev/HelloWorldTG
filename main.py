from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
TG_TOKEN="5808341596:AAHSHyUYnpgsMc5DOazWgm2Aq7CmtzT5ZI4"

def start(update, context):
    print('user enter start')
    # print(f'{telegram.Bot.send_message('')}')
    update.message.reply_text("start using bot")

def help(update, context):
    print('user enter help')
    update.message.reply_text("you need help?")
def getMessage(update, context):
    userText = update.message.text
    user = update.message.from_user
    # chat = telegram.Chat("@normaldevtest", telegram.Chat.GROUP)
    # print(f"{telegram.Chat('@normaldevtest').id}")
    bot = telegram.Bot(TG_TOKEN)
    bot.sendMessage("@normaldevtest", f"{userText}")
    # telegram.Bot.send_message(telegram.Chat("@normaldevtest").id, f"{userText}", "HTML ")
    print(f"{userText} from {user}")
    # update.message.reply_text(f'You say: "{userText}"')

def sendReply(update, context):


    print(f"REPLY: {update.message.text}")
    replyText = update.message.text
    user = update.message.from_user.id
    bot = telegram.Bot(TG_TOKEN)
    bot.sendMessage(user, replyText)
def main ():
    updater = Updater(TG_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.chat_type.private, getMessage))
    dispatcher.add_handler(MessageHandler(Filters.reply, sendReply))
    updater.start_polling()
    updater.idle()




if __name__ == "__main__":
    main()