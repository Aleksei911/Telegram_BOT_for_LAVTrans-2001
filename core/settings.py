from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int
    group_id: int
    cars_api_url: str
    drivers_api_url: str


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str('TOKEN'),
            admin_id=env.int('ADMIN_ID'),
            group_id=env.int('GROUP_ID'),
            cars_api_url=env.str('CARS_API_URL'),
            drivers_api_url=env.str('DRIVER_API_URL')
        )
    )


settings = get_settings('input')
