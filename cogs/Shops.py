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
    global PersistentView
    class PersistentView(disnake.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @disnake.ui.button(
            label="Green", style=disnake.ButtonStyle.green, custom_id="persistent_example:green"
        )
        async def green(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
            Wardrob = ['<:greenpoint:1255098975208607805> Туманность \n \
                        <:yellowpoint:1255098956321521807> Неко тян\n\
                        <:yellowpoint:1255098956321521807> Dota 2 \n\
                        <:greenpoint:1255098975208607805> Valorant \n\
                        <:greenpoint:1255098975208607805> Закат \n\
                        ']
            wardrobe_embed = disnake.Embed()
            wardrobe_embed.add_field(name = "**Фоны профыиля**" ,
                                     value=f"{Wardrob[0]}" )
            emojis = inter.message.guild
            await inter.send(embed = wardrobe_embed, ephemeral=True)
    @commands.Cog.listener()
    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(PersistentView())
            self.persistent_views_added = True
    @commands.command(auto_sync=True)
    async def mark(self, inter: disnake.AppCmdInter): 
        #Отправка изображения с надписью МАГАЗИН
        fp = io.BytesIO()
        shop = Image.open('/home/container/assets/sources/Solid.png')
        shop.save(fp=fp,format ='PNG')
        fp.seek(0)
        shop.close()
        shop=File(fp=fp , filename="Solid.png")
        
        await inter.send(file=shop, view = PersistentView())
    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        
        member = inter.author
        custom = inter.component.custom_id
        if custom == "wardrobe":
            Wardrob = ['<:greenpoint:1255098975208607805> Туманность \n \
                        <:yellowpoint:1255098956321521807> Неко тян\n\
                        <:yellowpoint:1255098956321521807> Dota 2 \n\
                        <:greenpoint:1255098975208607805> Valorant \n\
                        <:greenpoint:1255098975208607805> Закат \n\
                        ', 
                        '']
            wardrobe_embed = disnake.Embed()
            wardrobe_embed.add_field(name = "**Фоны профыиля**" ,
                                     value=f"\
                                     <:greenpoint:1255098975208607805> Туманность \n 
                                     <:yellowpoint:1255098956321521807> Неко тян\n\
                                     <:yellowpoint:1255098956321521807> Dota 2 \n\
                                     <:greenpoint:1255098975208607805> Valorant \n\
                                     <:greenpoint:1255098975208607805> Закат \n\
                                     " )
            emojis = inter.message.guild
            await inter.send(embed = wardrobe_embed, ephemeral=True)
            next_point = Button(style  = ButtonStyle.blurple,  label = "next",custom_id = "wardrobe")
            
            
            
        
    
def setup(bot):
    bot.add_cog(Shops(bot))