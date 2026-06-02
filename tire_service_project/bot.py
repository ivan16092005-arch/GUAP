import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from database import SessionLocal
from models import Appointment

TOKEN = "8430507247:AAFBBQ6R4lR8khpsHNaBEibfwEVe3x8vhC0"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Добро пожаловать!\n\n"
        "Для записи отправьте:\n"
        "Имя;Услуга;Дата\n\n"
        "Пример:\n"
        "Иван Иванов;Замена шин;15.06.2026"
    )


@dp.message(F.text)
async def create_appointment(message: Message):
    try:
        name, service, date = message.text.split(";")

        db = SessionLocal()

        appointment = Appointment(
            name=name.strip(),
            service=service.strip(),
            date=date.strip()
        )

        db.add(appointment)
        db.commit()
        db.close()

        await message.answer("Запись успешно создана!")

    except Exception:
        await message.answer(
            "Неверный формат.\n"
            "Используйте:\n"
            "Имя;Услуга;Дата"
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())