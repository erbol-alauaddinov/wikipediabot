from telegram import *
from config import admin
key_start = InlineKeyboardMarkup([[InlineKeyboardButton("🤖BOTLAR🤖", callback_data="bots"), InlineKeyboardButton("❗INFO❗", callback_data="info")], [InlineKeyboardButton("👨‍💻ADMIN👨‍💻", url=f"https://t.me/{admin}")]])
key_back = InlineKeyboardMarkup([[InlineKeyboardButton("🔙ORTGA🔙", callback_data="back")]])