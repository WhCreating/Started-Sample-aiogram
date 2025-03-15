rom aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

import asyncio

from config_data.config import load_config
from logs.log import logs

import logging


async def main():
    logger = logging.getLogger(__name__)
    logs()

    config = load_config()

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
