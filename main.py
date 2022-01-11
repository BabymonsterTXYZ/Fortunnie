import random
import discord
import asyncio
from discord.ext import commands

coin = ['Head','Tail']
cards = ['Card No. 0 THE FOOLS', 
        'Card No. 1 THE MAGICIAN', 
        'Card No. 2 THE HIGH PRIESTESS', 
        'Card No. 3 THE EMPRESS', 
        'Card No. 4 THE EMPEROR', 
        'Card No. 5 THE HIEROPHANT', 
        'Card No. 6 THE LOVERS', 
        'Card No. 7 THE CHARIOT', 
        'Card No. 8 THE STRENGHT',
        'Card No. 9 THE HERMIT',
        'Card No. 10 WHEEL OF FORTUNE',
        'Card No. 11 JUSTICE', 
        'Card No. 12 THE HANGED MAN',
        'Card No. 13 DEATH', 
        'Card No. 14 TEMPERAMCE', 
        'Card No. 15 THE DEVIL', 
        'Card No. 16 THE TOWER', 
        'Card No. 17 THE STAR', 
        'Card No. 18 THE MOON', 
        'Card No. 19 THE SUN', 
        'Card No. 20 JUDGEMENT'
        'Card No. 21 THE WORLD']

bot = commands.Bot(command_prefix = "-")

@bot.event
async def on_ready():
    print("I'm ready !")

@bot.command()
async def roll(ctx):
    embed = discord.Embed(title = "Dice Rolled", description=(random.randint(1, 6)) , color = (0x7F7F7F))
    await ctx.send(embed = embed)


@bot.command()
async def flip(ctx):
    embed = discord.Embed(title="Coin Fliped", description=(random.choice(coin)), color=(0x7F7F7F))
    await ctx.send(embed = embed)

@bot.command()
async def card(ctx):
    embed = discord.Embed(title="Card picked", description=(random.choice(cards)), color=(0x7F7F7F))
    await ctx.send(embed = embed)
    

bot.run('token')
 
