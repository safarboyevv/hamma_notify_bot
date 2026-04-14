import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
TARGET_GROUP = os.getenv("GROUP_CHAT_ID")