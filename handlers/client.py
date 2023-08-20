import time

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup
from create_bot import bot


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])

