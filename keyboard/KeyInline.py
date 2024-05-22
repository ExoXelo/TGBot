from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://www.drive2.ru/b/1017245/')
    but_inline_2 = InlineKeyboardButton('Посмотреть', url='https://www.drive2.ru/b/1017245/')
    keyboard_inline.add(but_inline, but_inline_2)
    return keyboard_inline