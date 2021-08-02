from src.setup import bot, logger
from src.helpers import get_links_message, get_info, get_links_from_api, url_message
import src.messages as responses


def send_welcome(message):
    bot.reply_to(
        message, "Bienvenidx a este botardo con información util sobre la Universidad Nacional del Oeste. Escribí <b>/help</b> para saber cómo seguir.")


def help_message(message):
    user_id = message.from_user.id
    logger.info(f"El usuario {user_id} ha solicitado AYUDA.")
    chat_id = message.chat.id
    bot.send_message(chat_id, responses.help_message())


def get_useful_links(message):
    user_id = message.from_user.id
    logger.info(f"El usuario {user_id} ha solicitado LINKS.")
    chat_id = message.chat.id
    bot.send_message(chat_id, get_links_message())


def request_url_information(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    logger.info(
        f"El usuario {user_id} ha solicitado información de {message.text}.")
    if message.text == "/siu":
        url = 'https://autogestion.uno.edu.ar/uno/'
        name = "siu guarani"
    elif message.text == "/campus":
        url = 'http://campusvirtual.uno.edu.ar/moodle/'
        name = 'campus'

    bot.send_message(
        chat_id, f"<i>Solicitando información a {url} ...</i>")
    bot.send_message(chat_id, url_message(url, name))


def get_comunidades_it(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    logger.info(f"El usuario {user_id} ha solicitado Comunidades IT.")
    bot.send_message(chat_id, responses.comunidades_it())


def get_academic_calendar(message):
    arguments = message.text.split()
    user_id = message.from_user.id
    chat_id = message.chat.id
    if len(arguments) > 1 and arguments[1] == 'feriados':
        logger.info(
            f"El usuario {user_id} ha solicitado el Calendario de Feriados.")
        bot.send_message(chat_id, responses.calendario_feriados_message())
    else:
        logger.info(
            f"El usuario {user_id} ha solicitado el Calendario Académico.")
        bot.send_message(chat_id, responses.calendario_academico_message())


def get_emails(message):
    arguments = message.text.split()
    user_id = message.from_user.id
    chat_id = message.chat.id
    logger.info(f"El usuario {user_id} ha solicitado MAILS.")
    if len(arguments) > 1:
        bot.send_message(chat_id, responses.get_mails_by_term(arguments[1]))
    else:
        bot.send_message(chat_id, responses.get_mails_by_term())
