import discord
from discord.ext import commands 
import os
import json
import requests
import random
from datetime import datetime
import urllib.parse # For encoding URLs

client = discord.Client()

# Variables used
x = 0
totalCommands = 0
text = ''

# Gets the contents of config.json file so the token is not revealed
with open('config.json') as f:
    data = json.load(f)
    token = data['token']
    prefix = data['prefix']
#--------------------------------------------------------------------------------------------------------------------------#

# Function that returns a "yo mamma" joke
def get_joke():
    response = requests.get('https://api.yomomma.info/') # API used for "yo mamma" jokes
    data = json.loads(response.text) # Loads the value of the variable which is the joke
    return data['joke'] # Returns the string of the joke
#--------------------------------------------------------------------------------------------------------------------------#

# Function that returns a Kanye West quote
def get_kanye_quote():
    response = requests.get('https://api.kanye.rest/') # API used for Kanye quotes
    data = json.loads(response.text) # Loads the value of the variable which is the quote
    return data['quote']
#--------------------------------------------------------------------------------------------------------------------------#

# Function that translates text to yoda
def translate_yoda(text):
    response = requests.get('https://api.funtranslations.com/translate/yoda.json?text='+urllib.parse.quote(text)) # Converts the text into a URL string
    data = json.loads(response.text)
    if data['error'] is None:
        return data['contents']['translated']
    else:
        return data['error']['message']
#--------------------------------------------------------------------------------------------------------------------------#

# Shows when the bot has logged in and what bot has logged in
@client.event
async def on_ready():
    os.system('clear')
    print("We have logged in as {0.user}".format(client))
#--------------------------------------------------------------------------------------------------------------------------#


# Sends a message according to what the user asks for
@client.event
async def on_message(message):

    message.content = message.content.lower()

    global x
    global totalCommands

    # If the bot sends the message the function isn't executed
    if message.author == client.user:
        return

    # Sends a message if the user sends hello with the prefix
    if message.content.startswith(prefix+'hello'):
        await message.channel.send('Hello!')
        print("Sent message: 'Hello'")
        x += 1 # Counts +1 if the command is used

    # Same as above, but in Portuguese
    if message.content.startswith(prefix+'ola') or message.content.startswith(prefix+'olá'):
        await message.channel.send('Olá!')
        print("Sent message: 'Olá'")
        x += 1 # Counts +1 if the command is used

    # Sends a "yo mamma" joke using the get_joke() function
    if message.content.startswith(prefix+'joke') or message.content.startswith(prefix+'piada'):
        joke = get_joke()
        await message.channel.send(joke)
        print("Sent message: 'Joke'")
        x += 1 # Counts +1 if the command is used

    # Sends the website nheco.me if the user requests nheco
    if message.content.startswith(prefix+'nheco'):
        await message.channel.send('https://www.nheco.me/')
        print("Sent message: 'Nheco'")
        x += 1 # Counts +1 if the command is used

    # Sends a Kanye West quote using the kanye.rest API
    if message.content.startswith(prefix+'kanye'):
        quote = get_kanye_quote()
        await message.channel.send(quote)
        print("Sent message: 'Kanye Quote'")
        x += 1 # Counts +1 if the command is used

    # Translates the message sent to yoda
    if message.content.startswith(prefix+'yoda'):
        message.content = message.content.replace('€yoda','')
        text = translate_yoda(message.content) # Sends the message to the function
        await message.channel.send(text)
        print("Sent message: 'Yoda Translation'")
        x += 1 # Counts +1 if the command is used

    # Fakes a transaction to the user's account
    if message.content.startswith(prefix+'paid') or message.content.startswith(prefix+'paypal') or message.content.startswith(prefix+'pay'):
        await message.channel.send('Sending now 100€ to your account!')
        print("Sent message: 'Sent Transaction'")
        x += 1 # Counts +1 if the command is used
    
    # Says if 5 commands have been used and the total commands used
    if x == 5:
        totalCommands = totalCommands + x # Sums the total of commands
        print("Used ",x," Commands | In total ",totalCommands," commands have been used")
        x = 0 # Resets the variable
        
#--------------------------------------------------------------------------------------------------------------------------#

client.run(token)