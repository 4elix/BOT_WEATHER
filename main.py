# pytelegrambotapi -> библиотека для создания тг ботов

from config import bot
from handlers import *
from callback import *

# это точка входа
if __name__ == '__main__':
    # infinity_polling -> наш бот букет работать без остановки
    bot.infinity_polling()
