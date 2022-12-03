## flask app for telegram bot

from flask import Flask, request
from config import token
import telegram
import logging

app = Flask(__name__)

bot = telegram.Bot(token=token)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

@app.route('/{}'.format(token), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)

    bot.sendMessage(chat_id=chat_id, text="I'm a bot, please talk to me!", reply_to_message_id=msg_id)

    return 'ok'

@app.route('/')
def index():
    return 'ok'

if __name__ == '__main__':
    app.run(threaded=True)
