import pymysql.cursors
import ast
import pymysql
from disnake.ext import commands
from disnake.ext import *
from disnake import *
from disnake.ui import *
import os, io
import disnake
import asyncio
import asyncpg
import numpy as np 
import aggdraw
from PIL import Image, ImageDraw, ImageFont
import requests
from confi import config
class Lvl(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        member = message.author
        if member != self.bot.user:
            try:
                db = pymysql.connect(**config)
                try:
                    with db.cursor() as cursor:
                        cursor.execute("SELECT * FROM `s168073_members`.`members` WHERE member_id = %s", member.id)
                        user = cursor.fetchall()[0]
                        lvl  =  user[3]
                        xp =  user[5]
                        cursor.execute("UPDATE `s168073_members`.`members` SET exp = %s WHERE member_id = %s", (xp+(0.1), member.id))
                        cursor.execute("SELECT * FROM `s168073_members`.`members` WHERE member_id = %s", member.id)
                        xp =  user[5]
                        if xp >= (4*(lvl ** 3)) / 5 :
                            cursor.execute("UPDATE `s168073_members`.`members` SET exp = %s, lvl = %s WHERE member_id = %s", (0, lvl+1 ,member.id))
                            lvl = lvl + 1

                        db.commit()
                finally:
                    db.close()
            except Exception as ex:
                print("message")
                print(ex)
    @commands.has_permissions(administrator = True)
    @commands.command()
    async def shop(self , ctx):
        author_id = ctx.author.id
        try:
            db = pymysql.connect(**config)
            try:
                with db.cursor() as cursor:    
                    
                    cursor.execute("SELECT * FROM `s168073_members`.`members` WHERE member_id = %s", author_id)
                    user = cursor.fetchall()[0]
                    money = user[1]
                    potion = disnake.ui.Button(style = ButtonStyle.primary,  label = "Купить зелье", custom_id= "potion" )
                    bow = disnake.ui.Button(style = ButtonStyle.primary, label = "Купить лук", custom_id = "bow")
                    sw = disnake.ui.Button(style = ButtonStyle.primary, label = "Купить [10000 SC]", custom_id = "sw+")
                    aboutsw=disnake.ui.Button(style= ButtonStyle.url, label="Подробнее", url="https://solidworld-1.gitbook.io/solidworld/podderzhka-servera/sponsor-sw+")
                    aboutswplus=disnake.ui.Button(style= ButtonStyle.url, label="Подробнее", url="https://solidworld-1.gitbook.io/solidworld/podderzhka-servera/sponsor+-sw++")
                    swplus = disnake.ui.Button(style = ButtonStyle.primary, label = "Купить [20000 SC]", custom_id = "sw++")
                    await ctx.send(embed = disnake.Embed(title="ПОДПИСКА SOLIDWORLD+ НА 1 МЕСЯЦ ", description = "Временная подписка SW+ на 30 дней", colour = 0xa103d3 ),components=[ActionRow(sw, aboutsw)])
                    await ctx.send(embed = disnake.Embed(title="ПОДПИСКА SOLIDWORLD++ НА 1 МЕСЯЦ ", description = "Временная подписка SW++ на 30 дней", colour = 0xa103d3),components=[ActionRow(swplus, aboutswplus)])
            finally:
                db.close()
        except Exception as ex:
            print(ex)
    
    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        author_id = str(inter.author.id)
        author = inter.author
        custom = inter.component.custom_id
        if custom  == "sw+":
            try:
                db = pymysql.connect(**config)
                try:
                    with db.cursor() as cursor:    
                        
                        cursor.execute("SELECT * FROM `s168073_members`.`members` WHERE member_id = %s", author_id)
                        user = cursor.fetchall()[0]
                        money = user[1]
                        if money >= 10000:
                            cursor.execute("UPDATE `s168073_members`.`members` SET money = %s WHERE member_id = %s", (money - 10000 ,author_id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_members`.`members` WHERE member_id = %s", author_id)
                            user = cursor.fetchall()[0]
                            money = user[1]
                            await inter.send("Товар был куплен", ephemeral= True)
                        else:
                            await inter.send(f"Вам не хватает средст, ваш баланс - {money}")
                finally:
                    db.close()
            except Exception as ex:
                print(ex)
        if custom == "sw++":
            try:
                db = pymysql.connect(**config)
                try:
                    with db.cursor() as cursor:
                        cursor.execute("SELECT * FROM `s168073_members`.`members` WHERE member_id = %s", author_id)   
                        user = cursor.fetchall()[0]
                        money = user[1] 
                        if money >= 20000:
                            cursor.execute("UPDATE `s168073_members`.`members` SET money = %s WHERE member_id = %s", (money - 2000 ,author_id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_members`.`members` WHERE member_id = %s", author_id)
                            user = cursor.fetchall()[0]
                            money = user[1]
                            await inter.send("Товар был куплен", ephemeral= True)
                        else:
                            await inter.send(f"Вам не хватает средст, ваш баланс - {money}")
                        
                        
                       
                finally:
                    db.close()
            except Exception as ex:
                print(ex)
    
    @commands.has_permissions(administrator = True)
    @commands.slash_command()
    async def give(self, member: disnake.Member, money: int,  inter: disnake.AppCmdInter):
        #Работа с бд
        try:
            db = pymysql.connect(**config)
            emsend = disnake.Embed(title=f"{member} было отправленно {money} монет")
            try:
                with db.cursor() as cursor:
                    cursor.execute("SELECT * FROM `s168073_members`.`members` WHERE  member_id = %s", member.id)
                    user = cursor.fetchall()[0]
                    user_money = user[3]
                    cursor.execute("UPDATE `s168073_members`.`members` SET money = %s WHERE member_id =%s", (user_money+money, member.id))
                    db.commit()
                    await inter.send(embed=emsend, ephemeral=True)
            finally:
                db.close()
        except Exception as ex:
            print("Bad")
            print(ex)
    
    @commands.has_permissions(administrator = True)
    @commands.slash_command()
    async def remove(self, member: disnake.Member ,money: int , inter: disnake.AppCmdInter):
        #Работа с бд
        try:
            db = pymysql.connect(**config)
            emsend = disnake.Embed(title=f"Баланс {member} был уменьшен на {money} монет")
            try:
                with db.cursor() as cursor:
                    cursor.execute("SELECT * FROM `s168073_members`.`members` WHERE  member_id = %s", member.id)
                    user = cursor.fetchall()[0]
                    user_money = user[3]
                    cursor.execute("UPDATE `s168073_members`.`members` SET money = %s WHERE member_id = %s",(user_money - money, member.id) )
                    db.commit()
                    await inter.send(embed=emsend, ephemeral=True)
            finally:
                db.close()
        except Exception as ex:
            print("Bad")
            print(ex)
    @commands.slash_command()
    async def ranke(self,inter: disnake.AppCmdInter, member: disnake.Member = None):
        if member is None : 
            member = inter.author
        try:
            db = pymysql.connect(**config)
            try:
                with db.cursor() as cursor:
                    cursor.execute("SELECT * FROM `s168073_members`.`members` WHERE  member_id = %s", member.id)
                    user = cursor.fetchall()[0]
                    lvl = user[3]
                    money = user[4]
                    xp = user[5]
                    inventar = ast.literal_eval(user[6])
            finally:
                db.close()
        except Exception as ex:
            print("Bad")
            print(ex)
        await inter.response.defer()
        if xp == 0.0: 
            percentage = 0
        else:
            percentage = ( (xp / ((4*(lvl ** 3)) / 5 )) )
        i = inventar['card']
        background = Image.open(f'assets/card/{i}.png')

        def averagePixels(imageName):
            imgData = imageName.load()
            r, g, b = 0, 0, 0
            count = 0
            for x in range(imageName.size[0]) :
                for y in range(imageName.size[1]):
                    tempr,tempg,tempb,tempf = imgData[x,y]
                    r += tempr
                    g += tempg
                    b += tempb
                    count += 1
            return (r/count), (g/count), (b/count), count
        PixelColor = averagePixels(background)

        #====
        fp = io.BytesIO()
        #====== BAR
        drawObject = ImageDraw.Draw(background)
        x1 =360
        y1 = 308
        w1 = 1328
        h1 = 60
        color = "white"
        drawObject.ellipse((x1+w1,y1,x1+h1+w1,y1+h1),fill=color)    
        drawObject.ellipse((x1,y1,x1+h1,y1+h1),fill=color)    
        # drawObject.rectangle((x1+(h1/2),y1, x1+w1+(h1/2), y1+h1),fill=color)             #====== Bar- Color
        x1 =365
        y1 = 315
        w1 = 1295
        h1 = 46
        w1 = w1*percentage  
        drawObject.ellipse((x1+w1,y1,x1+h1+w1,y1+h1),fill=(round(PixelColor[0]),round(PixelColor[1]),round(PixelColor[2])))    
        drawObject.ellipse((x1,y1,x1+h1,y1+h1),fill=(round(PixelColor[0]),round(PixelColor[1]),round(PixelColor[2])))    
        drawObject.rectangle((x1+(h1/2),y1, x1+w1+(h1/2), y1+h1),fill=(round(PixelColor[0]),round(PixelColor[1]),round(PixelColor[2])))
        #=====
        money_len = len(str(money))
        money_avatar = Image.open('assets\sources\money_avatar.png')
        money_lines = Image.open('assets\sources\money_lines.png').resize((1300+money_len*100, 400))
        money_x = 1427
        money_y = 50
        background.paste(money_lines, (money_x-money_len*30,25), mask=money_lines)
        background.paste(money_avatar, (money_x-money_len*30+20,40), mask=money_avatar)
        #===== AVATAR
        def add_corners(image, radius):
            mask = Image.new('L', image.size) # filled with black by default
            draw = aggdraw.Draw(mask)
            brush = aggdraw.Brush('white')
            width, height = mask.size
            #upper-left corner
            draw.pieslice((0,0,radius*2, radius*2), 90, 180, None, brush)
            #upper-right corner
            draw.pieslice((width - radius*2, 0, width, radius*2), 0, 90, None, brush)
            #bottom-left corner
            draw.pieslice((0, height - radius * 2, radius*2, height),180, 270, None, brush)
            #bottom-right corner
            draw.pieslice((width - radius * 2, height - radius * 2, width, height), 270, 360, None, brush)
            #center rectangle
            draw.rectangle((radius, radius, width - radius, height - radius), brush)
            #four edge rectangle
            draw.rectangle((radius, 0, width - radius, radius), brush)
            draw.rectangle((0, radius, radius, height-radius), brush)
            draw.rectangle((radius, height-radius, width-radius, height), brush)
            draw.rectangle((width-radius, radius, width, height-radius), brush)
            draw.flush()
            image = image.convert('RGBA')
            image.putalpha(mask)   
            return image
        link = str(member.avatar)
        filename = f"{member.name}.png"
        r = requests.get(link, allow_redirects=True)
        open(filename, "wb").write(r.content)
        profile = Image.open(f"{member.name}.png").resize((300,300))
        profile = add_corners(profile, 150)
        background.paste(im=profile, box=(43,56), mask=profile)
        #=====
        
        #=====TEXT LVL
        draw = ImageDraw.Draw(background)
        font_name= ImageFont.truetype(font = "\assets\sources\assets\junegull_rg.ttf",size = 56)
        font_text = ImageFont.truetype(font = "\assets\sources\assets\junegull_rg.ttf", size = 30)
        draw.text(xy = (1507, 236), font = font_name , text = f"{xp}/{((4*(lvl ** 3)) / 5 )}", fill = (255,255,255))
        #=====TEXT NAME
        draw.text(xy=(360,227),font = font_name,text= f"{member.display_name}", fill=(255,255,255))
        #=====
        draw.text(xy=(money_x-money_len*30+70,42),font = font_text, text=f"{money}", fill= (255,255,255))
        #=====Circl nean avatar
        x =193
        y = 205
        p1=round(PixelColor[0])
        p2=round(PixelColor[1])
        p3= round(PixelColor[2])
        draw.arc((x-160, y-160, x+160,y+160), width= 6, start = -90, end = 100, fill=(p1,p2,p3))
        background.save(fp, "PNG")
        fp.seek(0)
        background.close()
        background = File(fp=fp , filename="card.png")
        emrank = disnake.Embed(title = None)
        emrank.set_image(file=background)
        
        await inter.send(embed=emrank)

        
        
        
def setup(bot):
    bot.add_cog(Lvl(bot))