import disnake 
import disnake
import asyncio
from disnake.ext import commands, tasks
from disnake.ext import *
from disnake import *
from disnake.ui import *
import datetime
from datetime import timedelta , datetime
from easy_pil import Editor, Canvas, Font, font
import pymysql
import requests
from confi import config, host, passwd , port

class Mod(commands.Cog): 
    def __init__(self, bot) :
        self.bot = bot
        self.guild = ' '
    @commands.slash_command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: disnake.Member, *, reason = None):
        if ctx.author.guild_permissions.kick_members and member.mention != ctx.author.mention:
            await member.kick(reason=reason)
            emb = disnake.Embed( title = ' ', colour = disnake.Color.red())
            emb.set_author(name = member.mention, icon_url = member.avatar.url)
            emb.add_field(name ='Kick', value =f'{member.mention} был кикнут ')
            emb.set_footer(text = f'{member.mention} Был кикнут участником {ctx.author.name}', icon_url = member.avatar.url)
            await ctx.send(embed = emb)
        elif member.mention == ctx.author.mention :
            emnekcik = disnake.Embed( title = ' ', colour = disnake.Color.red())
            emnekcik.add_field(name = 'Вы не можите кикнуть самого себя', value ='!!!'  )
            await ctx.send(embed = emnekcik)
    @commands.slash_command()
    @commands.has_permissions(ban_members = True )
    async def ban (self, inter:AppCmdInter, member: disnake.Member, reason = None ):
        chanal = inter.guild.get_channel(1205564085974999132)
        await member.ban()
        try:
            db = pymysql.connect(**config)
            try:
                with db.cursor() as cursor:
                    cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET warns = %s WHERE member_id = %s", (2, member.id))
                    ban_member = cursor.execute("SELECT member_id FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", str(member.id))[1]
                    db.commit()                
            finally:
                db.close()
        except Exception as ex:
            print("Bad")
            print(ex)
        client = cl(host = host, port = port, passwd=passwd) 
        client.connect(login= True)      
        client.ban(player=f"{ban_member}", reason = f"{reason}")
        client.close()
        await inter.response.defer()
        link = str(member.display_avatar)
        filename = f"{member.name}.png"
        r = requests.get(link, allow_redirects=True)
        open(filename, "wb").write(r.content)
        Mutebackground = Editor(f"/home/container/SolidBot/assets/Modcard/BANIMBA.png")
        Jungl = Font(path ='/home/container/SolidBot/assets/junegull rg.ttf', size=40)
        MutedBro = Editor(f"{member.name}.png").resize((160,160)).circle_image()
        Mutebackground.paste(MutedBro.image, (432,427))
        Mutebackground.text((500,675), f"{member.display_name} был забанен ",align="center", font=  Jungl, color= '#4682B4')
        Mutebackground.text((500,725), f"Причина: {reason}",align="center", font=  Jungl, color= '#4682B4')
        file = File(fp = Mutebackground.image_bytes, filename="card.png")
        await chanal.send(file=file)
    @commands.slash_command()
    @commands.has_permissions(manage_messages = True)
    async def clear(inter: disnake.CommandInteraction, amount):
        
        emoj = disnake.Embed(title = "Ожидайте...", colour = disnake.Color.dark_gold())
        await inter.send(embed = emoj, ephemeral= True )
        await inter.channel.purge(limit = int(amount))
        embdel = disnake.Embed( title = 'Clear ', colour = disnake.Color.dark_gray())
        embdel.add_field(name = f'**удалено {amount}**', value =':)' )
        await inter.edit_original_message(embed = embdel)
    @commands.slash_command(aliases = ['мьют', 'мут'], auto_sync= True)
    @commands.has_permissions(mute_members = True)
    async def mute(self, inter:AppCmdInter, reason , member: disnake.Member, sec: int = 0, min: int = 0, hours: int = 0 , days: int = 0,  weeks: int= 0):
        chanal = inter.guild.get_channel(1205564085974999132)
        delta = timedelta(
            days=days,
            seconds=sec,
            microseconds=0,
            milliseconds=0,
            minutes=min,
            hours=hours,
            weeks=weeks
        )
        await member.timeout(duration = delta, reason = reason )
        await inter.response.defer()
        link = str(member.display_avatar)
        filename = f"{member.name}.png"
        r = requests.get(link, allow_redirects=True)
        open(filename, "wb").write(r.content)
        
        Mutebackground = Editor(f"/home/container/SolidBot/assets/Modcard/MUTEIMBA.png").resize((1022,1080))
        Jungl = Font(path ='/home/container/SolidBot/assets/junegull rg.ttf', size=40)
        MutedBro = Editor(f"{member.name}.png").resize((160,160)).circle_image()
        Mutebackground.paste(MutedBro.image, (432,410))
        Mutebackground.text((500,675), f"{member.display_name} был наказан на: ",align="center", font=  Jungl, color= '#4682B4')
        Mutebackground.text((500,725), f"{delta}",align="center",font=Jungl,  color= '#4682B4')
        Mutebackground.text((500,775), f"По причине: {reason}",align="center", font =  Jungl, color= '#4682B4')
        
        file = File(fp = Mutebackground.image_bytes, filename="card.png")
        await inter.send("Успешно", ephemeral= True)
        await chanal.send(file=file)
        #--------------------------
    @commands.slash_command(aliases = ['анмьют', 'анмут'], auto_sync= True)
    @commands.has_permissions(mute_members = True)
    async def unmute(self,inter:AppCmdInter, member: disnake.Member,reason: str = None):   
        chanal = inter.guild.get_channel(1205564085974999132)
        delta = timedelta(
            days=0,
            seconds=0,
            microseconds=0,
            milliseconds=0,
            minutes=0,
            hours=0,
            weeks=0
        )
        await member.timeout(duration = delta, reason= reason)
        await inter.response.defer()
        link = str(member.display_avatar)
        filename = f"{member.name}.png"
        r = requests.get(link, allow_redirects=True)
        open(filename, "wb").write(r.content)
        
        Mutebackground = Editor(f"/home/container/SolidBot/assets/Modcard/unmute.png").resize((1022,1080))
        Jungl = Font(path ='/home/container/SolidBot/assets/junegull rg.ttf', size=40)
        MutedBro = Editor(f"{member.name}.png").resize((160,160)).circle_image()
        Mutebackground.paste(MutedBro.image, (432,380))
        Mutebackground.text((500,650), f" C игрока {member.display_name} был снят Мьют ",align="center", font=  Jungl, color= '#4682B4') 
        if reason != None:
            Mutebackground.text((500,725), f"Причина: {reason}",align="center", font =  Jungl, color= '#4682B4')
        file = File(fp = Mutebackground.image_bytes, filename="card.png")
        await chanal.send(file=file)
    @commands.slash_command()
    @commands.has_permissions(ban_members = True )
    async def warn(self, inter: AppCmdInter, member: disnake.Member, reason):
        chanal = inter.guild.get_channel(1205564085974999132)
        try:
            db = pymysql.connect(**config)
            try:
                with db.cursor() as cursor:
                    cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE  member_id = %s", member.id)
                    user = cursor.fetchall()[0]
                    warns = user[7]
                    cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET warns = %s WHERE member_id = %s", (warns+1, member.id))
                    db.commit()
                    cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE  member_id = %s", member.id)
                    user = cursor.fetchall()[0]
                    warns = user[7]
                    await inter.response.defer()
                    link = str(member.display_avatar)
                    filename = f"{member.name}.png"
                    r = requests.get(link, allow_redirects=True)
                    open(filename, "wb").write(r.content)
                    if warns == 3:
                        await member.ban()
                        cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET warns = %s WHERE member_id = %s", (2, member.id))
                        db.commit()
                        Mutebackground = Editor(f"/home/container/SolidBot/assets/Modcard/banwarn.png")
                        Jungl = Font(path ='/home/container/SolidBot/assets/junegull rg.ttf', size=40)
                        MutedBro = Editor(f"{member.name}.png").resize((160,160)).circle_image()
                        Mutebackground.paste(MutedBro.image, (432,420))
                        Mutebackground.text((500,675), f"{member.display_name} был забанен ",align="center", font=  Jungl, color= '#4682B4')
                        Mutebackground.text((500,725), f"Причина: {reason}",align="center", font=  Jungl, color= '#4682B4')
                        file = File(fp = Mutebackground.image_bytes, filename="banwarn.png")
                        await inter.send("Успешно", ephemeral= True)
                        await chanal.send(file=file)
                    else:
                        Mutebackground = Editor(f"/home/container/SolidBot/assets/Modcard/warn.png")
                        Jungl = Font(path ='/home/container/SolidBot/assets/junegull rg.ttf', size=40)
                        MutedBro = Editor(f"{member.name}.png").resize((160,160)).circle_image()
                        Mutebackground.paste(MutedBro.image, (432,427))
                        Mutebackground.text((500,675), f"{member.display_name} был выдан варн ",align="center", font=  Jungl, color= '#4682B4')
                        Mutebackground.text((500,725), f"Причина: {reason}",align="center", font=  Jungl, color= '#4682B4')
                        file = File(fp = Mutebackground.image_bytes, filename="warn.png")
                        if warns==1: i = "варн"
                        else: i = "варнов"
                        await member.send(f"Вам был вадан варн\nНа данный момент у вас {warns} {i}")
                        await inter.send("Успешно", ephemeral= True)
                        await chanal.send(file=file)                    
            finally:
                db.close()
        except Exception as ex:
            print("Bad")
            print(ex)
    @commands.slash_command()
    @commands.has_permissions(ban_members = True )
    async def unwarn(self, inter: AppCmdInter, member: disnake.Member, reason):
        chanal = inter.guild.get_channel(1205564085974999132)
        try:
            db = pymysql.connect(**config)
            try:
                with db.cursor() as cursor:
                    cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE  member_id = %s", member.id)
                    user = cursor.fetchall()[0]
                    warns = user[7]
                    cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET warns = %s WHERE member_id = %s", (warns-1, member.id))
                    db.commit()
                    cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE  member_id = %s", member.id)
                    user = cursor.fetchall()[0]
                    warns = user[7]
                    await inter.response.defer()
                    link = str(member.display_avatar)
                    filename = f"{member.name}.png"
                    r = requests.get(link, allow_redirects=True)
                    open(filename, "wb").write(r.content)
                    Mutebackground = Editor(f"/home/container/SolidBot/assets/Modcard/unwarn.png")
                    Jungl = Font(path ='/home/container/SolidBot/assets/junegull rg.ttf', size=40)
                    MutedBro = Editor(f"{member.name}.png").resize((160,160)).circle_image()
                    Mutebackground.paste(MutedBro.image, (432,427))
                    Mutebackground.text((500,675), f"С {member.display_name} снят варн ",align="center", font=  Jungl, color= '#4682B4')
                    Mutebackground.text((500,725), f"Причина: {reason}",align="center", font=  Jungl, color= '#4682B4')
                    file = File(fp = Mutebackground.image_bytes, filename="warn.png")
                    if warns==1: i = "варн"
                    else: i = "варнов"
                    await member.send(f"С вас был снят варн\nНа данный момент у вас {warns} {i}")
                    await inter.send("Успешно", ephemeral= True)
                    await chanal.send(file=file)                    
            finally:
                db.close()
        except Exception as ex:
            print("Bad")
            print(ex)
        
def setup(bot):
    bot.add_cog(Mod(bot))