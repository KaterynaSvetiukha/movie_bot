import asyncio
from aiogram import Bot, Dispatcher, html
from aiogram.types import Message
from config import TOKEN_BOT
from aiogram.filters import Command

dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message) -> None:
    user_name = message.from_user.full_name
    await message.answer(f'Вітаю, {html.bold(user_name)} :)')

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer('Відбулася помилка!')

async def main() -> None:
    bot = Bot(token=TOKEN_BOT)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())