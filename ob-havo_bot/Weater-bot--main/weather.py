from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_menu = InlineKeyboardMarkup(
    inline_keyboard= [

    {InlineKeyboardButton(text="Navoiy",callback_data="navoiy"),
    InlineKeyboardButton(text="Fargona",callback_data="fargona"),},

    {InlineKeyboardButton(text="Vobkent",callback_data="vobkent"),
    InlineKeyboardButton(text="Andijon",callback_data="andijon")},

    {InlineKeyboardButton(text="Jizzax",callback_data="jizzax"),
    InlineKeyboardButton(text="Qarshi",callback_data="qarshi")},
    {InlineKeyboardButton(text="Buxoro",callback_data="buxoro"),
    InlineKeyboardButton(text="Namangan",callback_data="namangan")},
    {InlineKeyboardButton(text="Qashqadaryo",callback_data="qashqdaryo"),
    InlineKeyboardButton(text="Sirdaryo",callback_data="sirdaryo")},
    {InlineKeyboardButton(text="Surxandaryo",callback_data="surxandaryo"),
    InlineKeyboardButton(text="Samarqand",callback_data="samarqand")},
    {InlineKeyboardButton(text="Xorazim",callback_data="xorazim"),
     InlineKeyboardButton(text="Qaraqalpoqiston",callback_data="qaraqalpoq")},
    ]
    


)

uchir = InlineKeyboardMarkup(
    inline_keyboard= [

    {InlineKeyboardButton(text="🔙orqaga",callback_data="🔙ortga")},

    ]
    


)


 