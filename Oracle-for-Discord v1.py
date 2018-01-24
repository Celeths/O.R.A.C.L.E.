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

global answer

firstcheck = ("should", "can", "is", "will", "did", "do", "am", "are", "will", "was")
firstanswers = ("Yes", "No", "Maybe", "Perhaps", "Probably not", "Not going to touch this one")

secondcheck = ("what")
nextSecondCheck = ("will", "is")
nextSecondCheckAnswers = ("Bad things", "Nothing.", "You know this already", "Good things",
                          "Complete destruction", "Perfection")

thirdCheck = ("how")
nextThirdCheck = ("many", "much")
nextThirdCheckTwo = ("will", "can", "am", "are")
nextThirdCheckTwoAnswers = ("With failure", "With success", "Badly", "Averagely", "Amazingly")
nextThirdCheckThree = ("more")
nextThirdCheckThreeAnswers = ("Many more", "Just a few", "Almost done", "It never ends")

fourthCheck = ("when")
fourthCheckAnswers = ("Soon", "Never", "In a while", "Now", "Today", "In a long time", "Didn't it already happen")

feelings = ("Good", "Bad", "Sad", "Happy", "Depressed", "Manic", "Strangely good", "Almost dead")

bot = commands.Bot(command_prefix="o!")

def teller(starter):
    answer = ""
    if starter[0] in firstcheck:
        answer = (random.choice(firstanswers))
    elif starter[0] in secondcheck:
        if starter[1] in nextSecondCheck:
            answer = (random.choice(nextSecondCheckAnswers))
    elif starter[0] in thirdCheck:
        if starter[1] in nextThirdCheck:
            if starter[2] in nextThirdCheckThree:
                either = randint(1,2)
                if either == 1:
                    answer = (random.choice(nextThirdCheckThreeAnswers))
                else:
                    manyValue = randint(0,randint(10, 100))
                    answer = (manyValue)
            else:
                manyValue = randint(0,randint(10, 100))
                answer = (manyValue)
        if starter[1] in nextThirdCheckTwo:
            if starter[2] != "you":
                if starter[2] != "I":
                    answer = (random.choice(nextThirdCheckTwoAnswers))
                else:
                    answer = (random.choice(feelings))
            else:
                answer = (random.choice(feelings))
    elif starter[0] in fourthCheck:
        answer = (random.choice(fourthCheckAnswers))

    else:
        answer = ("I'm sorry, I didn't understand the question")


    answer = (str(answer) + ".")

    return answer

@bot.event
async def on_ready():
    print("Active as " + bot.user.name + "\nWith the id " + bot.user.id + ".")

@bot.command(pass_context=True)
async def tell(ctx):
    msg = ctx.message.content.split(" ", 1)
    response = msg[1]
    response = str(response).lower()
    starter = re.sub("[^\w]", " ",  response).split()
    answer = teller(starter)
    await bot.say(str(answer))

#Token to run (KEEP SECRET)
bot.run("TOKEN")