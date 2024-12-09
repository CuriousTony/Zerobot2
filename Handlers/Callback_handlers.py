from aiogram.types import Message
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram import Router
from weather import get_weather

router = Router()


@router.message(CommandStart(ignore_case=True))
async def handle_start(message: Message):
    await message.answer('Привет! Отправь мне </погода название города>\n'
                         f'и я пришлю актуальный прогноз погоды')


@router.message(Command('погода', ignore_case=True))
async def forecast(message: Message, command: CommandObject):
    data = command.args.split()
    city = data[0]
    weather_info = await get_weather(city)
    await message.reply(weather_info)


@router.message(Command('help', ignore_case=True))
async def handle_help(message: Message):
    await message.answer('Пока что мне нечем Вам помочь :(')
