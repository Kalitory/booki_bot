from aiogram import Bot, Dispatcher

from config import Config, load_config
from hendlers import router

# Создаем глобальный объект бота
config: Config = load_config()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher()

# Регистриуем роутеры в диспетчере
dp.include_router(router)


# Функция конфигурирования и запуска бота
async def tg_bot_main():
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
