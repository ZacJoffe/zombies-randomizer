#!/usr/bin/env python3

import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

random.seed()
client = discord.Client()

maps = [
    "Shadows of Evil",
    "The Giant",
    "Der Eisendrache",
    "Zetsubou No Shima",
    "Gorod Krovi",
    "Revelations",
    "Nacht der Untoten",
    "Verrückt",
    "Shi No Numa",
    "Kino Der Toten",
    "Ascension",
    "Shangri-La",
    "Moon",
    "Origins"
]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!map'):
        await message.channel.send(maps[random.randint(0, 13)])


client.run(TOKEN)
