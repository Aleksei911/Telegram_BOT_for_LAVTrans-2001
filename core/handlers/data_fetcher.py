import aiohttp
from core.settings import settings


async def get_car():
    async with aiohttp.ClientSession() as session:
        async with session.get(settings.bots.cars_api_url) as response:
            return await response.json()


async def get_driver():
    async with aiohttp.ClientSession() as session:
        async with session.get(settings.bots.drivers_api_url) as response:
            return await response.json()
