from jinja2 import Environment, FileSystemLoader
from classes.Broadcaster import Broadcaster
from classes.templates import Templates
from classes.Keyboard import Keyboard
from aiogram import Bot, Dispatcher
from classes.db import DB
import logging
import asyncio
import os


strfmt = '[%(asctime)s] | [%(name)s] | [%(levelname)s] | %(message)s'

datefmt = '%Y-%m-%d %H:%M:%S'

logging.basicConfig(level=logging.INFO, format=strfmt, datefmt=datefmt)
log = logging.getLogger('init')


loop = asyncio.get_event_loop()


log.info('Including the database in the solution')
db = DB('baseDate')


log.info('Including the Keyboard in the solution')
Keyboards = Keyboard()


log.info('Including the Environment in the solution')
env = Environment(loader=FileSystemLoader('text_templates'), trim_blocks=True)


bot = Bot(os.environ.get('TOKEN'))
dp = Dispatcher(bot)


log.info('Including the Templates in the solution')
temp = Templates(bot, env)


log.info('Including the Broadcaster in the solution')
broadcaster = Broadcaster(bot, db, loop, Keyboards, temp)