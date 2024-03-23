from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,InlineKeyboardButton
from data import config
import asyncio
import logging
import sys
from menucommands.set_bot_commands  import set_default_commands
from baza.sqlite import Database
from filters.admin import IsBotAdminFilter
from filters.check_sub_channel import IsCheckSubChannels
from keyboard_buttons import admin_keyboard
from aiogram.fsm.context import FSMContext #new
from states.reklama import Adverts
from aiogram.utils.keyboard import InlineKeyboardBuilder
import time 
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.types import Message,CallbackQuery
from weather import inline_menu,uchir
import requests
from bs4 import BeautifulSoup as BS
ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS

dp = Dispatcher()




@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text="Assalomu alaykum, ob-havo botimizga xush kelibsiz ⛅️ \nShaharni tanlang!", reply_markup=inline_menu)
    except:
        await message.answer(text="Assalomu alaykum, ob-havo botimizga xush kelibsiz ⛅️ \nShaharni tanlang!",reply_markup=inline_menu)


@dp.message(IsCheckSubChannels())
async def kanalga_obuna(message:Message):
    text = ""
    inline_channel = InlineKeyboardBuilder()
    for index,channel in enumerate(CHANNELS):
        ChatInviteLink = await bot.create_chat_invite_link(channel)
        inline_channel.add(InlineKeyboardButton(text=f"{index+1}-kanal",url=ChatInviteLink.invite_link))
    inline_channel.adjust(1,repeat=True)
    button = inline_channel.as_markup()
    await message.answer(f"{text} kanallarga azo bo'ling",reply_markup=button)



#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("Shu bot ob-havo boti")



#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Men Tuxtapulatov Sardor 2024 - yil ushbu botni yaratdim \n<a href='https://www.instagram.com/sardortme/'>Instagram</a>\n<a href='https://t.me/Sardor_Tuxtapulatov'>Telegram</a>")


@dp.message(Command("admin"),IsBotAdminFilter(ADMINS))
async def is_admin(message:Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)


@dp.message(F.text=="Foydalanuvchilar soni",IsBotAdminFilter(ADMINS))
async def users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

@dp.message(F.text=="Reklama yuborish",IsBotAdminFilter(ADMINS))
async def advert_dp(message:Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")

@dp.message(Adverts.adverts)
async def send_advert(message:Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()


city = {"Navoiy":"погода-навои","Fargona":"погода-фергана","Vobkent":"погода-баткен","Andijon":"погода-андижан","Jizzax":"погода-джизак","Qarshi":"погода-карши","Buxoro":"погода-бухара","Namangan":"погода-наманган","Qashqadaryo":"погода-карши","Sirdaryo":"/погода-термез","Surxandaryo":"погода-термез","Samarqand":"погода-самарканд","Xorazim":"погода-ургенч","Qaraqalpoqiston":"погода-нукус"}
# boshqa viloyatlarni xam qo'shish kerak. Aiogram botga ulash kerak 


@dp.callback_query(F.data=="navoiy")
async def navoiy_harorat(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    navoiy = ob_havo(city=city.get("Navoiy"))
    await callback.message.edit_text(text=f"Navoiy: {navoiy}",reply_markup=uchir)    

@dp.callback_query(F.data=="fargona")
async def fargona_xarorat(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    fargona = ob_havo(city=city.get("Fargona"))
    await callback.message.edit_text(text=f"Fargona: {fargona}",reply_markup=uchir)    

@dp.callback_query(F.data=="vobkent")
async def vobkent_harorat(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    vobkent = ob_havo(city=city.get("Vobkent"))
    await callback.message.edit_text(text=f"Vobkent: {vobkent}",reply_markup=uchir)   

@dp.callback_query(F.data=="andijon")
async def andijon_harorati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    andijon = ob_havo(city=city.get("Andijon"))
    await callback.message.edit_text(text=f"Andijon: {andijon}",reply_markup=uchir)

@dp.callback_query(F.data=="jizzax")
async def jizzax_haroati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    jizzax = ob_havo(city=city.get("Jizzax"))
    await callback.message.edit_text(text=f"Jizzax: {jizzax}",reply_markup=uchir)  

@dp.callback_query(F.data=="qarshi")
async def qarshi_harorati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    qarshi = ob_havo(city=city.get("Qarshi"))
    await callback.message.edit_text(text=f"Qarshi: {qarshi}",reply_markup=uchir)           

@dp.callback_query(F.data=="buxoro")
async def qarshi_harorati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    Qoraqalpoqistoni = ob_havo(city=city.get("Buxoro"))
    await callback.message.edit_text(text=f"Buxoro: {Qoraqalpoqistoni}",reply_markup=uchir)    

@dp.callback_query(F.data=="namangan")
async def qarshi_harorati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    Qoraqalpoqistonh = ob_havo(city=city.get("Namangan"))
    await callback.message.edit_text(text=f"Namangan: {Qoraqalpoqistonh}",reply_markup=uchir)           
       
@dp.callback_query(F.data=="qashqdaryo")
async def qarshi_harorati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    qashqa = ob_havo(city=city.get("Qashqadaryo"))
    await callback.message.edit_text(text=f"Qashqadaryo: {qashqa}",reply_markup=uchir)           
       
@dp.callback_query(F.data=="sirdaryo")
async def qarshi_harorati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    sirdaryo = ob_havo(city=city.get("Sirdaryo"))
    await callback.message.edit_text(text=f"Sirdaryo: {sirdaryo}",reply_markup=uchir)   

@dp.callback_query(F.data=="surxandaryo")
async def qarshi_harorati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    surxon = ob_havo(city=city.get("Surxandaryo"))
    await callback.message.edit_text(text=f"Surxandaryo: {surxon}",reply_markup=uchir)   

@dp.callback_query(F.data=="samarqand")
async def qarshi_harorati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max
        

    samarqand = ob_havo(city=city.get("Samarqand"))
    await callback.message.edit_text(text=f"Samarqand: {samarqand}",reply_markup=uchir)   

@dp.callback_query(F.data=="xorazim")
async def qarshi_harorati(callback:CallbackQuery):


    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    xorazm = ob_havo(city=city.get("Xorazim"))
    await callback.message.edit_text(text=f"Xorazim: {xorazm}",reply_markup=uchir)   

@dp.callback_query(F.data=="qaraqalpoq")
async def qarshi_harorati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    xorazm = ob_havo(city=city.get("Qaraqalpoqiston"))
    await callback.message.edit_text(text=f"Qaraqalpoqiston: {xorazm}",reply_markup=uchir)   


@dp.callback_query(F.data=="ortga")
async def qaytar(callback:CallbackQuery):
    await callback.message.edit_text(text="Assalomu alaykum bu ob hafo boti",reply_markup=inline_menu)




@dp.startup()
async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)

#bot ishga tushganini xabarini yuborish
@dp.shutdown()
async def off_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishdan to'xtadi!")
        except Exception as err:
            logging.exception(err)


def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    from middlewares.throttling import ThrottlingMiddleware

    # Spamdan himoya qilish uchun klassik ichki o'rta dastur. So'rovlar orasidagi asosiy vaqtlar 0,5 soniya
    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))



async def main() -> None:
    global bot,db
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    db = Database(path_to_db="main.db")
    db.create_table_users()
    # db.create_table_audios()
    await set_default_commands(bot)
    await dp.start_polling(bot)
    setup_middlewares(dispatcher=dp, bot=bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    asyncio.run(main())