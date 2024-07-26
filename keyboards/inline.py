from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# InlineKeyboardMarkup -> класс для настройки кнопки
# InlineKeyboardButton -> класс для контента кнопки


def inline_questionnaire(dt_request, user_id):
    inline = InlineKeyboardMarkup()
    inline.add(
        # callback_data -> что-бы отлавливать нашу кнопку. так как inline кнопка не отправляет в чат сообщении,
        # поэтому мы будет искать по callback_data
        InlineKeyboardButton(text='Правильно', callback_data=f'true_{dt_request}_{user_id}'),
        InlineKeyboardButton(text='Не правильно', callback_data=f'false_{dt_request}_{user_id}')
    )
    return inline


def inline_menu(user_id, message_id):
    inline = InlineKeyboardMarkup()
    inline.add(
        InlineKeyboardButton(text='Удалить все запросы', callback_data=f'delete_{user_id}_{message_id}'),
        InlineKeyboardButton(text='Назад', callback_data='back')
    )
    return inline
