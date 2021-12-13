import discord
from discord.ext import commands 
import json
import random
import requests
import urllib.parse # For encoding URLs
import asyncio

class Memes(commands.Cog): # Registers the class of the commands in the €help command
    def __init__(self, bot):
        self.bot = bot


    # Shows when the cog has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has loaded.")


    # Function that gets a joke form the API and sends it
    @commands.command(
        name = "Joke",
        description = "Sends a yo mama joke."
    )
    async def get_joke(self, ctx):
        """Sends a yo mama joke."""
        response = requests.get('https://api.yomomma.info/') # Gets the joke from the API
        data = json.loads(response.text) # Loads the contents of the json file to data as an array
        embed = discord.Embed(title =  data['joke'], color = discord.Color.random())
        await ctx.send(embed = embed)


    # Function that gets a fact from the API and sends it
    @commands.command(
        name = "Fact", # Sets the command 
        aliases = ["UselessFact", "uf"], # Sets other ways to use the command
        description = "Sends a Useless Fact." # A description of the command
    )
    async def get_fact(self, ctx):
        """Sends a Useless Fact.""" # A description of the command
        response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
        data = json.loads(response.text)
        embed = discord.Embed(title = data['text'], color = discord.Color.random())
        await ctx.send(embed = embed)


    # Function that translates from regular speech to yoda speech
    @commands.command(
        name = "Yoda",
        description = "Translates from regular speech to yoda speech."
    )
    async def yoda_translate(self, ctx, *, message):
        """Translates from regular speech to yoda speech."""
        url_text = urllib.parse.quote(str(message)) # Takes the context of the message and turns it into a url string
        response = requests.get('https://api.funtranslations.com/translate/yoda.json?text='+url_text)
        data = json.loads(response.text)
        if 'error' in data: # Checks if error exists in the json file
            embed = discord.Embed(title = data['error']['message'], color = discord.Color.random())
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title = data['contents']['translated'], color = discord.Color.random())
            await ctx.send(embed = embed)


    # Sends a Kanye Quote
    @commands.command(
        name = "Kanye",
        aliases = ["KanyeQuoted", "kq"],
        description = "Sends a Kanye Quote."
    )
    async def get_kanye_quote(self, ctx):
        """Sends a Kanye Quote."""
        response = requests.get('https://api.kanye.rest/')
        data = json.loads(response.text)
        embed = discord.Embed(title = data['quote'], color = discord.Color.random())
        await ctx.send(embed = embed)


    # Nheco
    @commands.command(
        name = "Nheco",
        description = "Nheco, try it."
    )
    async def nheco(self, ctx):
        """Nheco, try it."""
        embed = discord.Embed(color=discord.Colour.random())
        embed.add_field(name = 'Nheco, try it... :pinched_fingers:', value = "[Nheco](https://www.nheco.me/)")
        await ctx.send(embed = embed)


    # Sends money
    @commands.command(
        name = "PayPal",
        aliases = ["Pay", "Paid"],
        description = "I will send you money!"
    )
    async def paypal(self, ctx):
        """I will send you money!"""
        text = 'Sending you money.'
        message = await ctx.send(text)
        for i in range(8):
            await asyncio.sleep(0.5)
            text += '.'
            await message.edit(content = text)
        await ctx.send('Done!')
            

def setup(bot):
    bot.add_cog(Memes(bot))