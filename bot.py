import discord
import json
import os

from discord.ext import commands
from utils import default

with open('./config/auth.json', 'r') as a:
    auth = json.load(a)

with open('./config/config.json', 'r') as c:
    config = json.load(c)

client = commands.Bot(
    command_prefix = config["prefix"],
    help_command = commands.DefaultHelpCommand(command_attrs=dict(brief="Displays this message.", description=f"Displays help message."), no_category='About')
)

# Bot info
@client.command(brief="Displays information about the bot.", description="Displays information about bot.", name="info")
@commands.guild_only()
async def info(ctx):
    info = "[info message]"
    await ctx.send(info)

for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
        client.load_extension(f'modules.{filename[:-3]}')
        print(f"Extension: {filename[:-3]} sucessfully loaded.")
        
client.run(auth["token"])
