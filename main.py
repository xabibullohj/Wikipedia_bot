from config import API_TOKEN,CHANNELS
from aiogram import Bot, Dispatcher, executor, types
import wikipedia as wk
import obuna
from button import check_button


wk.set_lang("uz")

bot=Bot(token=API_TOKEN)
ab=Dispatcher(bot)



@ab.message_handler(commands=["start", "help"])
async def start(message: types.Message):
    channels_format = str()
    fullname=message.from_user.full_name
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        #logging.info(invite_link)
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"
    await message.answer(f"Assalomu aleykum {fullname}. Botdan foydalanish uchun , quyidagi kanallarga obuna bo'ling: \n"f"{channels_format}", reply_markup=check_button, disable_web_page_preview=True, parse_mode ='HTML')
  





@ab.callback_query_handler(text="chek_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await obuna.check(user_id=call.from_user.id, channel=channel)


        channe1 = await bot.get_channel(channel)
        if status:
            result+=f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        else:
            invite_link=await channel.export_invite_link()
            results







@ab.message_handler()
async def wiki(message: types.Message):
    try:
        manba=wk.summary(message.text)
        await message.answer(manba)
    except:
        await message.answer("Bunday ma'lumot yo'q")









if __name__ == '__main__':
    executor.start_polling(ab)

