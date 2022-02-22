# Lab Project 2 - Autonomous Artistic Agent by Anthony Venditti
# Discord bot reference help: https://realpython.com/how-to-make-a-discord-bot-python/
# Fortunes: https://joshmadison.com/2008/04/20/fortune-cookie-fortunes/
# Magic 8 Ball answers: https://www.pinterest.ca/pin/216806169541583348/
# Bot profile picture: https://image.pngaaa.com/464/5306464-middle.png
# Photos used for photo command: https://unsplash.com/s/photos/mysterious?order_by=latest (website)

# DISCORD SERVER (PLEASE JOIN!!!): https://discord.gg/rUF2A2bfcE

import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix=['!', '?', '.'], intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is now Online! Please join the Discord server, if you have not already, using the link at the top^^^')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey {member.name}, welcome to my EECS 1720 Lab Project #2 Discord server!\n' 
        'To get started, please open the server and type \'!help\' in the general text-channel (should be the only channel).\n'
        'Enjoy the mysteries that await you!\n\n'
        '~Sincerely, MysteryBot?¿'
    )

    
@bot.command()
async def help(context):
    await context.send(
        '**-----HELP-----**\n'
        '*You must use !, ., or ? as a prefix for each command!* \n\n'
        '**Commands:**\n'
        'fortune - Provides you with a random and very mysterious fortune🔮\n'
        'number - Tests your luck with a random generated number from 1-100💯\n'
        'coin - Call heads or tails first, then flip away. Great for decisions🪙\n'
        'magic8 - Ask a question, then enter this command for an answer🎱\n'
        'photo - An unknown mysterious photo, likely classified...🖼️\n'
        'help - Shows this message.'
        )


@bot.command(name='fortune')
async def Fortune(ctx):
    fortunes = [
        'A good friendship is often more important than a passionate romance.',
        'Accept something that you cannot change, and you will feel better.',
        'Do not be intimidated by the eloquence of others.',
        'Follow the middle path. Neither extreme will make you happy.',
        'Have a beautiful day, you deserve it🙂',
        'If you wish to see the best in others, show the best of yourself.',
        'The greatest achievement in life is to stand up again after falling.',
        'What\'s that in your eye? Oh... it\'s a sparkle✨',
        'You will be sharing great news with all the people you love.',
        'Your happiness is before you, not behind you! Cherish it❤️'
    ]

    response = random.choice(fortunes)
    await ctx.send(response)


@bot.command(name='number')
async def Number(ctx):
    numbers = random.randint(1, 100)

    response = numbers
    await ctx.send(response)


@bot.command(name='coin')
async def Coin(ctx):
    coinSide = [
        'Heads.',
        'Tails.',
        'OMG, it landed on the side 0o0'
    ]

    response = random.choice(coinSide)
    await ctx.send(response)


@bot.command(name='magic8')
async def Magic8(ctx):
    answers = [
        'Yes - definitely👌',
        'My sources say... uh, no.',
        'VERY doubtful, sorry🙁',
        'Don\'t count on it.',
        'Outlook good.',
        'Certainly.',
        'Ask again later.',
        'Ehhh... can\'t predict that right now🤷‍♂️',
        'Better I don\'t tell you.'
    ]

    response = random.choice(answers)
    await ctx.send(response)


@bot.command(name='photo')
async def Photo(ctx):
    pick = random.randint(1, 5)
    if pick == 1:
        await ctx.send(file=discord.File('data/fog.jpg'))
    elif pick == 2:
        await ctx.send(file=discord.File('data/lady.jpg'))
    elif pick == 3:
        await ctx.send(file=discord.File('data/train.jpg'))
    elif pick == 4:
        await ctx.send(file=discord.File('data/darkness.jpg'))
    elif pick == 5:
        await ctx.send(file=discord.File('data/faceless.jpg'))


bot.run(TOKEN)
