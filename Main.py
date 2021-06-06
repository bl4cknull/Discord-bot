import discord
import os
import random
import youtube_module
import pyshorteners as sh
import harvester
import insta_follower
from django.core.validators import URLValidator
from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
validator = URLValidator()
s = sh.Shortener()
client = discord.Client()
img = 'https://cdn.discordapp.com/avatars/743381002382082198/e7bbfd903534e2aecec7748e707c3626.webp?size=1024'

@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord!")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, welcome to my Discord server!")


bot = commands.Bot(command_prefix="0")


@bot.command(name="yt")
async def youtube(ctx, url):
    await ctx.message.reply("W A I T . . .", delete_after=5)
    link = youtube_module.get_download_link(url)
    response = "link: {}".format(link)
    await ctx.message.reply(response)


@bot.command(name="cc")
@commands.has_role("admin")
async def create_channel(ctx, channel_name,category_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f"Creating a new channel: {channel_name}")
        await guild.create_text_channel(channel_name)
        await ctx.message.reply("your channel created successfully", delete_after=5)

@bot.command(name="ig")
async def gain_data(ctx, url):
    await ctx.message.reply("its maybe take a moment...", delete_after=5)
    data = harvester.datas(url)
    await ctx.send(file=discord.File('result.txt'))

@bot.command(name="fn")
async def get_insta(ctx, insta_id):
    await ctx.message.reply("W A I T . . .", delete_after=5)
    numbers = insta_follower.get_follower(insta_id)
    response = "Your follower numbers: {}".format(f'{numbers:,}')
    await ctx.message.reply(response)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("You do not have the required role for this command.")


bot.run(TOKEN)
