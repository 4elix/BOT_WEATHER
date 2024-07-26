from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from database.for_users import search_tg_user

# ReplyKeyboardMarkup -> класс для настройки кнопки
# KeyboardButton -> класс для контента кнопки


def start_menu(tg_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    # resize_keyboard -> указываем True, что-бы кнопку было равна тексту
    # row_width -> сколько хотим располагать кнопок на одной ширине

    user = search_tg_user(tg_id)
    if user is not None:
        markup.add(
            KeyboardButton(text='Узнать погоду'),
            KeyboardButton(text='История запросов')
        )
    else:
        markup.add(
            KeyboardButton(text='Регистрация')
        )
    return markup


def send_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        # request_contact=True -> позволит отправить свой контакт
        KeyboardButton(text='Поделиться контактом', request_contact=True)
    )
    return markup

