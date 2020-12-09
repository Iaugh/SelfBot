import discord
import json
import requests
import asyncio
import os
import random
from datetime import datetime, timezone
from discord.ext import commands

color = 0x2f3137


class lookup(commands.Cog):

    def __init__(self, client):
        self.client = client

    # @commands.command()
    # async def bots(self, ctx):
    #     my_embed = discord.Embed(
    #         description=" [__**Click Me!**__](https://discord.com/api/oauth2/authorize?client_id=771697308458811434&permissions=8&scope=bot)",
    #         color=color)
    #
    #     my_embed.add_field(name="Version Code:\n", value="v0.1", inline=False)
    #
    #     my_embed.add_field(name="Released On:", value="November 2020", inline=False)
    #
    #     my_embed.add_field(name="Servers", value=len(ctx.client.guilds))
    #
    #     my_embed.set_footer(text="Made by Cap")
    #
    #     my_embed.set_author(name="Xo Info")
    #
    #     await ctx.message.channel.send(embed=my_embed)

    @commands.command(name='inv')
    async def inv(self, ctx):
        print('inv link generated')
        embed = discord.Embed(
            title="Wanna use this selfbot?",
            description=" [__Click Me!__](https://discord.gg/ny)",
            color=color,
            timestamp=datetime.now(),
        )
        embed.set_footer(text="moon")
        await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        date_format = "%a , %d %b %Y %I:%M %p"
        join_pos = sorted(ctx.guild.members, key=lambda member: member.joined_at).index(member) + 1
        roles = [role for role in member.roles]
        embed = discord.Embed(timestamp=ctx.message.created_at, color=color)
        embed.set_author(name=str(member), icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)

        embed.add_field(name="ID:", value=member.id, inline=False)
        embed.add_field(name="Display Name:", value=member.display_name, inline=False)

        embed.add_field(name="Registered", value=member.created_at.strftime(date_format), inline=False)
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                        inline=False)
        embed.add_field(name="Position:", value=f"{join_pos}/{len(ctx.guild.members)}", inline=False)

        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="Highest Role:", value=member.top_role.mention, inline=False)
        embed.set_footer(text=f"𝙧𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙙 𝙗𝙮 {ctx.author.name}", icon_url=ctx.author.avatar_url)
        print(member.top_role.mention)
        await ctx.send(embed=embed)

    @commands.command()
    async def serverinfo(self, ctx):
        name = ctx.guild.name
        create_server = ctx.guild.created_at
        owner_server = ctx.guild.owner
        server = ctx.message.guild
        role_count = len(server.roles)
        emoji_count = len(server.emojis)
        channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])

        em = discord.Embed(timestamp=ctx.message.created_at, color=color)
        em.set_author(name=str(name), icon_url=ctx.guild.icon_url)
        em.set_thumbnail(url=ctx.guild.icon_url)

        em.add_field(name="Owner", value=owner_server, inline=False)
        em.add_field(name='Region', value=server.region, inline=False)
        em.add_field(name='Members', value=server.member_count, inline=False)
        em.add_field(name="Created On", value=create_server.strftime("%a, %#d %B %Y"), inline=False)
        em.add_field(name='Text Channels', value=str(channel_count), inline=False)
        em.add_field(name='Number of Roles', value=str(role_count))
        em.add_field(name='Number of Emotes', value=str(emoji_count))

        await ctx.send(embed=em)


def setup(client):
    client.add_cog(lookup(client))
