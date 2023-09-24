import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, WebAppInfo

dp = Dispatcher()
TOKEN = "TOKEN @BotFather"


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(
        text="Купить",
        web_app=WebAppInfo(url="https://what-xd.github.io/SaleKoumiss/")
    )
    )

    await message.answer(f"👋", reply_markup=builder.as_markup(resize_keyboard=True))


@dp.message(lambda x: bool(x.web_app_data))
async def answer(message):
    await message.answer(f"Спасибо что купили <code>{message.web_app_data.data.replace('buy-', '')} шт.</code> кумыса!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
