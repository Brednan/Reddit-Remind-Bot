import time

from bot import Bot


if __name__ == '__main__':
    bot = Bot('./account.txt')
    while True:
        bot.bot_sequence()
        time.sleep(10)
