# #Напишите программу, которая принимает на вход вещественное 
# # число и показывает сумму его цифр.

# def InputNums(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = float(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("This is not number!")
#     return number


# def sumNums(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum


# num = InputNums("Enter numbers: ")

# print(f"Sum digit = {sumNums(num)}")

# # Напишите программу, которая принимает на вход число 
# # N и выдает набор произведений чисел от 1 до N.

# def InputNums(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = int(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("The number must be an integer")
#     return number


# def multiply(n):
#     if n == 1:
#         return 1
#     else:
#         return n * multiply(n - 1)


# num = InputNums("Enter number: ")

# list = []
# for e in range(1, num + 1):
#     list.append(multiply(e))

# print(f"Products of numbers from 1 to {num}:  {list}")

# # Задайте список из n чисел последовательности 
# # $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n= int(input('n= '))
# d={}
# sum=0
# for i in range(1, n+1):
#     d[i]=round((1+1/i)**i,2)
#     sum+=d[i]
# print(d)
# print(round(sum, 2))

# #Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# # Найдите произведение элементов на указанных позициях. 
# # Позиции хранятся в файле file.txt в одной строке одно число.

# arr = [int(input('Enter element arr: ')) for i in range(int(input('Enter length arr: ')))]
 
# prod = 1
# for i in arr:
#     prod *= i
 
# print(f'All list: {arr}')
# print(f'Summ element list = : {sum(arr)}')
# print(f'Product element list: {prod}')

# # Реализуйте алгоритм перемешивания списка.

import random 
y = ['Nignt ', 'Summer ', 'Evening ', 'Day', 'Tomorrow']
random.shuffle(y)
 
print(y)
