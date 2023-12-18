from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from random import randint

from database import genres, sub_genres
from keyboards import main_navigation_keyboard, choice_genre_keyboard, choice_genre_mood, choice_book, return_to_main
from lexicon import LEXICON
from services import show_description

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=ReplyKeyboardRemove())
    await main_navigation(message)


@router.message(F.text == 'Назад')
async def main_navigation(message: Message):
    await message.answer(
        text=LEXICON['main_choice'], reply_markup=main_navigation_keyboard()
    )


@router.message(F.text == 'Подобрать книгу')
async def process_choice_genre(message: Message):
    await message.answer(
        text=LEXICON['genres'],
        reply_markup=choice_genre_keyboard().as_markup()
        )


@router.message(F.text.in_(genres.keys()))
async def process_choice_mood(message: Message):
    await message.answer(
        text=LEXICON['mood'],
        reply_markup=choice_genre_mood(message.text).as_markup()
    )


@router.message(F.text.in_(sub_genres.keys()))
async def process_choice_mood(message: Message):
    await message.answer(
        text=LEXICON['lets_read'],
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text=LEXICON['choice_book'],
        reply_markup=choice_book(message.text).as_markup()
    )


@router.callback_query(F.data.isdigit())
async def process_read_description(callback: CallbackQuery):
    await callback.message.answer(
        text=show_description(callback.data), reply_markup=return_to_main()
    )


@router.message(F.text == 'Случайная книга')
async def process_choice_genre(message: Message):
    await message.answer(
        text=f"{LEXICON['random_book']}"
             f"\n{show_description(randint(1, 103))}",
        reply_markup=return_to_main())

@router.message()
async def other_messages(message: Message):
    await message.answer(
        text=LEXICON['other']
    )
