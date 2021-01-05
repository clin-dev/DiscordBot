import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands #for bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

"""
intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, welcome!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run(TOKEN)

"""

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready(): 
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulate rolling dice.')
async def roll(ctx, num_of_dice: int):
    dice = [
        str(random.choice(range(1, 7)))
        for _ in range(num_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name='flip_coin', help='Simulate flipping coin.')
async def flip(ctx, num_of_coin: int):
    faces = ["head", "tail"]
    coin = [
        random.choice(faces)
        for _ in range(num_of_coin)
    ]
    await ctx.send(', '.join(coin))


bot.run(TOKEN)
