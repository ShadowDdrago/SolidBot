import pymysql.cursors
import ast
import pymysql
import disnake
from disnake import *
from disnake.ext import commands
from disnake.ui import *
import os, io
import asyncio
import asyncpg
import numpy as np 
import aggdraw
from PIL import Image, ImageDraw, ImageFont
import requests
from confi import config
class Shops(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @commands.command(auto_sync=True)
    async def market(self, inter: disnake.AppCmdInter):        
        shops = disnake.Embed(color=0x303136)
        fp = io.BytesIO()
        shop = Image.open('/home/container/SolidBot/assets/sources/Solid.png')
        shop.save(fp=fp,format ='PNG')
        fp.seek(0)
        shop.close()
        shop=File(fp=fp , filename="Solid.png")
        shops.set_image(file = shop)
        await inter.send(embed=shops)
def setup(bot):
    bot.add_cog(Shops(bot))