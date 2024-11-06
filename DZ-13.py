# Задание №1.

# Образец №1.

# s = eval(input("Введите пример:"))
#
# print(s)


# Образец №2.

import re
s = input("Введите пример:")
operation = re.findall(r'[\-/\+*]', s)
print(operation)
numbers = re.split(r'[(\-/\+*)]', s.replace(" ", ""))
print(numbers)
i = 0
result = 0
res = []
j = 0
isk = []
while j < len(numbers):
    print(operation[j])
    if operation[j] == "/":
        res.append(int(numbers[j]) / int(numbers[j+1]))
        numbers.pop(j)
        numbers.pop(j)
        operation.pop(j)
        j = 0
    if operation[j] == "*":
        res.append(int(numbers[j]) * int(numbers[j + 1]))
        numbers.pop(j)
        numbers.pop(j)
        operation.pop(j)
        j = 0
    j += 1
print(operation, numbers)
print(res)






















# A = "111"
#
# def DZ13(s = "", a = 1 , b = 0):
#     # try:
#     #     f = a / b
#     # except:
#     #     f = 1
#     #     print("Исключение")
#     # finally:
#     #     print("Завершили")
#     # f = a * b
#     if not s: s = "Пустая строка"
#     d = A
#     print(d)
#
#     return d
#
# def sl(d = ""):
#     e = d.lower()
#     return e
#
# DZ13(sl("kdhhihIHKNKhijbkc"))