"""
    run.py worker. Execute this file to start the Discord bot server.
"""
from app_settings import DISCORD_TOKEN
from models.client_model import BotClient


bot_client = BotClient()

bot_client.run(DISCORD_TOKEN)
