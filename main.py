from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.handlers.basic import get_start
from core.settings import settings
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers import apsched
from datetime import datetime
import asyncio
import logging


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='work')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='don`t work')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token)
    dp = Dispatcher()

    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(apsched.send_message_car, trigger='cron', hour='09',
                      minute='00', start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.add_job(apsched.send_message_driver, trigger='cron', hour='09',
                      minute='00', start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.start()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
