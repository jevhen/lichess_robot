import telebot

def handlers(bot: telebot.TeleBot):
        @bot.message_handler(commands=['start', 'help'])
        def initial_response(message):
            bot.reply_to(message, "Howdy hoe, working I am!")