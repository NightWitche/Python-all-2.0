# #Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = input("Enter text separated by a space:\n")
# print(f"Source text: {text}")
# find_text = "абв"
# lst = [i for i in text.split() if find_text not in i]
# print(f'Result: {" ".join(lst)}')

# #Создайте программу для игры с конфетами человек против человека.
# # Условие задачи: На столе лежит 2021 конфета. 
# # Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# # За один ход можно забрать не более чем 28 конфет. 
# # Все конфеты оппонента достаются сделавшему последний ход. 
# # Сколько конфет нужно взять первому игроку, 
# # чтобы забрать все конфеты у своего конкурента?
# # a) Добавьте игру против бота
# # b) Подумайте как наделить бота ""интеллектом""

# #(человек против человека)

# from random import randint

# def indat(name):
#     amoutcand = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while amoutcand < 1 or amoutcand > 28:
#         amoutcand = int(input(f"{name}, введите корректное количество конфет: "))
#     return amoutcand


# def laprint(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# count1 = 0 
# count2 = 0

# while value > 28:
#     if flag:
#         k = indat(player1)
#         count1 += k
#         value -= k
#         flag = False
#         laprint(player1, k, count1, value)
#     else:
#         k = indat(player2)
#         count2 += k
#         value -= k
#         flag = True
#         laprint(player2, k, count2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# #(человек против Бота)

# from random import randint

# def indat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def laprint(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# count1 = 0 
# count2 = 0

# while value > 28:
#     if flag:
#         k = indat(player1)
#         count1 += k
#         value -= k
#         flag = False
#         laprint(player1, k, count1, value)
#     else:
#         k = randint(1,29)
#         count2 += k
#         value -= k
#         flag = True
#         laprint(player2, k, count2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# # (Восстание машин)

# from random import randint

# def indat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def laprint(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


# def bot_calc(value):
#     k = randint(1,29)
#     while value-k <= 28 and value > 29:
#         k = randint(1,29)
#     return k

# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# count1 = 0 
# count2 = 0

# while value > 28:
#     if flag:
#         k = indat(player1)
#         count1 += k
#         value -= k
#         flag = False
#         laprint(player1, k, count1, value)
#     else:
#         k = bot_calc(value)
#         count2 += k
#         value -= k
#         flag = True
#         laprint(player2, k, count2, value)

# if flag:
#     print(f"The Vin {player1}")
# else:
#     print(f"The Vin {player2}")

# # Создайте программу для игры в ""Крестики-нолики"".

# maps = [1,2,3,
#         4,5,6,
#         7,8,9] 

# lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
 
# def print_maps():
#     print(maps[0], end = " | ")
#     print(maps[1], end = " | ")
#     print(maps[2])
#     print('==========') 
#     print(maps[3], end = " | ")
#     print(maps[4], end = " | ")
#     print(maps[5])
#     print('==========')
#     print(maps[6], end = " | ")
#     print(maps[7], end = " | ")
#     print(maps[8])    
 
# def who_win():
#     win = ""
#     for i in lines:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "Победил игрок 1 (Х)!"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "Победил игрок 2 (O)!"        
#     return win
 
# i=1

# print_maps()
# while i<10:
#     if i%2!=0:
#         step =int(input("ход игрока 1: "))
#         if step>9 or step<1:
#             print("Номера ячеек лежат в диапазоне от 1 до 9. Начните игру сначала")
#             break
#         if maps[step-1]!="X"and maps[step-1]!="O":
#             maps[step-1]="X"
#         else:
#             print("Эта ячейка уже занята,  начните игру сначала")
#             break
#     else:
#         step =int(input("ход игрока 2: "))
#         if maps[step-1]!="X"and maps[step-1]!="O":
#             maps[step-1]="O"
#         else:
#             print("Эта ячейка уже занята начните игру сначала")
#             break
        
#     print_maps()
#     win= who_win()
#     if win!='':
#         print(win)
#         break
#     i+=1
    
# if win=='':
#     print("Ничья!")

# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def incod(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def deincod(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Enter text to encode: ")
print(f"Text after encoding: {incod(s)}")
print(f"Text after decryption: {deincod(incod(s))}")