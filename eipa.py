import os
import discord
import requests
from dotenv import load_dotenv
from random import randint

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CAT = os.getenv("CAT_API")

client = discord.Client()

class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("祝你有好的一天!")
        await client.change_presence(status=discord.Status.online, activity=game)

        print("ready")

    async def on_message(self, message):
        if message.author.bot:
            return None

    async def on_message(self, message):
        if "!meow" in message.content:
            data = requests.get('https://api.thecatapi.com/v1/images/search?size=small',
                                headers={"X-API-KEY": CAT}).json()
            await message.channel.send(data[0]["url"])

        if '!eipa' in str(message.content):
            num = randint(0, 31)
            List = open("pos.txt").readlines()
            channel = message.channel
            msg = "**" + List[num] + "**"
            await channel.send(msg)
            return None

        if message.author.id == 736233390923186307:
            num2 = randint(0, 14)
            List2 = open("pos2.txt", encoding="utf8").readlines()
            channel = message.channel
            msg = List2[num2]
            await channel.send(msg)
            return None

client = chatbot()
client.run(TOKEN)
