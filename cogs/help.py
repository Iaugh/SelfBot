import discord
import json
import requests
import asyncio
import os
import datetime
import random
from discord.ext import commands

color = 0x2f3137


class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Help
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="`Commands`", color=color, inline=True)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="`Info`", value="*Check Info Commands*", inline=False)
        embed.add_field(name="`Fun`", value="*Check Fun Commands*", inline=False)
        embed.add_field(name="`User`", value="*Check User Commands*", inline=False)
        embed.add_field(name="`Nsfw`", value="*Check Nsfw Commands*", inline=False)


        embed.set_footer(text='𝙝𝙚𝙡𝙥 𝙘𝙖𝙩𝙚𝙜𝙤𝙧𝙞𝙚𝙨')
        await ctx.send(embed=embed)

    @commands.command()
    async def fun(self, ctx):
        embed = discord.Embed(title="`Fun`", color=color, inline=True)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="`dog`", value="*Gives you a random dog image ʕ•́ᴥ•̀ʔっ*", inline=False)
        embed.add_field(name="`kiss`", value="*Kiss someone <3*", inline=False)
        embed.add_field(name="`hug`", value="*Hug someone ^.^*", inline=False)
        embed.add_field(name="`slap`", value="*Slap someone </3*", inline=False)
        embed.add_field(name="`feed`", value="*Feed someone -.-*", inline=False)
        embed.add_field(name="`cuddle`", value="*Cuddle with someone ⊂（♡⌂♡）⊃*", inline=False)
        embed.add_field(name="`tickle`", value="*Tickle someone ♡*", inline=False)
        embed.add_field(name="`pat`", value="*Pat someone (ㆆ_ㆆ)*", inline=False)
        embed.add_field(name="`poll`", value="*Start a poll (ง︡'-'︠)ง*", inline=False)
        # embed.add_field(name="",value="",inline=False)
        embed.set_footer(text='𝙛𝙪𝙣 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨')

        await ctx.send(embed=embed)

    @commands.command()
    async def nsfw(self, ctx):
        embed = discord.Embed(title="`Nsfw`", color=color, inline=True)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="`anal`", value="*view anal*", inline=False)
        embed.add_field(name="`lewd`", value="*some anime hentai command*", inline=False)
        embed.add_field(name="`trap`", value="*get trapped*", inline=False)
        embed.add_field(name="`neko`", value="*you weeb*", inline=False)
        embed.add_field(name="`pussy`", value="*you need some pussy*", inline=False)

        # embed.add_field(name="",value="",inline=False)
        embed.set_footer(text='𝙣𝙨𝙛𝙬 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨')

        await ctx.send(embed=embed)

    @commands.command()
    async def user(self, ctx):
        embed = discord.Embed(title="`User`", color=color, inline=True)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="`av`", value="*Avatar someone*", inline=False)
        embed.add_field(name="`purge`", value="*Purges amount of messages*", inline=False)
        embed.add_field(name="`snipe`", value="*Snipe a message*", inline=False)
        embed.add_field(name="`embed`", value="*Embed a message, Title | Description*", inline=False)

        # embed.add_field(name="",value="",inline=False)
        embed.set_footer(text='𝙪𝙨𝙚𝙧 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨')

        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="`Info`", color=color, inline=True)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="`serverinfo`", value="*Purges amount of messages*", inline=False)
        embed.add_field(name="`userinfo`", value="*Purges the bots messages*", inline=False)
        embed.add_field(name="`bot`", value="*Gives you self bot information*", inline=False)
        embed.add_field(name="`stream`", value="*Change status to streaming*", inline=False)
        embed.add_field(name="`inv`", value="*Download the selfbot*", inline=False)

        # embed.add_field(name="",value="",inline=False)
        embed.set_footer(text='𝙞𝙣𝙛𝙤 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(help(client))
