import time

from bot import Bot


if __name__ == '__main__':
    bot = Bot('./account.txt')
    while True:
        try:
            bot.bot_sequence()

        except:
            pass

        time.sleep(6)
