import asyncio
import datetime
from aiogram import Bot
from core.settings import settings
from .data_fetcher import get_car, get_driver


async def send_message_car(bot: Bot):
    cars = await get_car()
    car_check_day = datetime.date.today() + datetime.timedelta(days=20)
    if cars:
        await bot.send_message(settings.bots.group_id, 'ВНИМАНИЕ!!!!')
        for car in cars:
            answer = f"{car['number']}\n"
            if car['green_card']:
                if datetime.datetime.strptime(car['green_card'], "%Y-%m-%d").date() <= car_check_day:
                    answer += f"Зелёнка до - {car['green_card'][8:10]}.{car['green_card'][5:7]}.{car['green_card'][:4]} !!!\n"
                else:
                    answer += f"Зелёнка до - {car['green_card'][8:10]}.{car['green_card'][5:7]}.{car['green_card'][:4]}\n"
            if car['strahovka']:
                if datetime.datetime.strptime(car['strahovka'], "%Y-%m-%d").date() <= car_check_day:
                    answer += f"Страховка до - {car['strahovka'][8:10]}.{car['strahovka'][5:7]}.{car['strahovka'][:4]} !!!\n"
                else:
                    answer += f"Страховка до - {car['strahovka'][8:10]}.{car['strahovka'][5:7]}.{car['strahovka'][:4]}\n"
            if car['tehosmotr']:
                if datetime.datetime.strptime(car['tehosmotr'], "%Y-%m-%d").date() <= car_check_day:
                    answer += f"Техосмотр до - {car['tehosmotr'][8:10]}.{car['tehosmotr'][5:7]}.{car['tehosmotr'][:4]} !!!\n"
                else:
                    answer += f"Техосмотр до - {car['tehosmotr'][8:10]}.{car['tehosmotr'][5:7]}.{car['tehosmotr'][:4]}\n"
            if car['tahograf']:
                if datetime.datetime.strptime(car['tahograf'], "%Y-%m-%d").date() <= car_check_day:
                    answer += f"Тахограф до - {car['tahograf'][8:10]}.{car['tahograf'][5:7]}.{car['tahograf'][:4]} !!!\n"
                else:
                    answer += f"Тахограф до - {car['tahograf'][8:10]}.{car['tahograf'][5:7]}.{car['tahograf'][:4]}\n"
            if car['tamogennoye']:
                if datetime.datetime.strptime(car['tamogennoye'], "%Y-%m-%d").date() <= car_check_day:
                    answer += f"Таможенное до - {car['tamogennoye'][8:10]}.{car['tamogennoye'][5:7]}.{car['tamogennoye'][:4]} !!!\n"
                else:
                    answer += f"Таможенное до - {car['tamogennoye'][8:10]}.{car['tamogennoye'][5:7]}.{car['tamogennoye'][:4]}\n"
            if car['kasko']:
                if datetime.datetime.strptime(car['kasko'], "%Y-%m-%d").date() <= car_check_day:
                    answer += f"КАСКО до - {car['kasko'][8:10]}.{car['kasko'][5:7]}.{car['kasko'][:4]} !!!\n"
                else:
                    answer += f"КАСКО до - {car['kasko'][8:10]}.{car['kasko'][5:7]}.{car['kasko'][:4]}\n"
            if car['cmr_strahovka']:
                if datetime.datetime.strptime(car['cmr_strahovka'], "%Y-%m-%d").date() <= car_check_day:
                    answer += f"CMR-страховка до - {car['cmr_strahovka'][8:10]}.{car['cmr_strahovka'][5:7]}.{car['cmr_strahovka'][:4]} !!!\n"
                else:
                    answer += f"CMR-страховка до - {car['cmr_strahovka'][8:10]}.{car['cmr_strahovka'][5:7]}.{car['cmr_strahovka'][:4]}\n"
            if car['e100_rb']:
                if datetime.datetime.strptime(car['e100_rb'], "%Y-%m-%d").date() <= car_check_day:
                    answer += f"Топливная карта Е100 РБ до - {car['e100_rb'][8:10]}.{car['e100_rb'][5:7]}.{car['e100_rb'][:4]} !!!\n"
                else:
                    answer += f"Топливная карта Е100 РБ до - {car['e100_rb'][8:10]}.{car['e100_rb'][5:7]}.{car['e100_rb'][:4]}\n"
            if car['e100_rf']:
                if datetime.datetime.strptime(car['e100_rf'], "%Y-%m-%d").date() <= car_check_day:
                    answer += f"Топливная карта Е100 РФ до - {car['e100_rf'][8:10]}.{car['e100_rf'][5:7]}.{car['e100_rf'][:4]} !!!"
                else:
                    answer += f"Топливная карта Е100 РФ до - {car['e100_rf'][8:10]}.{car['e100_rf'][5:7]}.{car['e100_rf'][:4]}"

            await asyncio.sleep(3)

            await bot.send_message(settings.bots.group_id, answer)


