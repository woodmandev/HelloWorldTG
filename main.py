
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
from importlib import resources
from icmplib import ping

TG_TOKEN = ""
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

    global TG_TOKEN
    with resources.open_text("resources", "secret.properties") as secret:
        lines = secret.readlines()
        for line in lines:
            line = line.strip()
            if line.split(":")[0] == "TG_TOKEN":
                TG_TOKEN = line.replace(f"{line.split(':')[0]}:", "")
    print(TG_TOKEN)
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