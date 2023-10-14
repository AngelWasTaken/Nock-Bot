from discord.ext import commands
import discord

BOT_TOKEN = "Nuh uh"
CHANNEL_ID = 1041579268305584190

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.create_dm()

@bot.event
async def on_ready():
    print("Howdy :cowboy:")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Howdy :cowboy:")
    #on start of bot

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
#!Hello = "Hello!"


@bot.command()
async def Ohgod(ctx):
    await ctx.send("Play with 4-15 player online or via local WiFi as you attempt to prepare your spaceship for departure, but beware as one or more random players among the Crew are Impostors bent on killing everyone! Originally created as a party game, we recommend playing with friends at a LAN party or online using voice chat. Enjoy cross-platform play between Android, iOS, PC, and console.")
#amongus


bot.run(BOT_TOKEN)
