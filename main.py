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

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx:discord.ApplicationContext):
    await ctx.respond("Hey!")

@bot.slash_command(name = "start", description = "start arma 3 server")
async def start(ctx:discord.ApplicationContext):
    r = requests.post('locallhost/arma3/start')
    await ctx.respond(r.json())

bot.run(os.getenv('TOKEN'))