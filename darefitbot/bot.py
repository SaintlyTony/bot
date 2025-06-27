import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from .config import settings
from .handlers import start, workout, ads


def register_handlers(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(workout.router)
    dp.include_router(ads.router)


async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
