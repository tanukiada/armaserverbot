import dotenv
import discord
import os
import requests

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command( description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(description = "start arma 3 server")
async def start(ctx):
    r = requests.post('127.0.0.1:8080/arma3/start')
    await ctx.respond(r.json())

bot.run(os.getenv('TOKEN'))