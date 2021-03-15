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


class nsfw(commands.Cog):

    def __init__(self, client):
        self.client = client

		
    @commands.command()
    async def anal(sself, ctx): 
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/anal").json()
        em = discord.Embed(description=f'', color=color)
        em.set_image(url=str(r['url']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['message']))
		
    @commands.command()
    async def lewd(sself, ctx): 
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/lewd").json()
        em = discord.Embed(description=f'', color=color)
        em.set_image(url=str(r['url']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['message']))
		
    @commands.command()
    async def trap(sself, ctx): 
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/trap").json()
        em = discord.Embed(description=f'', color=color)
        em.set_image(url=str(r['url']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['message']))


    @commands.command()
    async def foxgirl(sself, ctx): 
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/fox_girl").json()
        em = discord.Embed(description=f'', color=color)
        em.set_image(url=str(r['url']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['message']))		


    @commands.command()
    async def neko(sself, ctx): 
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/ngif").json()
        em = discord.Embed(description=f'', color=color)
        em.set_image(url=str(r['url']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['message']))

    @commands.command()
    async def pussy(sself, ctx): 
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/pussy").json()
        em = discord.Embed(description=f'', color=color)
        em.set_image(url=str(r['url']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['message']))	

		
		
def setup(client):
    client.add_cog(nsfw(client))
