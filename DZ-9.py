# Задание №2.

# Образец №1.

# result = []
# for i in range(100,1000):
#     num = str(i)
#     if num[0] == num[1] or num[1] == num[2] or num[0] == num[2]:
#         if num[0] == num[1] and num[1] == num[2]:
#             print()
#         else:
#             result.append(int(num[0]+num[1]+num[2]))
# print(len(result))


# Образец №2.

# s = input("Ввести диапазон из двух чисел:").split(" ")
# numbers = []
# for i in range(int(s[0]), int(s[1]) + 1):
#     num = []
#     for x in str(i):
#         num.append(x)
#     for j in range(10):
#         if num.count(str(j)) == 2:
#             numbers.append(i)
#             break
# print(numbers)
# print(len(numbers))

# Задание 4.

# Образец №1.

# s = input("Введите число:")
#
# num = ""
# for i in s:
#     if i != "3" and i != "6":
#         num += i
# print(int(num))

# Образец №2.

# s = input("Введите число:").replace("3","").replace("6","")
# print(s)