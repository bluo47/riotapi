import requests
import config
import discord
import json
from discord import app_commands

intents = discord.Intents.all()

client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=719741641463824425))
    # print "ready" in the console when the bot is ready to work
    print("ready")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content

    if msg.startswith('$status'):
        response = requests.get("https://na1.api.riotgames.com/lol/status/v4/platform-data?api_key={}".format(config.API_KEY))
        await message.channel.send(response)
        dict = response.json()
        
        # print(dict)

# response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/sFzzz?api_key={}".format(config.API_KEY))

@tree.command(name = "berate", description = "My first application Command", guild=discord.Object(id=719741641463824425)) 
async def first_command(interaction):
    await interaction.response.send_message("You're dogshit!")

@tree.command(name="name", description="description",guild=discord.Object(id=719741641463824425))
async def slash_command(interaction: discord.Interaction):    
    await interaction.response.send_message("command")

client.run(config.LPBOT_KEY)