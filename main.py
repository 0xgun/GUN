import telegram.ext
from config import token

updater = telegram.ext.Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def help(update, context):
    update.message.reply_text(
        '''
        Help!
        /sum <address> - get sum of all transactions
        /last <address> - get last transaction
        /failed <address> - get failed transactions
        '''
    )
def sum(update, context):
    update.message.reply_text('sum')

def last(update, context):
    update.message.reply_text('last')

def failed(update, context):
    update.message.reply_text('failed')


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('sum', sum))
dispatcher.add_handler(telegram.ext.CommandHandler('last', last))
dispatcher.add_handler(telegram.ext.CommandHandler('failed', failed))

updater.start_polling()
updater.idle()
