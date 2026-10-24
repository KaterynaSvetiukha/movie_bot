from aiogram.utils.keyboard import KeyboardBuilder
from models import FilmCallback

def films_inline_keyboard_markup(list_films: list[dict]):
    builder = KeyboardBuilder()
    builder.adjust(1, repeat=True)