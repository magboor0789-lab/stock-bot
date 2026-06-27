from aiogram import Bot, Dispatcher, executor, types
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("✅ البوت يعمل بنجاح")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("الأوامر:\n/start\n/help")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)