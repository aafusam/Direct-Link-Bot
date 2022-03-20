
from pyrogram import Client
from ..vars import Var

StreamBot = Client(
    session_name='WebStreamer',
    api_id= str(getenv('16641929')),
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)
