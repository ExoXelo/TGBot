from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keybaords import get_keyboard_1, get_keyboard_2
from keyboard.KeyInline import get_keyboard_inline


bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Запуск бота'),
        types.BotCommand(command='/help', description='Help'),
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('эхо бот', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://img.razrisyika.ru/kart/132/1200/526072-tolstyy-kotik-26.jpg', caption= 'ля какой', reply_markup= get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Перейти на некст клаву')
async def button_2_click(message: types.Message):
    await message.answer('Перейти на некст клаву', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://www.nairaland.com/attachments/14131018_images65_jpeg_jpeg4a48023df950c430bd5f8313a4f51b09', caption= 'Прикол')

@dp.message_handler(lambda message: message.text == 'На прошлую клаву')
async def button_2_click(message: types.Message):
    await message.answer('На прошлую клаву', reply_markup= get_keyboard_1())
async def start(message: types.Message):
    await message.answer('эхо бот', reply_markup= get_keyboard_1())

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
