import asyncio
import logging
from bot_giblets import bot, dp
from Handlers import Callback_handlers

dp.include_router(Callback_handlers.router)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    asyncio.run(main())
