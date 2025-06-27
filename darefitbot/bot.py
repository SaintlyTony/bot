import asyncio
from aiogram import Bot, Dispatcher

from .config import settings
from .handlers import start, workout


def register_handlers(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(workout.router)


async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
