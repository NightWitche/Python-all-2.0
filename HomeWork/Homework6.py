from random import randint
from random import random

# # Задача: Нахождение разницы между максимальным и минимальным
# # значением дробной части элементов списка вещественных чисел

# string2 = list(map(lambda value: round(value, 2), (randint(1, 9) + random() for i in range(10)))) # имитация ввода дробных значений
# fract = list(map(lambda num: round(num % 1, 2), string2)) # обрез целой части элементов списка
# max_num = max(fract)
# min_num = min(fract)
# print(f'1.2) For list {string2}\n difference between max ({max(fract)}) and min ({min(fract)}) the values ​​of the fractional parts of the elements is {round(max(fract) - min(fract), 2)}\n')

# # Задача: Программа, удаляющая из текста все слова, содержащие ""абв""

# text = 'авб абввв баа абв ывваабв ыукк абв вууа ыабвуу авб абббрполод абв'
# print(text)

# lst2 = list(filter(lambda text: not 'абв' in text, text.split()))
# print(f'2.2) {lst2}')

# Задача: Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

maxcommult = max(a, b)
mincommult = min(a, b)
mult_list = list(filter(lambda value: value % maxcommult == 0 and value % mincommult == 0, list(i for i in range(mincommult, mincommult * maxcommult + 1))))
print(f'3.2) Наименьшее общее кратное {a} и {b} - {min(mult_list)}')