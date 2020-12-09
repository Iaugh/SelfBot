import collections

import discord
import json
import requests
import asyncio
import os
import datetime
import random

from discord import client
from discord.ext import commands
from discord.ext.commands import has_permissions

color = 0x2f3137


class admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        return await ctx.send(f'{round(self.client.latency * 1000)}ms zzz lagging')

    @commands.command()
    async def support(self, ctx):
        return await ctx.send(f'Join ny')



def setup(client):
    client.add_cog(admin(client))
