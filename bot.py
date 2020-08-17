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

default_bo1_maps = [
    "Kino Der Toten",
    "Five",
    "Ascension",
    "Call of the Dead",
    "Shangri-La",
    "Moon",
    "Nacht der Untoten",
    "Verrückt",
    "Shi No Numa",
    "Der Riese"
]

default_bo2_maps = [
    "TranZit",
    "Nuketown",
    "Die Rise",
    "Mob of the Dead",
    "Buried",
    "Origins"
]

default_bo3_maps = [
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

bo1_maps = default_bo1_maps.copy()
bo2_maps = default_bo2_maps.copy()
bo3_maps = default_bo3_maps.copy()

client = commands.Bot(command_prefix='!')

@client.command(name='map', help='Randomly selects a map from the pool')
async def map(ctx, *args):
    if len(args) == 0:
        await ctx.send(bo3_maps[random.randint(0, len(bo3_maps) - 1)])
    else:
        game = args[0]
        print(game)
        if game == "bo1":
            await ctx.send(bo1_maps[random.randint(0, len(bo1_maps) - 1)])
        elif game == "bo2":
            await ctx.send(bo2_maps[random.randint(0, len(bo2_maps) - 1)])
        elif game == "bo3":
            await ctx.send(bo3_maps[random.randint(0, len(bo3_maps) - 1)])
        else:
            await ctx.send("{} is an invalid argument for this command!".format(game))

# these next commands only work for bo3 since the other games don't have custom
# maps and don't need this functionality
@client.command(name='add', help='Adds a given map to the pool')
async def add(ctx, *args):
    new_map = ' '.join(args)

    # prevent dupes
    if new_map in bo3_maps:
        await ctx.send("{} already in map pool!".format(new_map))
    else:
        bo3_maps.append(new_map)
        await ctx.send("Added {} to map pool".format(new_map))

@client.command(name='reset', help='Resets the pool to the original list of Black Ops 3 maps')
async def reset(ctx):
    bo3_maps[:] = default_bo3_maps.copy()
    print(bo3_maps)
    await ctx.send("Reset maps to original list")

@client.command(name='pop', help='Remove most recently inserted map from pool')
async def reset(ctx):
    # TODO - do not pop original items
    last_map = bo3_maps[-1]
    bo3_maps.pop()
    print(bo3_maps)
    await ctx.send("Removed {} from list".format(last_map))

@client.command(name='remove', help='Remove given map from pool')
async def reset(ctx, *args):
    map_name = ' '.join(args)

    # TODO - case insensitive
    if not map_name in bo3_maps:
        await ctx.send("{} not in list! Nothing to remove".format(map_name))
    else:
        bo3_maps.remove(map_name)
        await ctx.send("Removed {} from list".format(map_name))

@client.command(name='list', help='List the current maps in the pool')
async def list_maps(ctx):
    map_list = "List of the current map pool:"
    for i, v in enumerate(bo3_maps, 1):
        map_list += '\n{}. {}'.format(i, v)

    print(map_list)
    await ctx.send(map_list)

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
