from dataclasses import dataclass
from environs import Env

@dataclass
class Tg_Bot:
    token: str
    admin_ids: list

@dataclass
class Config:
    tg_bot: Tg_Bot

def load_config():
    env = Env()
    env.read_env(".env")

    return Config(
        tg_bot=Tg_Bot(
            token=env("BOT_TOKEN"),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        )
    )
