import discord
import json
import requests
import asyncio
import os
import datetime
import random
from discord.ext import commands
from discord.ext.commands import has_permissions

color = 0x2f3137


class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def poll(self, ctx, *, question):
        await ctx.message.delete()
        emoji1 = '✅'
        emoji2 = '❌'
        question = await ctx.send(f'{question}')
        await question.add_reaction(emoji1)
        await question.add_reaction(emoji2)

    @commands.command()
    async def kiss(self, ctx, user: discord.Member):
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        em = discord.Embed(description=f'{ctx.author.mention} kisses {user.mention}', color=color)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

    @commands.command()
    async def dog(self, ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://dog.ceo/api/breeds/image/random").json()
        em = discord.Embed(description=f'woof', color=color)
        em.set_image(url=str(r['message']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['message']))  

    @commands.command()
    async def pat(self, ctx, user: discord.Member):
        r = requests.get("https://nekos.life/api/v2/img/pat")
        res = r.json()
        em = discord.Embed(description=f'{ctx.author.mention} pats {user.mention}', color=color)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

    @commands.command()
    async def hug(self, ctx, user: discord.Member):
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        em = discord.Embed(description=f'{ctx.author.mention} hugs {user.mention}', color=color)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

    @commands.command()
    async def slap(self, ctx, user: discord.Member):
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()
        em = discord.Embed(description=f'{ctx.author.mention} slaps {user.mention}', color=color)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

    @commands.command()
    async def tickle(self, ctx, user: discord.Member):
        r = requests.get("https://nekos.life/api/v2/img/tickle")
        res = r.json()
        em = discord.Embed(description=f'{ctx.author.mention} tickles {user.mention}', color=color)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

    @commands.command()
    async def feed(self, ctx, user: discord.Member):
        r = requests.get("https://nekos.life/api/v2/img/feed")
        res = r.json()
        em = discord.Embed(description=f'{ctx.author.mention} feeds {user.mention}', color=color)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

    @commands.command()
    async def cuddle(self, ctx, user: discord.Member):
        r = requests.get("https://nekos.life/api/v2/img/cuddle")
        res = r.json()
        em = discord.Embed(description=f'{ctx.author.mention} cuddles {user.mention}', color=color)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

    @commands.command()
    async def lizard(sself, ctx): 
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/lizard").json()
        em = discord.Embed(description=f'', color=color)
        em.set_image(url=str(r['url']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['message']))   


def setup(client):
    client.add_cog(fun(client))
