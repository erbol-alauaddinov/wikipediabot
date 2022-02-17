# Create by Ebol Alauaddinov
import wikipedia
from config import *
from telegram import *
from telegram.ext import *
from key import *

wikipedia.set_lang("UZ")

def start(update, context):
  name = update.message.from_user.first_name
  id = update.message.from_user.id
  update.message.reply_text(f"<b>Salom <a href='tg://user?id={id}'>{name}</a>\n\n🔍WIKIPEDIA🔎 botga xush kelibsiz!\n\n🖊️Sizga qanday ma'lumot kerak shu yerga yozib qoldiring.</b>", parse_mode="html", reply_markup=key_start)

def menu(update, context):
  call = update.callback_query
  emt = call.edit_message_text
  ca = call.answer
  if call.data == "back":
    name = call.from_user.first_name
    id = call.from_user.id
    ca("🔝Asosiy menu.")
    emt(text=f"<b>Salom <a href='tg://user?id={id}'>{name}</a>\n\nWIKIPEDIA botga xush kelibsiz!\n\n🖊️Sizga qanday ma'lumot kerak shu yerga yozib qoldiring.</b>", parse_mode="html", reply_markup=key_start)

  if call.data == "bots":
    ca("👨‍💻Biz yaratgan botlar")
    emt(text="<b>👨‍💻Biz yaratgan botlar.\n\n@uzkinofilmbot - eng yangi kino va seriallar.\n\n@eWikiBot - Wikipedia bot</b>", parse_mode="html", reply_markup=key_back)
  if call.data == "info":
    ca("🤖Bot haqida.")
    emt(text="<b>🤖Ushbu bot <a href='https://t.me/uzkinofilm'>📹KINO&FILM📹</a> kanaliga tegishli.\n🤖Bot sizga <a href='https://www.wikipedia.org'>WIKIPEDIA</a> saytidan ma'lumot olib beradi</b>", parse_mode="html", reply_markup=key_back)



def wiki(update, context):
  txt = update.message.reply_text
  try:
    txt(wikipedia.summary(update.message.text))
  except:
    txt("<b>❌Uzur malumotlar bazamizdan bunday turdagi malumot topa olmadik</b>", parse_mode="html")

#________HANDLER________#
updater.dispatcher.add_handler(CommandHandler("start", start))

updater.dispatcher.add_handler(CallbackQueryHandler(menu))

updater.dispatcher.add_handler(MessageHandler(Filters.text, wiki))

updater.start_polling()
print("☑️")