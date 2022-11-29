# # Задайте список из нескольких чисел. 
# # Напишите программу, которая найдёт сумму элементов списка, 
# # стоящих на нечётной позиции.

# a= input("Enter list from multiple numbers through a space:   ").split()
# print(a)
# sum=0
# for i in range(1, len(a), 2):
#     sum+=int(a[i])
# print(f'The sum of the list elements in an odd position: {sum}')

# # Напишите программу, которая найдёт произведение пар чисел списка. 
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# a=input("Enter a list of several numbers separated by a space:   ").split()
# print(a)
# total=[]
# for i in range((len(a)+1)//2):
#   total.append(int(a[i])*int(a[-(i+1)]))
# print(total)

# # Задайте список из вещественных чисел. Напишите программу, 
# # которая найдёт разницу между максимальным 
# # и минимальным значением дробной части элементов.

# a= input("Specify a list of several real numbers separated by a space:   ").split()
# print(a)

# min= float((a[0]))%1
# max= float((a[0]))%1

# for i in a:
        
#         i=(float(i))%1
#         if i==0:
#             continue
#         if i>max:
#             max=i
#         elif i<min:
#             min=i
    
# print(f'Min value of the fractional part of the elements {round(min, 4)}')
# print(f'Max value of the fractional part of the elements {round(max, 4)}')
# print(f'The difference between the max and min value of the fractional part of the elements {round((max-min),4)}')

# # Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# digit = int(input())
 
# a = ''
 
# while digit > 0:
#     a = str(digit % 2) + a
#     digit = digit // 2
 
# print(a)

# # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Num=int(input("Enter a number to build a sequence: "))
# a=[0,1]

# for i in range(2,Num+1):
#     a.append(a[i-1]+a[i-2])

#     for i in range(Num):
#         a.insert(0,(a[1]-a[0]))

#     print(a)