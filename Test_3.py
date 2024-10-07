# a = 8
# b = 6
# c = 7
#
# if a > b:
#     print("Истина_1 ")
#     if a == b + 2:
#         print("Истина_2")
#         if a < c:
#             print("Истина_3")
#         else:
#             print("Ложь_3")
#     else:
#         print("Ложь_2")
# else:
#     print("Ложь_1")

from time import strftime

# i = 0
# a = [1,2,3,4,5]
# print(set(a))
# for i in a:
#     print(i)



string = input("Введите 3 числа через пробел: ")

print(string)

numbers = string.split(" ")
print(numbers)
if numbers[3] == "+":
    summa = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
    print("Сумма:", summa)
if numbers[3] == "*":
    summa = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
    print("Умножение:", summa)

# for i in numbers:
#     summa2 += int(i)
# print(summa2)
