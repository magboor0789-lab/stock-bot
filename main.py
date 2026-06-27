from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("🚀 البوت يعمل بنجاح")

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply("✅ البوت جاهز")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)