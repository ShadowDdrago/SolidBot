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
#СОЗДАНИЕ ВСЕХ КНОПОК
    # ОСНОВНАЯ КНОПКА
    global MainButton
    class MainButton(disnake.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.wardrob =  ['<:greenpoint:1255098975208607805> Туманность \n \
                        <:yellowpoint:1255098956321521807> Неко тян\n\
                        <:yellowpoint:1255098956321521807> Dota 2 \n\
                        <:greenpoint:1255098975208607805> Valorant \n\
                        <:greenpoint:1255098975208607805> Закат \n\
                        ','АБОБАББАА 1', 'АБОБАААА 2']
            self.count = 0
            self.wardrobe_embed = disnake.Embed()

        @disnake.ui.button(
            label="Гардироб", style=disnake.ButtonStyle.green,custom_id="gard"
        )
        async def green(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            self.wardrobe_embed.add_field(name = "**Фоны профыиля**" ,
                                     value=f"{self.wardrob[0]}" )
            emojis = inter.message.guild
            await inter.send(embed = self.wardrobe_embed, view=SupportButton() , ephemeral=True)
    global SupportButton
    class SupportButton(disnake.ui.View):
        def __init__(self, *, timeout: None):
            super().__init__(timeout=timeout)
            self.count = 0
        @disnake.ui.button(
            label="Next", style=disnake.ButtonStyle.green, custom_id="next"
        )
        async def next(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            self.count += 1
            wardrobe_embed = disnake.Embed()
            wardrobe_embed.add_field(name = "**Фоны профыиля**" ,
                                     value=f"{self.wardrob[self.count]}")
            inter.edit_original_message(embed=wardrobe_embed)
    @commands.Cog.listener()
    async def on_ready(self):
        if not self.bot.persistent_views:
            self.bot.add_view(MainButton())
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