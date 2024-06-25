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
#ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ
    global wardrob
    global MainButton
    global SupportButton
#=====================
    wardrob =  ['<:greenpoint:1255098975208607805> Графити \n \
                        <:yellowpoint:1255098956321521807> Туманность\n\
                        <:yellowpoint:1255098956321521807> Minecraft \n\
                        <:greenpoint:1255098975208607805> Minecraft_invers \n\
                        <:greenpoint:1255098975208607805> card6 изменить нахуй мало пикселей \n\
                        ',
                        '<:greenpoint:1255098975208607805> Апокалипсис \n \
                        <:yellowpoint:1255098956321521807> Город \n \
                        <:greenpoint:1255098975208607805> Dota2 \n \
                        <:yellowpoint:1255098956321521807> Luffy \n \
                        <:greenpoint:1255098975208607805> Природа \n \
                                            ', 
                        '<:greenpoint:1255098975208607805> Некотян \n\
                        <:greenpoint:1255098975208607805> Степь \n \
                        <:greenpoint:1255098975208607805> Valorant \n']
    class MainButton(disnake.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            
            

        @disnake.ui.button(
            label="Гардироб", style=disnake.ButtonStyle.green,custom_id="gard"
        )
        async def green(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            wardrobe_embed = disnake.Embed().add_field(name = "**Фоны профыиля**" ,
                                     value=f"{wardrob[0]}" )
            wardrobe_embed.set_footer(text = f"{1}/{len(wardrob)}")
            await inter.send(embed = wardrobe_embed, view=SupportButton() , ephemeral=True)
    class SupportButton(disnake.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.count = 0
        @disnake.ui.button(
            label="Next", style=disnake.ButtonStyle.green, custom_id="next"
        )
        async def next(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            self.count += 1
            try: 
                text = wardrob[self.count]
            except: 
                self.count = 0 
                text = wardrob[self.count]
            wardrobe_embed = disnake.Embed()
            wardrobe_embed.add_field(name = "**Фоны профыиля**" ,
                                     value=f"{wardrob[self.count]}")
            wardrobe_embed.set_footer(text = f"{self.count+1}/{len(wardrob)}")
            await inter.response.edit_message(embed=wardrobe_embed)
        @disnake.ui.button(
            label="previous", style=disnake.ButtonStyle.green, custom_id="previous"
        )
        async def previous(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            self.count -= 1
            try: 
                text = wardrob[self.count]
            except: 
                self.count = len(wardrob) -1 
                text = wardrob[self.count]
            wardrobe_embed = disnake.Embed()
            wardrobe_embed.add_field(name = "**Фоны профыиля**" ,
                                     value=f"{wardrob[self.count]}")
            wardrobe_embed.set_footer(text = f"{self.count+1}/{len(wardrob)}")
            await inter.response.edit_message(embed=wardrobe_embed)
    @commands.Cog.listener()
    async def on_ready(self):
        if not self.bot.persistent_views:
            self.bot.add_view(MainButton())
            self.bot.add_view(SupportButton())
    @commands.command(auto_sync=True)
    async def mark(self, inter: disnake.AppCmdInter): 
        #Отправка изображения с надписью МАГАЗИН
        fp = io.BytesIO()
        shop = Image.open('/home/container/assets/sources/Solid.png')
        shop.save(fp=fp,format ='PNG')
        fp.seek(0)
        shop.close()
        shop=File(fp=fp , filename="Solid.png")
        
        await inter.send(file=shop, view = MainButton())
            
            
            
        
    
def setup(bot):
    bot.add_cog(Shops(bot))