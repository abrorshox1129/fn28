

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message




API_TOKEN = '7829304194:AAFS5gAwbEp-5x-XTrwFK6b7S8ixZB4LRO8'

# Bot va Dispatcher obyektlarini yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# `/start` va `/help` komandalariga javob beruvchi handler
@dp.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.answer("Salom!\nMen oddiy Answer botman!\nMenga yozgan xabaringizni qaytaraman!")

# Barcha boshqa xabarlarga javob beruvchi handler (echo funksiyasi)
@dp.message()
async def echo(message: Message):
    await message.answer(message.text)

# Botni ishga tushirish
async def main():
    # Eski xabarlarni o'chirish va pollingni boshlash
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
