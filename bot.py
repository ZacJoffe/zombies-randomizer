#!/usr/bin/env python3

import os
import random
from dotenv import load_dotenv
from discord.ext import commands

# load .env file if exists
# DISCORD_TOKEN env var is set as a config var within Heroku
load_dotenv() 
TOKEN = os.getenv('DISCORD_TOKEN')

random.seed()

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

@client.command(name='map', help='Randomly selects a map from the pool')
async def map(ctx):
    print(maps)
    await ctx.send(maps[random.randint(0, len(maps) - 1)])

@client.command(name='add', help='Adds a given map to the pool')
async def add(ctx, *args):
    new_map = ' '.join(args)

    # prevent dupes
    if new_map in maps:
        await ctx.send("{} already in map pool!".format(new_map))
    else:
        maps.append(new_map)
        await ctx.send("Added {} to map pool".format(new_map))

@client.command(name='reset', help='Resets the pool to the original list of Black Ops 3 maps')
async def reset(ctx):
    maps[:] = default_maps.copy()
    print(maps)
    await ctx.send("Reset maps to original list")

@client.command(name='pop', help='Remove most recently inserted map from pool')
async def reset(ctx):
    # TODO - do not pop original items
    last_map = maps[-1]
    maps.pop()
    print(maps)
    await ctx.send("Removed {} from list".format(last_map))

@client.command(name='remove', help='Remove given map from pool')
async def reset(ctx, *args):
    map_name = ' '.join(args)

    # TODO - case insensitive
    if not map_name in maps:
        await ctx.send("{} not in list! Nothing to remove".format(map_name))
    else:
        maps.remove(map_name)
        await ctx.send("Removed {} from list".format(map_name))

@client.command(name='list', help='List the current maps in the pool')
async def list_maps(ctx):
    map_list = "List of the current map pool:"
    for i, v in enumerate(maps, 1):
        map_list += '\n{}. {}'.format(i, v)

    print(map_list)
    await ctx.send(map_list)

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')


client.run(TOKEN)
