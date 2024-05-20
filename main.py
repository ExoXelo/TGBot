from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Запуск бота'),
        types.BotCommand(command='/help', description='Help'),
        types.BotCommand(command='/one', description='one'),
        types.BotCommand(command='/two', description='two'),
        types.BotCommand(command='/three', description='three')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('эхо бот')

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer('help')

@dp.message_handler(commands='one')
async def one(message: types.Message):
    await message.answer('one')

@dp.message_handler(commands='two')
async def two(message: types.Message):
    await message.answer('two')

@dp.message_handler(commands='three')
async def three(message: types.Message):
    await message.answer('three')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
