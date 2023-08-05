from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

b1 = KeyboardButton('/Режим работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)

# Заменяет клавиатуру на кнопки
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# add - кнопки во всю строку, insert в свободное место,
kb_client.add(b1).add(b2).insert(b3)
# kb_client.row(b1, b2, b3)