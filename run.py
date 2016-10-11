import logging

from slackbot.bot import Bot

logging.basicConfig()

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
