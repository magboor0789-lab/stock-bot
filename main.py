
import asyncio

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from handlers.commands import router
from services.alert_engine import start_background_scanner

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(router)

async def main():
    asyncio.create_task(start_background_scanner(bot))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
