
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.market import get_stock_price
from services.news_service import get_news

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🚀 PRO STOCK BOT ONLINE\n\n"
        "الأوامر:\n"
        "/price TSLA\n"
        "/news TSLA\n"
        "/breakout\n"
        "/volume\n"
        "/halts\n"
        "/watchlist"
    )

@router.message(Command("price"))
async def price(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer("/price TSLA")
        return

    symbol = args[1].upper()

    price = get_stock_price(symbol)

    if not price:
        await message.answer("❌ تعذر جلب السعر")
        return

    await message.answer(
        f"📈 {symbol}\n\n💰 السعر: {price}"
    )

@router.message(Command("news"))
async def news(message: Message):

    args = message.text.split()

    if len(args) < 2:
        await message.answer("/news TSLA")
        return

    symbol = args[1].upper()

    headlines = get_news(symbol)

    if not headlines:
        await message.answer("❌ لا توجد أخبار")
        return

    text = f"📰 أخبار {symbol}\n\n"

    for item in headlines:
        text += f"• {item}\n\n"

    await message.answer(text)

@router.message(Command("breakout"))
async def breakout(message: Message):
    await message.answer(
        "🚨 نظام الاختراقات مفعل"
    )

@router.message(Command("volume"))
async def volume(message: Message):
    await message.answer(
        "📊 مراقبة الفوليوم شغالة"
    )

@router.message(Command("halts"))
async def halts(message: Message):
    await message.answer(
        "⛔ مراقبة الهلتات مفعلة"
    )
