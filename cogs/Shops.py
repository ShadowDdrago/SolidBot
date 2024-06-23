import pymysql.cursors
import ast
import pymysql
import disnake
from disnake import *
from disnake.ext import commands
from disnake.ui import *
import  io
from PIL import Image, ImageDraw, ImageFont
import requests
from confi import config
class Shops(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:      
        self.bot = bot
    
    @commands.command(auto_sync=True)
    async def mark(self, inter: disnake.AppCmdInter): 
        #Отправка изображения с надписью МАГАЗИН
        fp = io.BytesIO()
        shop = Image.open('/home/container/assets/sources/Solid.png')
        shop.save(fp=fp,format ='PNG')
        fp.seek(0)
        shop.close()
        shop=File(fp=fp , filename="Solid.png")
        
        # Кнопочки
        wardrobe = Button(style = ButtonStyle.grey,  label = "Гордиробчик",custom_id = "wardrobe")
        #... 
        await inter.send(file=shop, components= [ActionRow(wardrobe)])
    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        
        member = inter.author
        custom = inter.component.custom_id
        if custom == "wardrobe":
            emojis = inter.message.guild
            wardrobe_embed = disnake.Embed()
            wardrobe_embed.add_field(name = "**Фоны профыиля**", value=f"<:zdot:1125146314607431701> Туманность \n <:zdot:1125146314607431701> Неко тян" )
            await inter.send(embed = wardrobe_embed, ephemeral=True)
            
            
            
        
    
def setup(bot):
    bot.add_cog(Shops(bot))