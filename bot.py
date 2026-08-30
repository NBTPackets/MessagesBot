from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
import asyncio
import config

dp = Dispatcher()
bot = Bot(config.TOKEN)
welcomeImage = FSInputFile('welcome.png')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Добро пожаловать! Если у тебя спамблок ты можешь оставить сообщение просто написав его и я напишу тебе сам!")
#  await message.answer_photo(photo=welcomeImage, caption=f"Добро пожаловать! Если у тебя спамблок ты можешь оставить сообщение просто написав его и я напишу тебе сам!")
@dp.message()
async def handle_message(message: Message):
    keyboard = InlineKeyboardMarkup( inline_keyboard=[[InlineKeyboardButton(text="Ответить", url=f"https://t.me/{message.from_user.username or 'user'}")]])
    
    await bot.send_message(config.ID, f"Пользователь @{message.from_user.username or 'без username'} отправил новое сообщение", reply_markup=keyboard)
    
    await message.forward(config.ID)
    
    await message.reply("Я получил сообщение, ожидайте пока я напишу вам.")

async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main()) 