import random

# #Вычислить число c заданной точностью d
# #при d = 0.001, π = 3.141.    10^(-1) ≤ d ≤10^(-10)
# # e = 2,7182818284590452353602874713527
# # e = 1 + 1/1! + 1/2! + 1/3! + ..

# a = abs (int (input('введите количество знаков после запятой ')))

# d = 1 / (10 ** a)
# e = 1
# fact_e = 1

# count = 1

# while True:
#     fact_e *= count
#     went_e = e + 1 / (fact_e)
#     #print (went_e)
#     if (abs(e - went_e) <= d):
#         e = went_e
#         break
#     e = went_e    
#     count += 1


# print(f'e = {round (e , a)}')

# # Задайте натуральное число N. Напишите программу, 
# # которая составит список простых множителей числа N.

# num = abs (int (input('Enter a natural digit ')))
# went = num
# list1 = []
# num2 = 2
# while went != 1:
#     while went % num2 == 0 :
#         list1.append(num2)
#         went /= num2
#     num2 += 1
# if num != list1[0]:
#     print(list1)
# else: print(f'Digit {num} - is simple')

# # Задайте последовательность чисел. Напишите программу, 
# # которая выведет список неповторяющихся элементов исходной последовательности.

# num_list = [random.randint(1, 9) for i in range(random.randint(6, 15))]
# print(f'given a sequence of numbers:\n{num_list}')

# list1 = [num_list[0]]
# eq = False

# for item in num_list:
#     for i in range(len(list1)):
#         if item == list1[i]: eq = True
#     if eq == False:
#         list1.append(item)
#     eq = False
  
# print(f'list of non-repeating elements of the original sequence:\n{list1}')

# # Задана натуральная степень k. Сформировать случайным образом список 
# # коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# deg = int(input('Enter the natural degree of the polynomial: '))
# plist = []
# while deg != 0:
#     k = str(random.randint(0, 100))
#     if deg > 1:
#         if k != '0' and k != '1': plist.append(f'{k}x^{str(deg)}')
#         elif k == '1': plist.append(f'x^{str(deg)}')
#     elif deg == 1:
#         if k != '0' and k != '1': plist.append(f'{k}x')
#         elif k == '1': plist.append(f'x')
#     deg -= 1
# plist.append(str(random.randint(0, 100)))
    
# with open('file.txt', 'w') as data:
#     for i in range(len(plist) - 1):
#         data.write(f'{plist[i]} + ')
#     data.write(plist[-1])
# print(f'File created file.txt with polynomial:')
# with open('file.txt', 'r') as data:
#     print(f'{data.read()}\n')