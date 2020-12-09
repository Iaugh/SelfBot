import discord
import asyncio
from discord.ext import commands
from datetime import datetime
from discord import Embed, Member
from discord.ext.commands import Cog, command, has_guild_permissions

color = 0x2f3137


class user(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.smc = None
        self.sma = None
        self.smi = None

    @Cog.listener()
    async def on_message_delete(self, message):

        self.smc = message.content
        self.sma = message.author
        self.smi = message.id
        await asyncio.sleep(60)

        if message.id == self.smi:
            self.sma = None
            self.smc = None
            self.smi = None

    @command(aliases=['s'])
    async def snipe(self, ctx):
        if self.smi is None:
            await ctx.send("Nothing to snipe within the last 60 seconds.")
        else:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            embed = Embed(color=color, description=f"{self.smc}")
            embed.set_author(name=f"{self.sma}", icon_url=self.sma.avatar_url)
            embed.set_footer(text=f"Message Sent at {current_time}")
            await ctx.send(embed=embed)


    @commands.command(aliases=['pfp'])
    async def av(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        embed = discord.Embed(title="Avatar", color=color)
        embed.set_author(name=f"{member}", icon_url=f'{member.avatar_url}')
        embed.set_image(url='{}'.format(member.avatar_url))
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(user(client))
