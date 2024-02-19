import disnake 
import disnake
from disnake.ext import commands
from disnake.ext import *
from disnake import *
from disnake.ui import *
import random 

class VER(commands.Cog): 
    def __init__(self, bot) :
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(administrator = True )
    async def ver(ctx):
        two= Button(style = ButtonStyle.url,  label = "Прочитайте правила ", url = "https://discord.com/channels/1125825837791449210/1195803292048048208")
        one = Button(style = ButtonStyle.primary,  label = "🔑Пройти верефикацию!", custom_id= "verr")
        emver = disnake.Embed(title = " ", colour = disnake.Color.dark_gold())
        emver.add_field(name = "Верефикация! ", value = "Вы должны пройти верефикацию, что бы мы убедились, что вы не робочеловек!")
        await ctx.send(embed = emver, components= [ActionRow(one, two)])
        
    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        two= Button(style = ButtonStyle.url,  label = "Прочитайте правила ", url = "https://discord.com/channels/1125825837791449210/1195803292048048208")
        emtest1 = disnake.Embed(title= " ", colour =  disnake.Color.dark_gold())
        emtest1.add_field(name = "Вы прошли верефикацию!", value = "`Развлекайтесь!`")
        custom = inter.component.custom_id
        if str(custom) == "verr":
            await inter.author.remove_roles(disnake.utils.get(inter.guild.roles, name="Не верифициорванный"))
            await inter.author.add_roles(disnake.utils.get(inter.guild.roles, name="⌜🔥⌟  Верифицированный") )
            await inter.send(embed = emtest1, ephemeral= True)
                

        



def setup(bot):
    bot.add_cog(VER(bot))