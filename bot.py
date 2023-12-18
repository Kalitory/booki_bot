from aiogram import Bot, Dispatcher
from environs import Env

from hendlers import router


# Создаем глобальный объект бота
env = Env()
env.read_env()
bot = Bot(token=env('BOT_TOKEN'), parse_mode='HTML')
dp = Dispatcher()

# Регистриуем роутеры в диспетчере
dp.include_router(router)


# Функция конфигурирования и запуска бота
async def tg_bot_main():
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
