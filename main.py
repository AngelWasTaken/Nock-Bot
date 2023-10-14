from discord.ext import commands
import discord

BOT_TOKEN = "MTA1NDQ0MzcxNzc2MDY0NzE2OQ.GGioCP.nvMZRdYlON_wYpSfNAis3xX-vBcHSlW5oeIimI"
CHANNEL_ID = 1041579268305584190

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Howdy :cowboy:")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Howdy :cowboy:")
#on startup
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
#("!Hello") = ("Hello!")
@bot.command()
async def test(ctx):
    await ctx.send("https://youtu.be/ykwqXuMPsoc?si=MndZ5AVvHA3H9srM")
#This is a youtube song leading to narwals in the ocean
bot.run(BOT_TOKEN)
