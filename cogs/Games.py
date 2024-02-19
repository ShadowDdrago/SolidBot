import disnake
import asyncio
import asyncpg
from disnake.ext import commands
from disnake import member, Button, ButtonStyle
from disnake.ui import *
import os
import ast
import time 
import pymysql
import random
from confi import config
class Game(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.Game_start = False 
    @commands.command()
    async def faq(selc, ctx):
        await ctx.send("**Будем очень благодарны если вы поддержите наш проект!**")
        await ctx.send("[Чпок](https://solidworld.easydonate.ru/)")
    @commands.slash_command()
    async def knb(self, member: disnake.Member, inter: disnake.AppCmdInter): 
        author_command = inter.author
        self.users = member
        self.rec = True
        game_data = {}
        
        emgame = disnake.Embed(title="Камень Ножницы Бумага")
        emgame.add_field(name = f" Сейчас выбирает {self.users}", value="||Делайте выбор с умом||")
        
        
        class knbButtons(disnake.ui.View):
            def __init__(self):
                super().__init__(timeout= None)
                self.em = disnake.Embed(title="Проводятся самые сложные вычисления....")
            @disnake.ui.button(label="Камень🪨", style=ButtonStyle.blurple )
            async def stone_button(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):

                if len(game_data) == 0:
                    self.users = member
                    self.rounds = 1
                if len(game_data) == 1:
                    self.users = author_command
                    self.rounds = 2
    
                if inter.author == self.users:
                    game_data[self.users] = "1камень"
                    if self.rounds == 2:
                        if len(game_data) == (0 or 1): 
                            await inter.send(embed = disnake.Embed(title = "К сожелению один из вас не успел выбрать вариант ответа ( "))
                        else:
                            members_answer= int(game_data[member][0])
                            author_command_answer = int(game_data[author_command][0])
                            if (members_answer == 1  and author_command_answer== 1)  or (members_answer== 2 and author_command_answer== 2)  or (members_answer == 3  and author_command_answer == 3):
                                await inter.response.edit_message(embed=disnake.Embed(title="Ничья!"))
                            else:
                                if members_answer == 1 and author_command_answer == 2: winner=member
                                elif members_answer == 2 and author_command_answer == 3: winner= member
                                elif members_answer == 3 and author_command_answer == 1: winner= member
                                else: winner = author_command
                                await inter.response.edit_message(embed=disnake.Embed(title=f"В этом жесточайщем бою победил {winner.name}\n||{member} выбрал {game_data[member][1:10]}, {author_command} выбрал {game_data[author_command][1:10]}||"), view = None)
                    emgame = disnake.Embed(title="Камень Ножницы Бумага")
                    emgame.add_field(name = f" Сейчас выбирает {author_command}", value="||Делайте выбор с умом||")
                    if len(game_data) == 1:
                        await inter.response.edit_message(embed=emgame, view=knbButtons())
                else: 
                    await inter.send("Вы не были вызваны", ephemeral=True)
            @disnake.ui.button(label="Ножницы ✄", style=ButtonStyle.blurple )
            async def sc_button(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                if len(game_data) == 0:
                    self.users = member
                    self.rounds = 1
                if len(game_data) == 1:
                    self.users = author_command
                    self.rounds = 2
            
                if inter.author == self.users:
                    
                    game_data[self.users] = "2кожницы"
                    if self.rounds == 2:
                        if len(game_data) == (0 or 1): 
                            await inter.send(embed = disnake.Embed(title = "К сожелению один из вас не успел выбрать вариант ответа ( "))
                        else:
                            members_answer= int(game_data[member][0])
                            author_command_answer = int(game_data[author_command][0])
                            if (members_answer == 1  and author_command_answer== 1)  or (members_answer== 2 and author_command_answer== 2)  or (members_answer == 3  and author_command_answer == 3):
                                await inter.response.edit_message(embed=disnake.Embed(title="Ничья!"), view= None)
                            else:
                                if members_answer == 1 and author_command_answer == 2: winner=member
                                elif members_answer == 2 and author_command_answer == 3: winner= member
                                elif members_answer == 3 and author_command_answer == 1: winner= member
                                else: winner = author_command
                                await inter.response.edit_message(embed=disnake.Embed(title=f"В этом жесточайщем бою победил {winner.name}\n||{member} выбрал {game_data[member][1:10]}, {author_command} выбрал {game_data[author_command][1:10]}||"), view = None)
                    emgame = disnake.Embed(title="Камень Ножницы Бумага")
                    emgame.add_field(name = f" Сейчас выбирает {author_command}", value="||Делайте выбор с умом||")
                    if len(game_data) == 1:
                        await inter.response.edit_message(embed=emgame, view=knbButtons())
                else: 
                    await inter.send("Вы не были вызваны", ephemeral=True)
            @disnake.ui.button(label="Бумага📃", style=ButtonStyle.blurple )
            async def pa_button(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                if len(game_data) == 0:
                    self.users = member
                    self.rounds = 1
                if len(game_data) == 1:
                    self.users = author_command
                    self.rounds = 2
                    
                if inter.author == self.users:
                    game_data[self.users] = "3бумага"
                    if self.rounds == 2:
                        if len(game_data) == (0 or 1): 
                            await inter.send(embed = disnake.Embed(title = "К сожелению один из вас не успел выбрать вариант ответа ( "))
                        else:
                            members_answer= int(game_data[member][0])
                            author_command_answer = int(game_data[author_command][0])
                            if (members_answer == 1  and author_command_answer== 1)  or (members_answer== 2 and author_command_answer== 2)  or (members_answer == 3  and author_command_answer == 3):
                                await inter.response.edit_message(embed=disnake.Embed(title="Ничья!"),  view= None)
                            else:
                                if members_answer == 1 and author_command_answer == 2: winner=member
                                elif members_answer == 2 and author_command_answer == 3: winner= member
                                elif members_answer == 3 and author_command_answer == 1: winner= member
                                else: winner = author_command
                                await inter.response.edit_message(embed=disnake.Embed(title=f"В этом жесточайщем бою победил {winner.name}\n||{member} выбрал {game_data[member][1:10]}, {author_command} выбрал {game_data[author_command][1:10]}||"), view = None)
                    emgame = disnake.Embed(title="Камень Ножницы Бумага")
                    emgame.add_field(name = f" Сейчас выбирает {author_command}", value="||Делайте выбор с умом||")
                    if len(game_data) == 1:
                        await inter.response.edit_message(embed=emgame, view=knbButtons())   
                else: 
                    await inter.send("Вы не были вызваны", ephemeral=True)
            
                

        class acceptButtons(disnake.ui.View):
                def __init__(self):
                    super().__init__(timeout= 10)
                    
                    self.accept=False
                async def on_timeout(self):
                    if self.accept == False:
                        self.first_button.disabled = True
                        self.second_button.disabled = True
                        await inter.edit_original_message(embed = disnake.Embed(title = f"{member} не успел принять вызов"),view = self)
                        
                    
                    View.stop(self)
                    self.stop()
                @disnake.ui.button(label="Принять", style=ButtonStyle.green)
                async def first_button(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                    if inter.author == member:
                        self.accept = True
                        await inter.response.edit_message(embed=emgame, view=knbButtons())
                    else: 
                        await inter.send("Вы не были вызваны", ephemeral=True)
                    self.stop()
                @disnake.ui.button(label="Отказать", style=ButtonStyle.red)
                async def second_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
                    if inter.author == member:
                        self.accept = True
                        
                        await inter.response.edit_message(embed=disnake.Embed(title = f"{member} отказался от вызова"))
                    else: 
                        await inter.send("Вы не были вызваны", ephemeral=True)
                    self.stop()
                
        knbembeds = disnake.Embed(title = f"{inter.author.name} вызвал {member.name}")
        knbembeds.add_field(name = f"Примет ли {member.name} вызов ", value="У него есть 10 секунд")
        await inter.send(f"||{member.mention}||", embed  = knbembeds, view=acceptButtons())
        self.players ={member.id: inter.author} 
    @commands.slash_command()
    async def tic_tac_toe(self, member: disnake.Member, inter: disnake.AppCmdInter):
        # member - Нолики
        # author - Крестики
        # проверка на победу
       
        def is_win(spisok):
            if win_line in spisok:
                return True
            
            elif ((spisok[0][0] and spisok[1][0] and spisok[2][0] ) == 1) or ((spisok[0][1] and spisok[1][1] and spisok[2][1] ) == 1) or ((spisok[0][2] and spisok[1][2] and spisok[2][2])==1):
                return True
            elif (spisok[0][0] and spisok[1][1] and spisok[2][2] ) == 1 or (spisok[0][2] and spisok [1][1] and spisok[2][0]):
                return True
            return False
        win_line = [1,1,1]
        win_12=[[[1,0,0], [1,0,0], [1,0,0]],[ [0,1,0] , [0,1,0] , [0,1,0]]  ,[[0,0,1] , [0,0,1] , [0,0,1]]  , [[0,0,1] , [0,1,0] , [1,0,0]], [[1,0,0] , [0,1,0] , [0,0,1]]]
        author = inter.author
        tic_toc_em = disnake.Embed(title="Крестики   Нолики")
        tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Первым ходит {member}")
        try:
            db = pymysql.connect(**config)
            with db.cursor() as cursor:
                cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str([[0,0,0] for i in range(0,3)]), author.id))
                cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str([[0,0,0] for i in range(0,3)]), member.id))
                db.commit()
            db.close()
        except Exception as ex:
            print(ex)
        class cross(disnake.ui.View):
            def __init__(self):
                self.xod = member
                tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                super().__init__(timeout=None)
            #Декор
            @disnake.ui.button(label="ㅤ", style=ButtonStyle.blurple, row =0)
            async def but1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                
                try:
                    db = pymysql.connect(**config)
                    with db.cursor() as cursor:
                        #------------------------- Получение данных
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                        member_db = cursor.fetchall()[0]
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                        author_db = cursor.fetchall()[0]
                        member_games = ast.literal_eval(member_db[6])
                        author_games = ast.literal_eval(author_db[6])
                        member_games_count = member_games[0].count(0) + member_games[1].count(0) + member_games[2].count(0)
                        author_games_count = author_games[0].count(0) + author_games[1].count(0) + author_games[2].count(0)
                        
                        if author == inter.author and member_games_count != author_games_count:
                            self.xod = author
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but1.label = "X"
                            self.but1.disabled = True
                            author_games[0][0] = 1 
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(author_games), author.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                            author_db = cursor.fetchall()[0]
                            author_games = ast.literal_eval(author_db[6])
                            if is_win(author_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {author}"), view=self)
                                
                            else: await inter.response.edit_message(view=self)
                        elif member == inter.author and  author_games_count==member_games_count :
                            tic_toc_em = disnake.Embed(title="      Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.xod = member
                            self.but1.label = "O"
                            self.but1.disabled = True
                            member_games[0][0] = 1
                            
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(member_games), member.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                            member_db = cursor.fetchall()[0]
                            member_games = ast.literal_eval(member_db[6])
                            if is_win(member_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {member}"), view=self)
                            else: await inter.response.edit_message(view=self)
                            
                        db.commit()
                    db.close()
                
                except Exception as ex:
                    print(ex)
            
            @disnake.ui.button(label="ㅤ", style=ButtonStyle.blurple, row =0)
            async def but2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                try:
                    db = pymysql.connect(**config)
                    with db.cursor() as cursor:
                        #------------------------- Получение данных
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                        member_db = cursor.fetchall()[0]
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                        author_db = cursor.fetchall()[0]
                        member_games = ast.literal_eval(member_db[6])
                        author_games = ast.literal_eval(author_db[6])
                        member_games_count = member_games[0].count(0) + member_games[1].count(0) + member_games[2].count(0)
                        author_games_count = author_games[0].count(0) + author_games[1].count(0) + author_games[2].count(0)
                        
                        if author == inter.author and member_games_count != author_games_count:
                            self.xod = author
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but2.label = "X"
                            self.but2.disabled = True
                            author_games[0][1] = 1 
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(author_games), author.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                            author_db = cursor.fetchall()[0]
                            author_games = ast.literal_eval(author_db[6])
                            if is_win(author_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {author}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        elif member == inter.author and author_games_count == member_games_count:
                            self.xod = member
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but2.label = "O"
                            self.but2.disabled = True
                            member_games[0][1] = 1
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(member_games), member.id))
                            db.commit() 
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                            member_db = cursor.fetchall()[0]
                            member_games = ast.literal_eval(member_db[6])
                            if is_win(member_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {member}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        
                        #-------------------------
                        db.commit()
                    db.close()
                except Exception as ex:
                    print(ex)
            @disnake.ui.button(label="ㅤ", style=ButtonStyle.blurple, row =0)
            async def but3(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                try:
                    db = pymysql.connect(**config)
                    with db.cursor() as cursor:
                        #------------------------- Получение данных
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                        member_db = cursor.fetchall()[0]
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                        author_db = cursor.fetchall()[0]
                        member_games = ast.literal_eval(member_db[6])
                        author_games = ast.literal_eval(author_db[6])
                        member_games_count = member_games[0].count(0) + member_games[1].count(0) + member_games[2].count(0)
                        author_games_count = author_games[0].count(0) + author_games[1].count(0) + author_games[2].count(0)
                        
                        if author == inter.author and member_games_count != author_games_count:
                            self.xod = author
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but3.label = "X"
                            self.but3.disabled = True
                            author_games[0][2] = 1 
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(author_games), author.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                            author_db = cursor.fetchall()[0]
                            author_games = ast.literal_eval(author_db[6])
                            if is_win(author_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {author}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        elif member == inter.author and author_games_count == member_games_count:
                            self.xod = member
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but3.label = "O"
                            self.but3.disabled = True
                            member_games[0][2] = 1
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(member_games), member.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                            member_db = cursor.fetchall()[0]
                            member_games = ast.literal_eval(member_db[6])
                            if is_win(member_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {member}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        
                        #-------------------------
                        db.commit()
                    db.close()
                except Exception as ex:
                    print(ex)
            @disnake.ui.button(label="ㅤ", style=ButtonStyle.blurple, row =1)
            async def but4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                try:
                    db = pymysql.connect(**config)
                    with db.cursor() as cursor:
                        #------------------------- Получение данных
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                        member_db = cursor.fetchall()[0]
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                        author_db = cursor.fetchall()[0]
                        member_games = ast.literal_eval(member_db[6])
                        author_games = ast.literal_eval(author_db[6])
                        member_games_count = member_games[0].count(0) + member_games[1].count(0) + member_games[2].count(0)
                        author_games_count = author_games[0].count(0) + author_games[1].count(0) + author_games[2].count(0)
                        
                        if author == inter.author and member_games_count != author_games_count:
                            self.xod = author
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but4.label = "X"
                            self.but4.disabled = True
                            author_games[1][0] = 1 
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(author_games), author.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                            author_db = cursor.fetchall()[0]
                            author_games = ast.literal_eval(author_db[6])
                            if is_win(author_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {author}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        elif member == inter.author and author_games_count == member_games_count:
                            self.xod = member
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but4.label = "O"
                            self.but4.disabled = True
                            member_games[1][0] = 1
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(member_games), member.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                            member_db = cursor.fetchall()[0]
                            member_games = ast.literal_eval(member_db[6])
                            if is_win(member_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {member}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        
                        #-------------------------
                        db.commit()
                    db.close()
                except Exception as ex:
                    print(ex)
            @disnake.ui.button(label="ㅤ", style=ButtonStyle.blurple, row =1)
            async def but5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                try:
                    db = pymysql.connect(**config)
                    with db.cursor() as cursor:
                        #------------------------- Получение данных
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                        member_db = cursor.fetchall()[0]
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                        author_db = cursor.fetchall()[0]
                        member_games = ast.literal_eval(member_db[6])
                        author_games = ast.literal_eval(author_db[6])
                        member_games_count = member_games[0].count(0) + member_games[1].count(0) + member_games[2].count(0)
                        author_games_count = author_games[0].count(0) + author_games[1].count(0) + author_games[2].count(0)
                        
                        if author == inter.author and member_games_count != author_games_count:
                            self.xod = author
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but5.label = "X"
                            self.but5.disabled = True
                            author_games[1][1] = 1 
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(author_games), author.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                            author_db = cursor.fetchall()[0]
                            author_games = ast.literal_eval(author_db[6])
                            if is_win(author_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {author}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        elif member == inter.author and author_games_count == member_games_count:
                            self.xod = member
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but5.label = "O"
                            self.but5.disabled = True
                            member_games[1][1] = 1
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(member_games), member.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                            member_db = cursor.fetchall()[0]
                            member_games = ast.literal_eval(member_db[6])
                            if is_win(member_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {member}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        
                        #-------------------------
                        db.commit()
                    db.close()
                except Exception as ex:
                    print(ex)
            @disnake.ui.button(label="ㅤ", style=ButtonStyle.blurple, row =1)
            async def but6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                try:
                    db = pymysql.connect(**config)
                    with db.cursor() as cursor:
                        #------------------------- Получение данных
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                        member_db = cursor.fetchall()[0]
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                        author_db = cursor.fetchall()[0]
                        member_games = ast.literal_eval(member_db[6])
                        author_games = ast.literal_eval(author_db[6])
                        member_games_count = member_games[0].count(0) + member_games[1].count(0) + member_games[2].count(0)
                        author_games_count = author_games[0].count(0) + author_games[1].count(0) + author_games[2].count(0)
                        
                        if author == inter.author and member_games_count != author_games_count:
                            self.xod = author
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but6.label = "X"
                            self.but6.disabled = True
                            author_games[1][2] = 1 
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(author_games), author.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                            author_db = cursor.fetchall()[0]
                            author_games = ast.literal_eval(author_db[6])
                            if is_win(author_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {author}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        elif member == inter.author and author_games_count == member_games_count:
                            self.xod = member
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but6.label = "O"
                            self.but6.disabled = True
                            member_games[1][2] = 1
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(member_games), member.id))
                            db.commit() 
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                            member_db = cursor.fetchall()[0]
                            member_games = ast.literal_eval(member_db[6])
                            if is_win(member_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {member}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        
                        #-------------------------
                        db.commit()
                    db.close()
                except Exception as ex:
                    print(ex)
            @disnake.ui.button(label="ㅤ", style=ButtonStyle.blurple, row =2)
            async def but7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                try:
                    db = pymysql.connect(**config)
                    with db.cursor() as cursor:
                        #------------------------- Получение данных
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                        member_db = cursor.fetchall()[0]
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                        author_db = cursor.fetchall()[0]
                        member_games = ast.literal_eval(member_db[6])
                        author_games = ast.literal_eval(author_db[6])
                        member_games_count = member_games[0].count(0) + member_games[1].count(0) + member_games[2].count(0)
                        author_games_count = author_games[0].count(0) + author_games[1].count(0) + author_games[2].count(0)
                        
                        if author == inter.author and member_games_count != author_games_count:
                            self.xod = author
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but7.label = "X"
                            self.but7.disabled = True
                            author_games[2][0] = 1 
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(author_games), author.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                            author_db = cursor.fetchall()[0]
                            author_games = ast.literal_eval(author_db[6])
                            if is_win(author_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {author}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        elif member == inter.author and author_games_count == member_games_count:
                            self.xod = member
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but7.label = "O"
                            self.but7.disabled = True
                            member_games[2][0] = 1
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(member_games), member.id))
                            db.commit() 
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                            member_db = cursor.fetchall()[0]
                            member_games = ast.literal_eval(member_db[6])
                            if is_win(member_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {member}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        

                        #-------------------------
                        db.commit()
                    db.close()
                except Exception as ex:
                    print(ex)
            @disnake.ui.button(label="ㅤ", style=ButtonStyle.blurple, row =2)
            async def but8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                try:
                    db = pymysql.connect(**config)
                    with db.cursor() as cursor:
                        #------------------------- Получение данных
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                        member_db = cursor.fetchall()[0]
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                        author_db = cursor.fetchall()[0]
                        print(member_db)
                        member_games = ast.literal_eval(member_db[6])
                        author_games = ast.literal_eval(author_db[6])
                        member_games_count = member_games[0].count(0) + member_games[1].count(0) + member_games[2].count(0)
                        author_games_count = author_games[0].count(0) + author_games[1].count(0) + author_games[2].count(0)
                        
                        if author == inter.author and member_games_count != author_games_count:
                            self.xod = author
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but8.label = "X"
                            self.but8.disabled = True
                            author_games[2][1] = 1 
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(author_games), author.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                            author_db = cursor.fetchall()[0]
                            author_games = ast.literal_eval(author_db[6])
                            if is_win(author_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(view=self)
                            else: await inter.response.edit_message(view=self)
                        elif member == inter.author and author_games_count == member_games_count:
                            self.xod = member
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but8.label = "O"
                            self.but8.disabled = True
                            member_games[2][1] = 1
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(member_games), member.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                            member_db = cursor.fetchall()[0]
                            member_games = ast.literal_eval(member_db[6])
                            if is_win(member_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {member}"), view=self)
                            else: await inter.response.edit_message(view=self)
                            
                        #-------------------------
                        db.commit()
                    db.close()
                except Exception as ex:
                    print(ex)
            @disnake.ui.button(label="ㅤ", style=ButtonStyle.blurple, row =2)
            async def but9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
                try:
                    db = pymysql.connect(**config)
                    with db.cursor() as cursor:
                        #------------------------- Получение данных
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                        member_db = cursor.fetchall()[0]
                        cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                        author_db = cursor.fetchall()[0]
                        member_games = ast.literal_eval(member_db[6])
                        author_games = ast.literal_eval(author_db[6])
                        member_games_count = member_games[0].count(0) + member_games[1].count(0) + member_games[2].count(0)
                        author_games_count = author_games[0].count(0) + author_games[1].count(0) + author_games[2].count(0)
                        #------------------------- Изменение кнопки и списка у обоих участников
                        if author == inter.author and member_games_count != author_games_count:
                            self.xod = author
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but9.label = "X"
                            self.but9.disabled = True
                            author_games[2][2] = 1 
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(author_games), author.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (author.id))
                            author_db = cursor.fetchall()[0]
                            author_games = ast.literal_eval(author_db[6])
                            if is_win(author_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {author}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        elif member == inter.author and author_games_count == member_games_count:
                            self.xod = member
                            tic_toc_em = disnake.Embed(title="Крестики   Нолики")
                            tic_toc_em.add_field(name = f"{author} vs {member}", value=f"Ход {self.xod}")
                            self.but9.label = "O"
                            self.but9.disabled = True
                            member_games[2][2] = 1
                            cursor.execute("UPDATE `s168073_kjabdgkjabkgb`.`members` SET games = %s WHERE member_id = %s", (str(member_games), member.id))
                            db.commit()
                            cursor.execute("SELECT * FROM `s168073_kjabdgkjabkgb`.`members` WHERE member_id = %s ", (member.id))
                            member_db = cursor.fetchall()[0]
                            member_games = ast.literal_eval(member_db[6])
                            if is_win(member_games):
                                self.but1.disabled , self.but2.disabled, self.but3.disabled, self.but4.disabled, self.but5.disabled, self.but6.disabled, self.but7.disabled, self.but8.disabled, self.but9.disabled = True,True,True,True,True,True,True,True,True
                                await inter.response.edit_message(embed=disnake.Embed(title=f"Победил {member}"), view=self)
                            else: await inter.response.edit_message(view=self)
                        
                        #-------------------------
                        db.commit()
                    db.close()
                except Exception as ex:
                    print(ex)
        await inter.send(embed = tic_toc_em,view=cross())
def setup(bot):
    bot.add_cog(Game(bot)) 