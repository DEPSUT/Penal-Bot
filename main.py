import discord
from discord.ext import commands 
import os
import json

# Permissions for the bot
intents = discord.Intents()
intents.messages = True
intents.bans = True
intents.guilds = True
intents.reactions = True
intents.guild_messages = True
intents.typing = True
intents.members = True
intents.voice_states = True


# Gets the contents of config.json file
with open('bot_files/settings/config.json') as f:
    data = json.load(f)
    token = data['token']
    owner = data['owner']
    random_api_key = data['random_api_key']

# Gets the default settings
with open('bot_files/server/settings.json', 'r') as f:
    data = json.load(f)
    prefix = data['prefix'] # The default prefix is '€'

# Changes the settings of the bot
bot = commands.Bot( # When the bot is in more than 100 servers use AutoShardedBot
    command_prefix = prefix,
    owner_id = owner,
    case_insensitive = True,
    intents = intents
)

bot.token = token
bot.version = "0.2"
bot.random_api = random_api_key


# Shows some information when the bot logs in
@bot.event
async def on_ready():
    os.system('clear')
    print("#--------------------------#")
    print("Logged in as: "+bot.user.name+"#"+bot.user.discriminator)
    print("Bot Latency:", round(bot.latency * 1000, 2), "ms")
    print("Bot Version:", bot.version)
    print("Discord.py Version:", discord.__version__)
    print("#--------------------------#")


for filename in os.listdir("cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(bot.token)