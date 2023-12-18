from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from database import genres, sub_genres
from lexicon import LEXICON


def main_navigation_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=LEXICON['find_book']),
            KeyboardButton(text=LEXICON['get_random'])
        ]], resize_keyboard=True
    )

    return keyboard


def choice_genre_keyboard():
    buttons: list[KeyboardButton] = [
        KeyboardButton(text=genre) for genre in genres.keys()
    ]
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(*buttons, width=3)

    return kb_builder


def choice_genre_mood(gener: str): # ожидаемый тип
    buttons: list[KeyboardButton] = [
        KeyboardButton(text=genre) for genre in genres[gener]
    ]
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(*buttons, width=3)

    return kb_builder


def choice_book(sub_gener: str):
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(
            text=book_name,
            callback_data=str(book_id)
        ) for book_name, book_id in sub_genres[sub_gener].items()
    ]
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*buttons, width=1)

    return kb_builder


def return_to_main():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=LEXICON['back']),
        ]], resize_keyboard=True
    )

    return keyboard
