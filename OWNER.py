import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

OWNER = ["V_K_Z"]
OWNER_NAME = " 𝗥͜𝗼͡𝗪͡𝗲͜𝗦 "
BOT_TOKEN = getenv("BOT_TOKEN")
DATABASE = getenv("MONGO_DB_URI", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
CHANNEL = "https://t.me/zxxlz"
GROUP = "https://t.me/qkpqp"
VID_SO = "https://graph.org/file/510a7702f5400271266fa.jpg"
PHOTO ="https://graph.org/file/510a7702f5400271266fa.jpg"
LOGS = "elzoz"
