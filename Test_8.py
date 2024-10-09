# import calendar
#
# string = input("Введите номер дня:")
#
# print(list(calendar.day_name) [int(string)])

# if string == "1":
#     print("Понедельник")
# elif string == "2":
#     print("Вторник")
# elif string == "3":
#     print("Среда")
# elif string == "4":
#     print("Четверг")
# elif string == "5":
#     print("Пятница")
# elif string == "6":
#     print("Суббота")
# elif string == "7":
#     print("Воскресенье")
# else:
#     print("День не соотвествует")


import re

# string = input("Введите число:")

# number = ['0', '0']
# numbers = re.findall(r'[-+^.]?\d+', string)
# try:
#     number[0] = float(number[0])
# except:
#     number[0] = 0
# try:
#     number[1] = float(number[1])
# except:
#     number[1] = 0
#
# ishodnoe = str(number[0]) + str(number[1])
# print(ishodnoe)

# if float(string) > 0:
#     print("Положительное")
#
# elif float(string) < 0:
#     print("Отрицательное")
# else:
#     print("Число равно 0")


# string = input("Введите числа:").split(" ")

# Сортировка Пузырьковая

# numbers = []
# for i in string:
#     numbers.append(int(i))
# numbers.sort()
#
# print(numbers)




# if int(string[0]) == int(string[1]):
#     print("Числа равны:", string[0])
# else:
#     if int(string[0]) > int(string[1]):
#         print("Второе число:", int(string[1]))
#         print("Первое число:", int(string[0]))
#     else:
#         print("Первое число:", int(string[0]))
#         print("Второе число:", int(string[1]))