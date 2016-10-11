from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

from models import User

@respond_to('hi|hello', re.IGNORECASE)
def hi(message):
    message.reply('Hello, <@{}>!'.\
        format(message._client.users.get(message.body["user"])["name"]))

@respond_to('assembla key register (.*)')
def keyregister(message, key):
    sender = message._client.users.get(message.body["user"])["name"]

    query = User.select().where(User.name == sender)

    if query.exists():
        message.reply('You have already added the key. Please use \
<key update> to update the key.')
    else:
        user = User.create(name=sender, assembla_key=key)
        user.save()
        message.reply('Your key has been added!')
    
@listen_to('help')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')
