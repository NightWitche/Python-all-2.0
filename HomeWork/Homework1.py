# # Напишите программу, которая принимает на вход цифру, 
# # обозначающую день недели, 
# # и проверяет, является ли этот день выходным.

# day_week = input('Введите день недели: ')
# days = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
# if day == days[5] or day == days[6]:
#     print('это выходной день')
# else:
#     print('это рабочий день')

# #Напишите программу, которая принимает на вход координаты точки (X и Y), 
# # причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# # в которой находится эта точка (или на какой оси она находится).

# def ExamKoord(x):
#     dot = [0] * x
#     for i in range(x):
#         is_OK = False
#         while not is_OK:
#             try:
#                 number = float(input(f"Enter {i+1} koordinate: "))
#                 dot[i] = number
#                 is_OK = True
#                 if dot[i] == 0:
#                     is_OK = False
#                     print("koordinate cannot been equal 0 ")
#             except ValueError:
#                 print("This is not digit")
#     return dot


# def findCoordinates(xy):
#     text = 4
#     if xy[0] > 0 and xy[1] > 0:
#         text = 1
#     elif xy[0] < 0 and xy[1] > 0:
#         text = 2
#     elif xy[0] < 0 and xy[1] < 0:
#         text = 3
#     print(f"The point is in the {text} quarter plane")

# koordinate = ExamKoord(2)
# findCoordinates(koordinate)

# #Напишите программу для. проверки истинности 
# # утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# # для всех значений предикат.

# print('The assertion is true if all incoming combinations == true')
# for x in [True, False]:
#     for y in [True, False]:
#         for z in [True, False]:
#             print((not (x or y or z)) == ((not x) and (not y) and (not z)))
        
# # Напишите программу, которая по заданному 6
# # номеру четверти, показывает диапазон возможных координат 
# # точек в этой четверти (x и y).

# a=int(input("Number quater:  "))
# if a==1:
#     print("x>0 and y>0")
# if a==2:
#     print("x<0 and y>0")
# if a==3:
#     print("x<0 and y<0")
# if a==4:
#     print("x>0 and y<0")

# #Напишите программу, которая принимает на вход координаты двух точек 
# # и находит расстояние между ними в 2D пространстве.

def inputNumbers(x):
    xy = ["X", "Y"]
    dot = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Enter coordinate on {xy[i]}: "))
                dot.append(number)
                is_OK = True
            except ValueError:
                print("Error! Must enter whole numbers ")
    return dot


def calculateLength(dot1, dot2):
    lengthSegment = ((dot2[0] - dot1[0]) ** 2 + (dot2[1] - dot1[1]) ** 2) ** (0.5)
    return lengthSegment


print("Enter coordinates  dot1")
pointA = inputNumbers(2)
print("Enter coordinates  dot2")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLength(pointA, pointB), '.2f')}")