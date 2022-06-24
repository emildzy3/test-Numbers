import logging
from datetime import datetime
import asyncio

from aiogram import Bot, Dispatcher, executor, types

from aiogram.utils.markdown import hitalic, hunderline
from config import token
from aiogram.dispatcher.filters import Text
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dateutil.relativedelta import relativedelta
from getting_delivery_time import delivery_time_check
from setting import TIMEOUT

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome_message(message: types.Message):
    start_buttons = ["Проверить информацию сейчас"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer(text='Добро пожаловать! Здесь работает Ваш личный помощник заказов. Этот бот проверяет срок '
                              'поставки товара из таблицы. Если срок поставки нарушен, бот присылает данные по этому '
                              'заказу. '
                              'Также Вы можете самостоятельно сделать запрос и узнать, у каких товаров истек '
                              'срок поставки. '
                         )
    await message.answer(text='Для начала работы отправьте команду: /start_checking'
                         , reply_markup=keyboard)


@dp.message_handler(commands=['start_checking'])
async def send_welcome_message(message: types.Message):
    while True:
        overdue_orders = delivery_time_check()
        check_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        next_date_check = (datetime.now() + relativedelta(seconds=TIMEOUT)).strftime("%d-%m-%Y %H:%M:%S")
        await message.answer(text=f'Проверка была выполнена в {check_date}. Следующая в {next_date_check}')
        for order in overdue_orders:
            text = f'Заказ №: {order.order_number} \n' \
                   f'{hitalic(f"Планируемый срок поставки:")} {order.delivery_time} \n' \
                   f'{hunderline("Стоимость:")} {order.rubles_value} руб. ({order.dollar_value} $)'
            await message.answer(text=text)
        await asyncio.sleep(TIMEOUT)


@dp.message_handler(Text(equals="Проверить информацию сейчас"))
async def send_welcome_message(message: types.Message):
    overdue_orders = delivery_time_check()
    for order in overdue_orders:
        text = f'Заказ №: {order.order_number} \n' \
               f'{hitalic(f"Планируемый срок поставки:")} {order.delivery_time} \n' \
               f'{hunderline("Стоимость:")} {order.rubles_value} руб. ({order.dollar_value} $)'
        await message.answer(text=text)

if __name__ == '__main__':
    executor.start_polling(dp)
