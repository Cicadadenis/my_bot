from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher

from config import TOKEN
import keyboards as kb
import subprocess


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.callback_query_handler(lambda c: c.data == 'button17')
async def process_callback_button11(callback_query: types.CallbackQuery):
   # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 
    "1) разархивировать в диск С:\n \
     2) Запустить CMD от имени Администратора \n\n \
     3) ввести: echo(  C:\Tor\torrc \n\n \
     4) C:\Tor\tor.exe --service install -options -f 'C:\Tor\torrc' \n\n \
     5) C:\Tor\tor.exe --service start \n\n \
     6) Для удаления службы: 1. C:\Tor\tor.exe --service stop 2. C:\Tor\tor.exe --service remove ")
    
@dp.callback_query_handler(lambda c: c.data == 'button14')
async def process_callback_button11(callback_query: types.CallbackQuery):
   # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'У тебя нет доступа к этой фунтции!')

@dp.callback_query_handler(lambda c: c.data == 'button18') 
async def process_callback_button11(callback_query: types.CallbackQuery):
   # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 
    'KFZUS-F3JGV-T95Y7-BXGAS-5NHHP \
     T3ZWQ-P2738-3FJWS-YE7HT-6NA3K \
     KFZUS-F3JGV-T95Y7-BXGAS-5NHHP \
     65Z2L-P36BY-YWJYC-TMJZL-YDZ2S \
     SFZHH-2Y246-Z483L-EU92B-LNYUA \
     GSZVS-5W4WA-T9F2E-L3XUX-68473 \
     6JZUY-32TKX-TK9W7-DU387-9RWKZ')


@dp.callback_query_handler(lambda c: c.data == 'button15')
async def process_callback_button11(callback_query: types.CallbackQuery):
   # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'У тебя нет доступа к этой фунтции!')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("ВЫБЕРИТЕ КНОПКУ", reply_markup=kb.inline_kb_full)



if __name__ == '__main__':
    executor.start_polling(dp)
