import discord
from discord.ext import commands
import configs
import datetime as dt

client = commands.Bot( command_prefix = configs.PREFIX )
client.remove_command( "help" )

@client.event
async def on_ready():
    print( "Бот успешно подключен и запущен ->>" )

@client.command()
async def time(ctx):
    time = dt.datetime.now().strftime("%H:%M:%S")
    embed = discord.Embed( title = "Текущее время", colour = discord.Color.gold())
    embed.add_field(name = "Сейчас:", value= f"{time}")
    embed.set_author(name = client.user.name, icon_url= client.user.avatar_url)
    await ctx.send(embed = embed)

@client.command()
async def date(ctx):
    time = dt.datetime.now().strftime("%m.%d.%Yг.")
    embed = discord.Embed( title = "Текущая дата", colour = discord.Color.gold())
    embed.add_field(name = "Сегодня:", value= f"{time}")
    embed.set_author(name = client.user.name, icon_url= client.user.avatar_url)
    await ctx.send(embed = embed)

@client.command()
async def datetime( ctx ):
    time = dt.datetime.now()
    embed = discord.Embed( title = "Текущее время и дата", colour = discord.Color.gold())
    embed.add_field(name = "Сейчас:", value= "{}".format(time.strftime("%b %d %Y %H:%M:%S")))
    embed.set_author(name = client.user.name, icon_url= client.user.avatar_url)
    await ctx.send(embed = embed)

@client.command()
async def help( ctx ):
    time = dt.datetime.now()
    embed = discord.Embed( title = "Список всех команд", colour = discord.Color.gold())
    embed.add_field(name = f"{configs.PREFIX}time", value= "Выводит текущее время ⌚\nФормат: Часы:минуты:секунды")
    embed.add_field(name = f"{configs.PREFIX}date", value= "Выводит текущую дату 📅\nФормат: Месяц.День.Год")
    embed.add_field(name = f"{configs.PREFIX}datetime", value= "Выводит текущую дату и время 📅\nФормат: Месяц День Год Часы:минуты:секунды")
    embed.set_author(name = client.user.name, icon_url= client.user.avatar_url)
    await ctx.send(embed = embed)

client.run(configs.TOKEN)