from decouple import config
import telebot

import handlers


def bot_initialize(bot_token):
    bot = telebot.TeleBot(bot_token, parse_mode=None)
    handlers.handlers(bot)
    bot.infinity_polling()


if __name__ == '__main__':
    BOT_TOKEN = config('BOT_TOKEN')
    bot_initialize(BOT_TOKEN)
