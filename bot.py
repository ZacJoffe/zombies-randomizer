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

    # prevent dupes
    if new_map in maps:
        await ctx.send("{} already in map pool!".format(new_map))
    else:
        maps.append(new_map)
        await ctx.send("Added {} to map pool".format(new_map))

@client.command(name='reset')
async def reset(ctx):
    maps[:] = default_maps.copy()
    print(maps)
    await ctx.send("Reset maps to original list")

@client.command(name='pop')
async def reset(ctx):
    # TODO - do not pop original items
    last_map = maps[-1]
    maps.pop()
    print(maps)
    await ctx.send("Removed {} from list".format(last_map))

@client.command(name='remove')
async def reset(ctx, *args):
    map_name = ' '.join(args)

    # TODO - case insensitive
    if not map_name in maps:
        await ctx.send("{} not in list! Nothing to remove".format(map_name))
    else:
        maps.remove(map_name)
        await ctx.send("Removed {} from list".format(map_name))


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
