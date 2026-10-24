from aiogram.filters.callback_data import CallbackData

class FilmCallback(CallbackData, prefix='film', sep=";"):
    id: int
    name: str