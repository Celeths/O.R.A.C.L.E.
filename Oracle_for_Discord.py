"""Operational Revelator And Change Likeliness Estimator - For Discord
            Made by Leveles"""
import discord
from discord.ext import commands
from discord.ext.commands import bot
import os
import re
import random
from random import randint
import asyncio
import magic_conch_shell
import vocab

bot = commands.Bot(command_prefix="o!")

client = discord.Client()

@bot.event
async def on_ready():
    print("Active as " + bot.user.name + "\nWith the id " + bot.user.id + ".")


@bot.command(pass_context=True)
async def say(ctx):
    global starter
    name = ctx.message.author
    msg = ctx.message.content.split(" ", 1)
    response = msg[1]
    response = str(response).lower()
    starter = re.sub("[^\w]", " ",  response).split()
    magic_conch_shell.teller(starter)
    await bot.say(str(magic_conch_shell.answer))
    if magic_conch_shell.error == "record":
        manager = open("Error log", "a")
        manager.write(str((name)) + " : " + response + "\n")
        manager.close()

#Token to run (KEEP SECRET)
bot.run(os.environ["DISCORD_ORACLE_TOKEN"])