# Задание №1.

# Образец №1.

# string = input("Введите два числа:").split(" ")
#
# even = 0 # Четные числа
# even_number = []
# odds = 0 # Нечетные числа
# odds_number = []
# int9 = 0 # Кратные 9.
# int9_number = []
# for i in range(int(string[0]), int(string[1])):
#     if i % 2 == 0:
#         even += 1
#         even_number.append(i)
#     if  i % 2 != 0:
#         odds += 1
#         odds_number.append(i)
#     if i % 9 == 0:
#         int9 += 1
#         int9_number.append(i)
# print("Кол-во четных:", even, "Ср. Ариф.:", sum(even_number) / even)
# print("Кол-во нечетных:", odds, "Ср. Ариф.:", sum(odds_number) / odds)
# print("Кол-во кратных 9:", int9, "Ср. Ариф.:", sum(int9_number) / int9)

# Образец №2.

# string = input("Введите два числа:").split(" ")
# even = [i for i in range(int(string[0]), int(string[1])) if i % 2 == 0]
# odds = [i for i in range(int(string[0]), int(string[1])) if i % 2 != 0]
# int9 = [i for i in range(int(string[0]), int(string[1])) if i % 2 == 0]
# print("Кол-во четных:", len(even), "Ср. Ариф.:", sum(even) / len(even))
# print("Кол-во нечетных:", len(odds), "Ср. Ариф.:", sum(odds) / len(odds))
# print("Кол-во кратных 9:", len(int9), "Ср. Ариф.:", sum(int9) / len(int9))