import asyncio

from bot import tg_bot_main


async def main():

    # запуск tg_bot_main
    await tg_bot_main()


if __name__ == '__main__':
    asyncio.run(main())
