import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import os
from dotenv import load_dotenv

load_dotenv() # load variables from the .env file

bot = commands.Bot(command_prefix='', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

COLORS = {
    "red": 0xff0000,
    "orange": 0xffa500,
    "yellow": 0xffff00,
    "green": 0x00ff00,
    "blue": 0x0000ff,
    "purple": 0x800080,
    "white": 0xffffff,
    "black": 0x000000
}

@slash.slash(name="embed",
             description="Send an embed",
             options=[
                 {
                     "name": "title",
                     "description": "Embed title",
                     "type": 3, # type 3 is a string
                     "required": True
                 },
                 {
                     "name": "description",
                     "description": "Embed description",
                     "type": 3,
                     "required": True
                 },
                 {
                     "name": "color",
                     "description": "Embed color",
                     "type": 3,
                     "required": True,
                     "choices": [
                         {
                             "name": "Red",
                             "value": "red"
                         },
                         {
                             "name": "Orange",
                             "value": "orange"
                         },
                         {
                             "name": "Yellow",
                             "value": "yellow"
                         },
                         {
                             "name": "Green",
                             "value": "green"
                         },
                         {
                             "name": "Blue",
                             "value": "blue"
                         },
                         {
                             "name": "Purple",
                             "value": "purple"
                         },
                         {
                             "name": "White",
                             "value": "white"
                         },
                         {
                             "name": "Black",
                             "value": "black"
                         }
                     ]
                 }
             ])
async def _embed(ctx: SlashContext, title: str, description: str, color: str):
    if color.lower() not in COLORS:
        await ctx.send("Invalid color specified.")
        return
    embed = discord.Embed(title=title, description=description, color=COLORS[color.lower()])
    await ctx.send(embed=embed)

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
bot.run(TOKEN)
