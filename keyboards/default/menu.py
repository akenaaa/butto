from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="anime"),
        ],
        [
            KeyboardButton(text="dorama"),
            KeyboardButton(text="mandga")
        ],
    ],
    resize_keyboard=True
)