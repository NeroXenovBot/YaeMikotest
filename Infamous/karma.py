# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/f2944fa1c6206a7e446b7.jpg",
    "https://telegra.ph/file/ad1ab43fa6b423f8f40ed.jpg",
    "https://telegra.ph/file/df9dbbcdd7e2146f45cb2.jpg",
    "https://telegra.ph/file/956d23eef999d37f9e2fe.jpg",
    "https://telegra.ph/file/82d45e1805d601818eb6c.jpg",
    
]

HEY_IMG = "https://telegra.ph/file/df9dbbcdd7e2146f45cb2.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph/file/8749171543f603664546b.mp4",
    "https://telegra.ph/file/05bb011744f84bffae52d.mp4",
    
]

BAN_GIFS = [
    "https://telegra.ph//file/85ac1ab12c833afa1a5dd.mp4",
]


KICK_GIFS = [
    "https://tenor.com/BBLQlTQBCZ.gif",
]


MUTE_GIFS = [
    "https://tenor.com/bAdFP.gif",
]

FIRST_PART_TEXT = "⚡ *Hey There!!* {} . . ."

PM_START_TEXT = [
    "────「 <a href="https://t.me/yuta_xbot">Yuta Okkotsu</a> 」────\nMy Name Is Yuta Okkotsu ◎!\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n◍ I Am  a Group Management Bot , Built by Weebs for Weebs .\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n◍ I Specialize In Managing Anime Centric Communities, hit /help to know more!!"
    ]

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
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
        ib(text="UPDATES", url="https://t.me/Hydra_Updates"),
        ib(text="SUPPORT", url="https://t.me/hydraXsupport"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Yae-Miko* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
