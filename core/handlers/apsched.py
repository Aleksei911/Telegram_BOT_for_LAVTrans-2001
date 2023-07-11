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
                     f"Зелёнка до - {car['green_card'][8:10]}.{car['green_card'][5:7]}.{car['green_card'][:4]}\n" \
                     f"Страховка до - {car['strahovka'][8:10]}.{car['strahovka'][5:7]}.{car['strahovka'][:4]}\n" \
                     f"Техосмотр до - {car['tehosmotr'][8:10]}.{car['tehosmotr'][5:7]}.{car['tehosmotr'][:4]}\n" \
                     f"Тахограф до - {car['tahograf'][8:10]}.{car['tahograf'][5:7]}.{car['tahograf'][:4]}\n" \
                     f"Таможенное до - {car['tamogennoye'][8:10]}.{car['tamogennoye'][5:7]}.{car['tamogennoye'][:4]}\n" \
                     f"КАСКО до - {car['kasko'][8:10]}.{car['kasko'][5:7]}.{car['kasko'][:4]}\n" \
                     f"CMR-страховка до - {car['cmr_strahovka'][8:10]}.{car['cmr_strahovka'][5:7]}.{car['cmr_strahovka'][:4]}"
            await bot.send_message(settings.bots.group_id, answer)


async def send_message_driver(bot: Bot):
    await asyncio.sleep(2)
    drivers = await get_driver()
    if drivers:
        await bot.send_message(settings.bots.group_id, 'ВНИМАНИЕ!!!!')
        for driver in drivers:
            answer = f"{driver['last_name']} {driver['name']} {driver['middle_name']}\n" \
                     f"Паспорт до - {driver['passport'][8:10]}.{driver['passport'][5:7]}.{driver['passport'][:4]}\n" \
                     f"Виза до - {driver['visa'][8:10]}.{driver['visa'][5:7]}.{driver['visa'][:4]}\n" \
                     f"Водительское до - {driver['driver_card'][8:10]}.{driver['driver_card'][5:7]}.{driver['driver_card'][:4]}"
            await bot.send_message(settings.bots.group_id, answer)
