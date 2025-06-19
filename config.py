import os
import logging
from dotenv import load_dotenv


logging.basicConfig(
    filename='discord.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    encoding='utf-8'
)

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN not found in environment variables.")