async def send_message_driver(bot: Bot):
    await asyncio.sleep(90)
    drivers = await get_driver()
    driver_check_day = datetime.date.today() + datetime.timedelta(days=30)
    if drivers:
        await bot.send_message(settings.bots.group_id, 'ВНИМАНИЕ!!!!')
        for driver in drivers:
            answer = f"{driver['last_name']} {driver['name']} {driver['middle_name']}\n"
            if driver['passport']:
                if datetime.datetime.strptime(driver['passport'], "%Y-%m-%d").date() <= driver_check_day:
                    answer += f"Паспорт до - {driver['passport'][8:10]}.{driver['passport'][5:7]}.{driver['passport'][:4]} !!!\n"
                else:
                    answer += f"Паспорт до - {driver['passport'][8:10]}.{driver['passport'][5:7]}.{driver['passport'][:4]}\n"
            if driver['visa']:
                if datetime.datetime.strptime(driver['visa'], "%Y-%m-%d").date() <= driver_check_day:
                    answer += f"Виза до - {driver['visa'][8:10]}.{driver['visa'][5:7]}.{driver['visa'][:4]} !!!\n"
                else:
                    answer += f"Виза до - {driver['visa'][8:10]}.{driver['visa'][5:7]}.{driver['visa'][:4]}\n"
            if driver['driver_card']:
                if datetime.datetime.strptime(driver['driver_card'], "%Y-%m-%d").date() <= driver_check_day:
                    answer += f"Водительское до - {driver['driver_card'][8:10]}.{driver['driver_card'][5:7]}.{driver['driver_card'][:4]} !!!\n"
                else:
                    answer += f"Водительское до - {driver['driver_card'][8:10]}.{driver['driver_card'][5:7]}.{driver['driver_card'][:4]}\n"
            if driver['mezhdunarodnik']:
                if datetime.datetime.strptime(driver['mezhdunarodnik'], "%Y-%m-%d").date() <= driver_check_day:
                    answer += f"Квалификационная карточка водителя (международник) до - {driver['mezhdunarodnik'][8:10]}.{driver['mezhdunarodnik'][5:7]}.{driver['mezhdunarodnik'][:4]} !!!\n"
                else:
                    answer += f"Квалификационная карточка водителя (международник) до - {driver['mezhdunarodnik'][8:10]}.{driver['mezhdunarodnik'][5:7]}.{driver['mezhdunarodnik'][:4]}\n"
            if driver['chip']:
                if datetime.datetime.strptime(driver['chip '], "%Y-%m-%d").date() <= driver_check_day:
                    answer += f"Карта водителя (ЧИП) до - {driver['chip '][8:10]}.{driver['chip '][5:7]}.{driver['chip '][:4]} !!!\n"
                else:
                    answer += f"Карта водителя (ЧИП) до - {driver['chip '][8:10]}.{driver['chip '][5:7]}.{driver['chip '][:4]}\n"
            if driver['adr']:
                if datetime.datetime.strptime(driver['adr'], "%Y-%m-%d").date() <= driver_check_day:
                    answer += f"Свидетельство ДОПОГ (ADR) до - {driver['adr'][8:10]}.{driver['adr'][5:7]}.{driver['adr'][:4]} !!!\n"
                else:
                    answer += f"Свидетельство ДОПОГ (ADR) до - {driver['adr'][8:10]}.{driver['adr'][5:7]}.{driver['adr'][:4]}\n"
            if driver['doverennost_rus']:
                if datetime.datetime.strptime(driver['doverennost_rus'], "%Y-%m-%d").date() <= driver_check_day:
                    answer += f"Доверенность ООО ЛАВТРАНС-2001 РУС до - {driver['doverennost_rus'][8:10]}.{driver['doverennost_rus'][5:7]}.{driver['doverennost_rus'][:4]} !!!\n"
                else:
                    answer += f"Доверенность ООО ЛАВТРАНС-2001 РУС до - {driver['doverennost_rus'][8:10]}.{driver['doverennost_rus'][5:7]}.{driver['doverennost_rus'][:4]}\n"
            if driver['doverennost_lt']:
                if datetime.datetime.strptime(driver['doverennost_lt'], "%Y-%m-%d").date() <= driver_check_day:
                    answer += f"Доверенность ЧТУП ЛАВТранс-2001 до - {driver['doverennost_lt'][8:10]}.{driver['doverennost_lt'][5:7]}.{driver['doverennost_lt'][:4]} !!!\n"
                else:
                    answer += f"Доверенность ЧТУП ЛАВТранс-2001 до - {driver['doverennost_lt'][8:10]}.{driver['doverennost_lt'][5:7]}.{driver['doverennost_lt'][:4]}\n"
            if driver['doverennost_mul']:
                if datetime.datetime.strptime(driver['doverennost_mul'], "%Y-%m-%d").date() <= driver_check_day:
                    answer += f"Доверенность ООО МУЛЬТИЛАЙН до - {driver['doverennost_mul'][8:10]}.{driver['doverennost_mul'][5:7]}.{driver['doverennost_mul'][:4]} !!!"
                else:
                    answer += f"Доверенность ООО МУЛЬТИЛАЙН до - {driver['doverennost_mul'][8:10]}.{driver['doverennost_mul'][5:7]}.{driver['doverennost_mul'][:4]}"
            await bot.send_message(settings.bots.group_id, answer)
