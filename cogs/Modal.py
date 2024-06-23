import disnake
import asyncio
import asyncpg
from disnake.ext import commands
from disnake import *
from disnake.ui import *
import os
import pymysql
from confi import config
class Modal(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
#---# Создание модуля 
    @commands.has_permissions(administrator = True)
    @commands.slash_command(auto_sync = True)
    async def news(inter: disnake.AppCmdInter): 
        # Создание модуля 
        class mymodal(disnake.ui.Modal):
            def __init__(self):
                components = [
                    disnake.ui.TextInput(
                        label="Title",
                        placeholder="",
                        custom_id="name",
                        style=TextInputStyle.short,
                        max_length=50,
                    ),
                    disnake.ui.TextInput(
                label="Description",
                placeholder="Lorem ipsum dolor sit amet.",
                custom_id="описание",
                style=TextInputStyle.paragraph,
            ),
            disnake.ui.TextInput(
                    label="Ссылку на изображение",
                    placeholder="0 если нет изображения",
                    custom_id="url",
                    style=TextInputStyle.short,
                ),
        ]
                super().__init__(title="Объявление", components = components)
# ивент откликается на создание модуля 
            @commands.Cog.listener()
            async def callback(self, inter: disnake.ModalInteraction):
                embed1 = disnake.Embed(title=f"Извините, но вам придется разделить сообщение т.к. максимальное колличество символов 1024")
                for key, value in inter.text_values.items():
                    embed = disnake.Embed(title=f"{value}")
                    del inter.text_values[f'{key}']
                    break
                for key, value in inter.text_values.items():
                    if key == "url" and value != "0" :
                        embed.set_image(url=f"{value}")
                        del inter.text_values[f'{key}']
                        break
                    elif key == "url" and value == "0":
                        del inter.text_values[f'{key}']
                        break
                for key, value in inter.text_values.items():
                    if len(value)>1024:
                        await inter.response.send_message(embed=embed1, ephemeral=True, delete_after = True)
                    else:
                        embed.add_field(
                                name = "",
                                value= value[:1024],
                                inline=False,
                            )
                await inter.response.send_message("Пост успешно опублекован", ephemeral=True)
                await inter.channel.send(embed=embed)
        await inter.response.send_modal(modal = mymodal() )
#------------------------------------#
    @commands.slash_command(auto_sync=True)
    async def trade(inter: disnake.AppCmdInter):
        author = inter.author
        class tradeModal(disnake.ui.Modal):
            def __init__(self):
                components = [ 
                    disnake.ui.TextInput(
                    label="Покупаете/Продаете? ",
                    placeholder="Покупаю/Продаю",
                    custom_id="описание1",
                    style=TextInputStyle.short,
                ),
                disnake.ui.TextInput(
                            label="Товар",
                            placeholder="",
                            custom_id="name",
                            style=TextInputStyle.paragraph,
                            max_length=100,
                        ),
                disnake.ui.TextInput(
                    label="Ссылку на изображение",
                    placeholder="0 если нет изображения",
                    custom_id="url",
                    style=TextInputStyle.short,
                ),
            ]
                super().__init__(title="Обмен", components = components)
            @commands.Cog.listener()
            async def callback(self, inter: disnake.ModalInteraction):
                class sellButton(disnake.ui.View):
                            def __init__(self):
                                super().__init__(timeout=None)
                            @disnake.ui.button(label="Купить",  style=ButtonStyle.green)
                            async def buyButton(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                                button_author = inter.author
                                if button_author != author:
                                    await author.send(embed=disnake.Embed(title=f"{button_author} хочет купить вашь товар"))
                                else:
                                    await inter.send("Вы не можите покупать у самого себя )", ephemeral= True)
                            @disnake.ui.button(label="Купленно",  style=ButtonStyle.green)
                            async def sellButton(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                                self.buyButton.disabled = True
                                self.sellButton.disabled = True
                                button_author = inter.author
                                if button_author != author:
                                    await inter.send(embed=disnake.Embed(title=f"Это не вашь трейд"), ephemeral=True)
                                else:
                                    await inter.response.edit_message(embed=disnake.Embed(title="Проданно"),view = self)
                                    self.stop()
                class buyButton(disnake.ui.View):
                    def __init__(self):
                        super().__init__(timeout=None)
                        
                    @disnake.ui.button(label="Продать",  style=ButtonStyle.green)
                    async def buyButton(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                        button_author = inter.author
                        if button_author != author:
                            await author.send(embed=disnake.Embed(title=f"{button_author} хочет продать вам товар"))
                        else:
                            await inter.send("Вы не можите продать сами себе )", ephemeral= True)
                        
                    @disnake.ui.button(label="Купленно",  style=ButtonStyle.green)
                    async def sellButton(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                        self.buyButton.disabled = True
                        self.sellButton.disabled = True
                        button_author = inter.author
                        if button_author != author:
                            await inter.send(embed=disnake.Embed(title=f"Это не вашь трейд"), ephemeral=True)
                        else:
                            await inter.response.edit_message(embed=disnake.Embed(title="Проданно"),view = self)
                            self.stop()
                embed1 = disnake.Embed(title=f"Извините, но вам придется разделить сообщение т.к. максимальное колличество символов 1024")
                for key, value in inter.text_values.items():
                    embed = disnake.Embed(title=f"{value}")
                    if value == "Продаю":
                        classe = sellButton()
                    elif value == "Покупаю":
                        classe = buyButton()
                    del inter.text_values[f'{key}']
                    break
                for key, value in inter.text_values.items():
                    if key == "url" and value != "0" :
                        embed.set_image(url=f"{value}")
                        del inter.text_values[f'{key}']
                        break
                    elif key == "url" and value == "0":
                        del inter.text_values[f'{key}']
                        break
                embed.set_thumbnail(url= inter.author.display_avatar.url)
                embed.set_author(name = f"{inter.author.name}")
                await inter.send(embed=embed, view=classe)
        await inter.response.send_modal(modal = tradeModal())
#===================
        # For dynamic items, we must register the classes instead of the views.
        
#------------------------------------#
    @commands.command(auto_sync=True)
    async def app(self, inter: disnake.AppCmdInter):
        embeds = disnake.Embed(title = "Заявка", colour=disnake.Color.dark_magenta())
        rules = Button(style = ButtonStyle.url ,label = "Прочитайте правила", url = inter.guild.get_channel(1195803292048048208).jump_url)
        app_button = Button(style = ButtonStyle.green,label = "Заявка", custom_id = 'app')
        embeds.add_field(name = f"Нажав на кнопку и заполнив анкету, вы узнаете приняли ли вас)\nПеред падачей завки прочитайте правила", value="Удачи!")
        await inter.send(embed = embeds, components=[ActionRow(app_button,rules)])
#------------------------------------#     
    @commands.slash_command(auto_sync=True)
    async def tickets(self, inter: AppCmdInter):
        embeds = disnake.Embed(title=f"{'**Поддержка**'}")
        embeds.add_field(name=f"{''}", value='**Возникли вопросы? Нужна помощь? Есть предложения? Открывай тикет и пиши на прямую администрации**')
        class tickets(disnake.ui.View):
            def __init__(self):
                super().__init__(timeout = None)
            @disnake.ui.button(label="Создать тикет",custom_id='tick', style=ButtonStyle.blurple)
            async def tick(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                member = inter.guild.get_member(381559648655769600)
        await inter.send(embed=embeds, view=tickets())
#------------------------------------#
    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        member = inter.author
        custom = inter.component.custom_id
        if custom == "app":
            soadmin = inter.guild.get_member(381559648655769600)
            admin = inter.guild.get_member(575156428571148298)
            class applc(disnake.ui.Modal):
                    def __init__(self):
                            components = [
                                disnake.ui.TextInput(
                                    label="ВАШ НИКНЕЙМ В ИГРЕ",
                                    placeholder="",
                                    custom_id="Никнейм",
                                    style=TextInputStyle.short,
                                    max_length=50,
                                ),
                                disnake.ui.TextInput(
                            label="ВАШ ВОЗРАСТ",
                            placeholder="1000000",
                            custom_id="Сколько лет",
                            style=TextInputStyle.paragraph,
                            max_length=1024,
                        ),
                                disnake.ui.TextInput(
                            label="ОЗНАКОМЛЕНЫ ЛИ ВЫ С ПРАВИЛАМИ СЕРВЕРА",
                            placeholder="",
                            custom_id="Ознакомлены ли вы с правилами сервера?",
                            style=TextInputStyle.paragraph,
                            max_length=1024,
                        ),
                                disnake.ui.TextInput(
                            label="РАЗРЕШЕНО ЛИ ГРИФЕРСТВО?",
                            placeholder="",
                            custom_id="Разрешено ли греферство?",
                            style=TextInputStyle.paragraph,
                            max_length=1024,
                        ),
                                disnake.ui.TextInput(
                            label="ОТКУДА ВЫ УЗНАЛИ О НАШЕМ СЕРВЕРЕ?",
                            placeholder="",
                            custom_id="Откуда вы узнали о нашем сервере?",
                            style=TextInputStyle.paragraph,
                            max_length=1024,
                        ),
                    ]
                            super().__init__(title="Объявление", components = components)
                    @commands.Cog.listener()
                    async def callback(self, inter: disnake.ModalInteraction):
                        roles = inter.guild.get_role(1134133648925397063)
                        class trust_or_not(disnake.ui.View):
                            def __init__(self):
                                super().__init__(timeout= None)
                            @disnake.ui.button(label="Принять", style=ButtonStyle.blurple)
                            async def trustbut(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                                await member.send("Вашая заявка была принята!")
                                await member.add_roles(roles)
                                
                            @disnake.ui.button(label="Отклонить", style=ButtonStyle.blurple)
                            async def nottrustbut(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                                   await member.send("Вашая заявка была отклонена!")
                        for key, value in inter.text_values.items():
                            embed = disnake.Embed(title=f"{key}", description=f"{value}")
                            try:
                                db = pymysql.connect(**config)
                                try:
                                    with db.cursor() as cursor:
                                        cursor.execute("UPDATE `s168073_members`.`members` SET minecraft_nick = %s WHERE member_id = %s", (value, member.id))
                                        db.commit()
                                finally:
                                    db.close()
                            except Exception as ex : 
                                print("Bad1")
                                print(ex)
                            del inter.text_values[f'{key}']
                            break
                        for key, value in inter.text_values.items():
                            embed.add_field(name=f"{key}", value = f"{value}", inline = False)
                        embed.set_thumbnail(url= inter.author.display_avatar.url)
                        embed.set_author(name = f"{member.name}")
    
                        await inter.response.send_message("Ваша заявка была подана", ephemeral=True)
                        await admin.send(embed=embed,view=trust_or_not())
                        await soadmin.send(embed=embed,view=trust_or_not())
            await inter.response.send_modal(modal = applc()) 
        if custom == "tick":
            member = inter.author
            class closebutton(disnake.ui.View):
                def __init__(self):
                    super().__init__(timeout=None)
                @disnake.ui.button(label="Закрыть тикет",custom_id="close", style=ButtonStyle.red)
                async def close(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                    member=inter.author
                    
            embed = disnake.Embed(title= "Ticket")
            embed.add_field(name=f"{''}", value=f"Пожалуйста, опишите чем мы можем вам помочь {inter.author}\nОпишите все максимально подробно, для вашего же удобства")
                
            await inter.guild.create_text_channel(name =f"ticket - {inter.author}" , category=inter.guild.get_channel(1195826811108606022),overwrites={member: disnake.PermissionOverwrite(read_messages=True)})
            chanal = inter.guild.channels[-1]
            await inter.send(f"Тикет был создан {chanal.jump_url}", ephemeral=True)
            await chanal.send(embed=embed, view=closebutton())
        if custom == "close":
            overwrites = {
                            inter.guild.default_role: disnake.PermissionOverwrite(send_messages=False),
                            inter.guild.default_role: disnake.PermissionOverwrite(read_messages=False)
                            }
            await inter.send("Тикет был закрыт")
            await inter.channel.edit(name = f"Тикет - {inter.author}" , category=inter.guild.get_channel(1195844858506645574), overwrites=overwrites)
            

def setup(bot):
    bot.add_cog(Modal(bot)) 