import asyncio
import json
import os
import random
from datetime import datetime, timezone

import colorama
import discord
from colorama import Fore
from pathlib import Path
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, check
from discord.ext.commands import CheckFailure, check


class MissingPermissions(CheckFailure): pass


def has_permissions(**perms):
    def predicate(ctx):
        msg = ctx.message
        ch = msg.channel
        permissions = ch.permissions_for(msg.author)
        if all(getattr(permissions, perm, None) == value for perm, value in perms.items()):
            return True
        raise MissingPermissions()

    return check(predicate)


def get_prefix(client, message):
    with open('config.json', 'r') as f:
        config = json.load(f)

    return config["prefix"]


settings = json.loads(open("./config.json").read())
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=False)
client = commands.Bot(get_prefix, case_insensitive=True, intents=intents, self_bot=True)
color = 0x2f3137
client.remove_command('help')

with open('config.json') as f:
    config = json.load(f)
    token = config.get('token')
    prefix = config.get('prefix')

colorama.init()

# Status
@client.event
async def on_ready():
    # await client.change_presence(activity=discord.Streaming(name="with the homies", url="https://twitch.tv/develop"))
    print(f'''{Fore.LIGHTBLUE_EX}
 .------.
(        )    ..
 `------'   .' /
      O    /  ;
        o i  OO
         C    `-.
         |    <-'
         (  ,--.
          V  \\_)
           \\  :
            `._\\.
            {Fore.LIGHTBLUE_EX}Prefix: {Fore.WHITE}{prefix}
            {Fore.WHITE}Online.
            {Fore.LIGHTBLUE_EX}{client.user.name}
    ''' + Fore.RESET)

    @client.command()
    async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')

    @client.command()
    async def unload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
async def stream(ctx, *, message):
        await ctx.message.delete()
        stream = discord.Streaming(
            name=message,
            url="https://www.twitch.tv/moon",
        )
        await client.change_presence(activity=stream)


@client.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass 


@client.command()
async def embed(ctx, *, content: str):
    await ctx.message.delete()
    title, description = content.split('|')
    embed = discord.Embed(title=title, description=description, color=color)
    await ctx.send(embed=embed)


@client.command()
async def bot(ctx):
    my_embed = discord.Embed(color=color)

    my_embed.set_author(name="Self Bot Info")

    my_embed.add_field(name="Version Code:\n", value="v0.1", inline=False)

    my_embed.add_field(name="Released On:", value="November 2020", inline=False)

    my_embed.add_field(name="Servers", value=len(client.guilds))

    my_embed.add_field(name="Website",
                       value=f"[web](https://bye.lol)",)

    my_embed.add_field(name="Download Self Bot",
                       value=f"[Click Here!](https://discord.com/api/oauth2/authorize?client_id=771697308458811434&permissions=8&scope=bot)",
                       inline=False)

    my_embed.set_footer(text="star bot")
    my_embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.message.channel.send(embed=my_embed)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send("you don't have perms to use this command :(")


def getstatus(m):
    if str(m.status) == "dnd":
        return "do not disturb"
    return m.status


client.run(token, bot=False)
