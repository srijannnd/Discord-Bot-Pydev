"""
    BotClient Model to handle all events and communications.
"""
import discord
from models.message_model import Message


class BotClient(discord.Client):
    async def on_ready(self):
        print('Discord Client is running as {client}'.format(client=self.user.name))

    async def on_message(self, message):
        message_obj = Message(msg_client=message, user=self.user)
        await message_obj.send_response()
