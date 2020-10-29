import random
import string  # to process standard python strings

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from ufrpe_bot import Chatbot
import spacy

TOKEN = '1302545048:AAHVpW-QZCr0-nz6PBeWgr_IAvpfJD-gbYE'

# Keyword Matching
GREETING_INPUTS = ("ola", "oi", "eai", "yo", "hello", "hey", "ei", "tudo bom?", "tdb")
GREETING_RESPONSES = ["ola", "oi", "Hey", "Feliz em falar com você!"]
THANKS_INPUTS = ['obrigada', 'obrigado', 'obg', 'vlw', 'valeu']
BYE_INPUTS = ['tchau', 'flw', 'bye']
nlp = spacy.load('pt_core_news_sm')


def start(bot, update):
    response_message = "Olá! tem alguma dúvida em relação ao PLE?"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def unknown(bot, update):
    response_message = "----------------"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def make_response(user_response):
    def greeting(sentence):
        """If user's input is a greeting, return a greeting response"""
        for word in sentence:
            if word.lower_ in GREETING_INPUTS:
                return random.choice(GREETING_RESPONSES)

    def check_is_phrase_only_greetings_thanks_or_bye(word):
        is_greeting = word.lower_ in GREETING_INPUTS
        is_thanks = word.lower_ in THANKS_INPUTS
        is_bye = word.lower_ in BYE_INPUTS

        return is_greeting or is_bye or is_thanks

    user_response = user_response.lower()
    print(user_response)
    translator = str.maketrans('', '', string.punctuation)
    print(user_response.translate(translator))
    phrase = nlp(user_response.translate(translator))

    is_phrase_only_greetings_thanks_or_bye = all(check_is_phrase_only_greetings_thanks_or_bye(word) for word in phrase)
    print(is_phrase_only_greetings_thanks_or_bye)
    message = ''
    if greeting(phrase):
        message = message + '\n' + greeting(phrase)

    if not is_phrase_only_greetings_thanks_or_bye:
        chat = Chatbot()
        bot_response = chat.perguntar(user_response)
        message = message + '\n' + bot_response

    if any(thanks in [word.lower_ for word in phrase] for thanks in THANKS_INPUTS):
        message = message + '\n' + "De nada..."

    if any(bye in [word.lower_ for word in phrase] for bye in BYE_INPUTS):
        message = message + '\n' + "Tchauzinho! até mais.."

    return message


def get_response(bot, update):
    print('getting a response')

    bot_response = make_response(update.message.text)

    print(f'message: {bot_response}')
    bot.send_message(
        chat_id=update.message.chat_id,
        text=bot_response
    )


def main():
    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.text, get_response)
    )

    updater.start_polling()
    #updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
