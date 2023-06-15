import logging
from aiogram import Bot, Dispatcher, executor, types
from keyb import kb
from func import *

API_TOKEN = '5507458293:AAGLe4Pgnfx7WUSgQeSE1NWP1f31HsQaZIE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='markdown')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    stp.write(message.chat.id)
    await message.answer("🌸[ ](https://telegra.ph/file/06bef4a756add9b85d451.jpg)* Salom \n\nMen orqali o'z imsingiz bosh harfi yozilgan taqinchoqlar rasmini tayyorlay olasiz\n\nQuyidagi menyulardan birini tanlang*", reply_markup=kb.main())


@dp.callback_query_handler(lambda call: call.data == "birlik")
async def callback(call:types.CallbackQuery):
    cat = "birlik"
    s = "1"
    await call.message.delete()
    await call.message.answer_photo(photos[cat][s], "Kerakli rasmni tanlang", reply_markup=kb.catgory(cat, s, len(photos[cat])))

@dp.callback_query_handler(lambda call: call.data == "juftlik")
async def callback(call:types.CallbackQuery):
    cat = "juftlik"
    s = "1"
    await call.message.delete()
    await call.message.answer_photo(photos[cat][s], "Kerakli rasmni tanlang", reply_markup=kb.catgory(cat, s, len(photos[cat])))


@dp.callback_query_handler(lambda call: call.data.split('|')[0] == "back")
async def callback(call:types.CallbackQuery):
    com, cat, s =  call.data.split('|')
    s = str(int(s) - 1)
    try:
        await bot.edit_message_media(media=types.InputMedia(type='photo', media=photos[cat][s], caption = "Kerakli rasmni tanlang"), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=kb.catgory(cat, s, len(photos[cat])))
    except:
        await call.answer("Bu bosh sahifa", True)

@dp.callback_query_handler(lambda call: call.data.split('|')[0] == "next")
async def callback(call:types.CallbackQuery):
    com, cat, s =  call.data.split('|')
    s = str(int(s) + 1)
    try:
        await bot.edit_message_media(media=types.InputMedia(type='photo', media=photos[cat][s], caption = "Kerakli rasmni tanlang"), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=kb.catgory(cat, s, len(photos[cat])))
    except:
        await call.answer("Bu oxirgi sahifa", True)

@dp.callback_query_handler(lambda call: call.data.split('|')[0] == "select")
async def callback(call:types.CallbackQuery):
    stp.write(call.message.chat.id, call.data)
    try:
        await call.message.delete()
        await call.message.answer("*Ismingizni bosh harfini kiriting*")
    except:
        await call.answer("Qandaydir xatolik yuz berdi", True)

@dp.message_handler(lambda message: stp.read(message.chat.id)[0]=="select")
async def send_welcome(message: types.Message):
    com, cat, s = stp.read(message.chat.id)
    photo  = make_photo(cat, s, message.chat.id, message.text)
    if photo != None:
        await message.answer_photo(open(photo, 'rb'), "*Buyurtmangiz tayyor boldi.\n\n\nQayta ishlatish uchun /start bosing*")
    else:
        await message.answer("Qandaydir xatolik yuz berdi")


@dp.callback_query_handler(lambda call: call.data.split('|')[0] == "slcj")
async def callback(call:types.CallbackQuery):
    stp.write(call.message.chat.id, call.data)
    try:    
        await call.message.delete()
        await call.message.answer("*Ikki insonning ismini + belgisi bilan qo'shib yozib jo'nating\n\nMasalan E+M*")
    except:
        await call.answer("Qandaydir xatolik yuz berdi", True)

@dp.message_handler(lambda message: stp.read(message.chat.id)[0]=="slcj")
async def send_welcome(message: types.Message):
    com, cat, s = stp.read(message.chat.id)
    photo  = make_photo(cat, s, message.chat.id, message.text)
    if '+' in message.text and len(message.text)==3:
        if photo != None:
            await message.answer_photo(open(photo, 'rb'), "Buyurtmangiz tayyor boldi.\n\n\nQayta ishlatish uchun /start bosing")
        else:
            await message.answer("Qandaydir xatolik yuz berdi")
    else:
        await message.answer("Ikki insonning ismini + belgisi bilan qo'shib yozib jo'natingn\nMasalan E+M")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)