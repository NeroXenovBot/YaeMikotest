# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
HEY_IMG = "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

BAN_GIFS = [
    "https://telegra.ph//file/85ac1ab12c833afa1a5dd.mp4",
]


KICK_GIFS = [
    "https://telegra.ph//file/b4faf6e390d72d286abdf.mp4"
]


MUTE_GIFS = [
    "https://telegra.ph//file/b4faf6e390d72d286abdf.mp4",
]

PM_START_TEXT = "𝘔𝘺 𝘕𝘢𝘮𝘦 𝘐𝘴 𝘠𝘶𝘵𝘢 𝘖𝘬𝘬𝘰𝘵𝘴𝘶 ◎!\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n◍ 𝘐 𝘈𝘮  𝘢 𝘎𝘳𝘰𝘶𝘱 𝘔𝘢𝘯𝘢𝘨𝘦𝘮𝘦𝘯𝘵 𝘉𝘰𝘵 , 𝘉𝘶𝘪𝘭𝘵 𝘣𝘺 𝘞𝘦𝘦𝘣𝘴 𝘧𝘰𝘳 𝘞𝘦𝘦𝘣𝘴 .\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖/n◍ 𝘐 𝘚𝘱𝘦𝘤𝘪𝘢𝘭𝘪𝘻𝘦 𝘐𝘯 𝘔𝘢𝘯𝘢𝘨𝘪𝘯𝘨 𝘈𝘯𝘪𝘮𝘦 𝘊𝘦𝘯𝘵𝘳𝘪𝘤 𝘊𝘰𝘮𝘮𝘶𝘯𝘪𝘵𝘪𝘦𝘴, 𝘩𝘪𝘵 /help 𝘵𝘰 𝘬𝘯𝘰𝘸 𝘮𝘰𝘳𝘦!!"

START_BTN = [
    [
        InlineKeyboardButton(
            text="➕ 𝘼𝙙𝙙 𝙔𝙪𝙩𝙖 𝙏𝙤 𝙈𝙖𝙣𝙖𝙜𝙚 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="💬𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="👾𝘽𝙤𝙩 𝙄𝙣𝙛𝙤", callback_data="Miko_"),
    ],
    [
        InlineKeyboardButton(text="🗿𝘾𝙧𝙚𝙖𝙩𝙤𝙧 ", url=f"https://t.me/xenov7x"),
        InlineKeyboardButton(text="🤖𝘼𝙞 𝙭 𝘾𝙝𝙖𝙩𝙂𝙋𝙏", callback_data="ai_handler"),
    ],
    [
        InlineKeyboardButton(text="⛩ 𝙃𝙚𝙡𝙥 𝙖𝙣𝙙 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ⛩", callback_data="help_back"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="➕ 𝘼𝙙𝙙 𝙔𝙪𝙩𝙖 𝙏𝙤 𝙈𝙖𝙣𝙖𝙜𝙚 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/Yuta_Support"),
        ib(text="SUPPORT", url="https://t.me/SN_BotSupport"),
    ],
    [
        ib(
            text="➕ 𝘼𝙙𝙙 𝙔𝙪𝙩𝙖 𝙏𝙤 𝙈𝙖𝙣𝙖𝙜𝙚 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
⚡ *Yuta Okkotsu* ⚡

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
