#Интерфейс
from tkinter import *
import tkinter.ttk as ttk

#Подгрузчик ресурсов:
############################

#Игроки:
from src.nodes.players.player_sample import Player_Sample

#Контейнеры:
from src.conteiners.spisok import Spisok
from src.conteiners.stek import Stek

#Объекты:
from src.nodes.objects.items.item_sample import Object_Item
from src.nodes.objects.tools.tool_sample import Object_Tool
from src.nodes.objects.armors.armor_sample import Object_Armor
from src.nodes.objects.weapons.gun_sample import Gun_Sample
from src.nodes.objects.weapons.melee_sample import Melee_Sample

import random
'''
this is for random loot from the cave.
random.randit()
'''

import sys
'''
I'm importing this for quiting the program,
and for creating and reading files, for game-saving feature.
'''

import os
'''
Для очистки консоли и закрытия приложения!
'''

'''
Все объекты и всё объекты!
'''
        
def armor_loop(name : str()):
    '''
    Кожанка, Кольчуга,
    Улучшенная Кольчужная Броня. ХЭШ ТАБЛИЦА
    '''

    if name == "Кожанка":
        return Object_Armor(name, 4, 2)
    elif name == "Кольчуга":
        return Object_Armor(name, 9, 6)
    elif name == "Улучшенная Кольчужная Броня":
        return Object_Armor(name, 12, 9)

def resources_loop(a : int(), b : int(), group : int() ):
    '''
    Возвращает случайный предмет из доступных
    в другой любой контейнер.
    '''

    resources_table = list
    
    if group == 1:
        resources_table = ["Ткань", "Металлолом", "Пластик"]
    elif group == 2:
        resources_table = ["Кристалы Ядра", "Качественный Пластик", "Электро-Схемы"]

    name = random.choice(resources_table)
    count = int(random.randint(a,b))

    print(count)
    print(name)


    if name == "Ткань":
        return Object_Item(name, count)
    elif name == "Металлолом":
        return Object_Item(name, count)
    elif name == "Пластик":
        return Object_Item(name, count)

def craft_loop(stanok : bool):
    '''
    Проверка на доступность крафта
    Удаление испотльзованных в крафте предметов
    Выдача предмета после крафта
    '''
        
    craft_table : list

    table1 : list = ["Станок", "Заточка"]
    table2 : list = ["Бур", "Кирка", "Бур с напылением", "Кирка с напылением"]

    if stanok == False:
        craft_table = table1
    elif stanok == True:
        craft_table = table1 + table2

def main():
    
    STEP = 0  #переменная считающая игровые шаги (Тики)

    game_on = bool(True)

    name = input("Придумайте имя: ")

    Player = Player_Sample(name, 5, armor_loop("Кожанка"), Spisok(5))

    os.system("cls||clear") 

    while game_on == True:
        
        print("1 : Поиск ресурсов - 1 шаг")
        print("2 : Перейти в другую комнату")
        print("3 : Статистика Игрока")
        print("4 : Посмотреть инвентарь")
        print("5 : Создать")

        choise = int(input("Выберите действие: "))

        if choise == 1:
            os.system("cls||clear")
            STEP += 1
            print("Всего пройдено шагов:", STEP)

        elif choise == 2:
            os.system("cls||clear")
            print("В разработке...")

        elif choise == 3:
            os.system("cls||clear")
            Player.print_stats()
            
        elif choise == 4:
            os.system("cls||clear")
            print("В разработке...")

        elif choise == 5:
            os.system("cls||clear")
            print("В разработке...")
        
        elif choise == 6:
            os.system("cls||clear")
            print("Ты как сюда попал человек??? Owo")
        
        else:
            return



main()













