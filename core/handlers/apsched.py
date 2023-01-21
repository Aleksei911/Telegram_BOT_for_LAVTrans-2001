import asyncio
from aiogram import Bot
from core.settings import settings
from .data_fetcher import get_car, get_driver


async def send_message_car(bot: Bot):
    cars = await get_car()
    if cars:
        await bot.send_message(settings.bots.group_id, 'ВНИМАНИЕ!!!!')
        for car in cars:
            answer = f"{car['number']}\n" \
                     f"Техосмотр до - {car['tehosmotr']}\n" \
                     f"Страховка до - {car['strahovka']}\n" \
                     f"Таможенное до - {car['tamogennoye']}\n" \
                     f"Тахограф до - {car['tahograf']}"
            await bot.send_message(settings.bots.group_id, answer)


async def send_message_driver(bot: Bot):
    await asyncio.sleep(2)
    drivers = await get_driver()
    if drivers:
        await bot.send_message(settings.bots.group_id, 'ВНИМАНИЕ!!!!')
        for driver in drivers:
            answer = f"{driver['name']} {driver['last_name']}\n" \
                     f"Паспорт до - {driver['passport']}\n" \
                     f"Виза до - {driver['visa']}\n" \
                     f"Водительское до - {driver['driver_card']}"
            await bot.send_message(settings.bots.group_id, answer)
