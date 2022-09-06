import discord
import random
from discord.ext import commands
from time import sleep
import os

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

ins = list(os.getenv("INSULTS"))
com = list(os.getenv("COMPLIMENTS"))

@bot.slash_command(name="repeat")
async def add(ctx, message: discord.Option(str)):
    message = f"{message}"
    await ctx.channel.send(message)
@bot.slash_command(name="insult")
async def add(ctx, user: discord.Option(str)):
    user = f"{user}"
    await ctx.respond(user + " " + random.choice(ins))
@bot.slash_command(name="compliment")
async def add(ctx, user: discord.Option(str)):
    user = f"{user}"
    print(user)
    if user == "<@!860101465087148052>":
        await ctx.respond(user + " " + random.choice(ins))
    else:
        await ctx.respond(user + " " + random.choice(com))
@bot.slash_command(name="reccomend-song")
async def add(ctx, song: discord.Option(str), author: discord.Option(str)):
    song = f"{song}"
    authors = f"{author}"
    channel = bot.get_channel(1012465214836457532)
    await channel.send(song + " - " + authors)
    await ctx.respond("Reccomendation logged")

@bot.slash_command(name="passfromip")
async def add(ctx, ip: discord.Option(str), passdictionary: discord.Option(str)):
    inimsg = await ctx.respond("Cracking passwd/phrase (using dashcrack method from uninterestingusername and ibzyy) initiated from " + str(ctx.author))
    sleep(3)
    await ctx.channel.send("Using dashcrack 4.3.2++ (ibzyy fork)")
    time = random.randint(1,5)
    await ctx.respond("Loading estimated: " + str(time) + "s")
    sleep(1)
    await ctx.channel.send("Checking if user is whitelisted: ")
    await ctx.respond("check DMs")
    dms = await bot.create_dm(ctx.author)
    await dms.send("Sorry, you are **not** whitelisted for dashcrack")
@bot.slash_command(name="dm-me-a-meme")
async def add(ctx):
    await ctx.respond("Meme sent, check dms")
    dms = await bot.create_dm(ctx.author)
    await dms.send("No I will not send you a meme " + random.choice(["fuck", "piss"]) + " off")
@bot.slash_command(name="viruscheck")
async def add(ctx, fileurl: discord.Option(str)):
    await ctx.respond("Preparing.. ")
    load = await ctx.respond("-------")
    sleep(random.randint(1,6))
    await load.edit("#------")
    sleep(random.randint(1,6))
    await load.edit("##-----")
    sleep(random.randint(1,6))
    await load.edit("###----")
    sleep(random.randint(1,6))
    await load.edit("#####---")
    sleep(random.randint(1,6))
    await load.edit("######--")
    sleep(random.randint(1,6))
    await load.edit("#######-")
    sleep(random.randint(1,6))
    await load.edit("########")
    await ctx.respond("inconclusive")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    cnl = bot.get_channel(1013222271512485890)
    await cnl.send(str(message.content) + " **-** " + str(message.author))
    
gay = "yes"
@bot.slash_command(name="is-mfbot-gay")
async def add(ctx):
    ctx.respond(str(gay))
bot.run(os.getenv("TOKEN"))
