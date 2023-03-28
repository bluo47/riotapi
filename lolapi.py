import requests
import config
import discord
import json

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content

    if msg.startswith('$status'):
        response = requests.get("https://na1.api.riotgames.com/lol/status/v4/platform-data?api_key={}".format(config.API_KEY))
        await message.channel.send(response)
        dict = json.loads(response)
        
        print(response.content)

# response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/sFzzz?api_key={}".format(config.API_KEY))

client.run(config.LPBOT_KEY)