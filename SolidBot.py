import disnake
from confi import TOKEN
import pymysql.cursors
import pymysql
from disnake.ext import commands
from disnake.ext import *
from disnake import *
from disnake.ui import *
import os
import asyncpg
from confi import config
intents = disnake.Intents(messages=True, guilds=True, members=True)
intents = disnake.Intents().all()
client = disnake.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents, test_guilds=[1125825837791449210])
async def all_members(ctx):
    await ctx.send(ctx.guild.members)
bot.remove_command('help')
#Cogs-
for cog in os.listdir("/home/container/SolidBot/cogs"):
    if cog.endswith(".py") and not cog.startswith("_"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        
        except Exception as e:
            print(f"{cog} не может быть загружен")
            raise e

#База данных 
@bot.event
async def on_ready():
    
    game = disnake.Game("Уже сокро)")
    await bot.change_presence(status=disnake.Status.online, activity=game)
    for guild in bot.guilds:
        for member in guild.members:
            try:
                db = pymysql.connect(**config)
                try:
                    with db.cursor() as cursor:
                        
                        if member == bot.user:
                            pass
                        elif cursor.execute("SELECT member_id FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", str(member.id)) == 0:
                            cursor.execute("INSERT INTO `s168073_kjabdgkjabkgb`.`members`(member_id, lvl, money, exp, custom) VALUE (%s, '0' , '0', '0',%s)", (str(member.id), str({"card": "card5"})))
                            db.commit()
                finally:
                    db.close()
            except Exception as ex : 
                print("Bad1")
                print(ex)
@bot.event
async def on_member_join(member: disnake.Member):
    try:
        db = pymysql.connect(**config)
        try:
            with db.cursor() as cursor:
                if member == bot.user:
                    pass
                
                elif cursor.execute("SELECT member_id FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", str(member.id)) == None:
                    cursor.execute("INSERT INTO `s168073_kjabdgkjabkgb`.`members`(member_id, lvl, money, exp, custom) VALUE (%s, '0' , '0', '0',%s)", (str(member.id), str({"card": "card5"})))
                    db.commit()
        finally:
            db.close()
    except Exception as ex : 
        print("Bad2")
        print(ex)
bot.run(TOKEN)