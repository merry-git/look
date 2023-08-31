import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=discord.Intents.all())
@client.event
async def on_ready():
  print("server up {0.user}".format(client))
  await client.change_presence(status=discord.Status.online,activity=discord.Game(':))'))

hypixelKey = "ENTER HYPIXEL API KEY HERE"
discordToken = "ENTER DISCORD BOT TOKEN HERE"
# HIGHLY ADVISED TO MAKE THESE ENVIORNMENT VARIABLES ^

@client.command()
async def stalk(ctx, ign:str):

    data = requests.get(f"https://api.hypixel.net/player?key={key}&name={ign}").json()
    
    classgrab = None
    skingrab = None

    try:
        classgrab = data['player']['stats']['Walls3']['chosen_class']
    except KeyError:
        await ctx.send("Please run the command in a minute!")
        return  
    except TypeError:
        await ctx.send("Player does not Exist. Try again!")
        return
      
    try:
        skingrab = data['player']['stats']['Walls3'][f'chosen_skin_{classgrab}']
    except KeyError:
        await ctx.send(f"{ign} is playing {classgrab} with UNKNOWN skin.")
        return

    message = f"{ign} is playing {classgrab} with {skingrab}."
    await ctx.send(message)

client.run(discordToken)
