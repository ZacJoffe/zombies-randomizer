#!/usr/bin/env python3

import os
# import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

random.seed()
# client = discord.Client()

default_maps = [
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

maps = default_maps.copy()

client = commands.Bot(command_prefix='!')
# bot = commands.Bot(command_prefix='!')

@client.command(name='map')
async def map(ctx):
    print(maps)
    await ctx.send(maps[random.randint(0, len(maps) - 1)])

@client.command(name='add')
async def add(ctx, *args):
    new_map = ' '.join(args)
    maps.append(new_map)
    await ctx.send("Added {} to map pool".format(new_map))

@client.command(name='reset')
async def reset(ctx):
    maps[:] = default_maps.copy()
    print(maps)
    await ctx.send("Reset maps to original list")

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('!map'):
#         await message.channel.send(maps[random.randint(0, len(maps) - 1)])

#     if message.content.startswith('!moss'):
#         await message.channel.send("Nacht der Untoten")

#     if message.content.startswith('!add'):
#         await message.channel.send(maps[random.randint(0, len(maps) - 1)])

#     if message.content.startswith('!reset'):
#         default_maps = maps


client.run(TOKEN)
