# Задание №1.
import operator

# Образец №1.

# s = eval(input("Введите пример:"))
#
# print(s)


# Образец №2.

# import re
# s = input("Введите пример:")
# operation = re.findall(r'[\-/\+*]', s)
# print(operation)
# numbers = re.split(r'[(\-/\+*)]', s.replace(" ", ""))
# print(numbers)
# i = 0
# result = 0
# res = []
# j = 0
# isk = []
# while j < len(numbers):
#     print(operation[j])
#     if operation[j] == "/":
#         res.append(int(numbers[j]) / int(numbers[j+1]))
#         numbers.pop(j)
#         numbers.pop(j)
#         operation.pop(j)
#         j = 0
#     if operation[j] == "*":
#         res.append(int(numbers[j]) * int(numbers[j + 1]))
#         numbers.pop(j)
#         numbers.pop(j)
#         operation.pop(j)
#         j = 0
#     j += 1
# print(operation, numbers)
# print(res)

# expression = input("Введите арифметическое выражение (например, 23+12): ")
# parts = expression.split()
#
# if len(parts) == 3:
#     num1 = float(parts[0])
#     operator = parts[1]
#     num2 = float(parts[2])
#    if operator == '+':
#        result = num1 + num2
#    elif operator == '-':
#        result = num1 - num2
#    elif operator == '*':
#        result = num1 * num2
#    elif operator == '/':
#        if num2 == 0:
#            print("Ошибка: деление на ноль.")
#        else:
#            result = num1 / num2
#    else:
#        print("Ошибка: неверный оператор.")
# else:
#    print("Ошибка: неверный формат ввода.")
#
# print("Результат:", result)


# import random
# random_list = [random.randint(-10, 10) for _ in range(10)]
# min_value = min(random_list)
# max_value = max(random_list)
# negative_count = sum(1 for num in random_list if num < 0)
# positive_count = sum(1 for num in random_list if num > 0)
# zero_count = sum(1 for num in random_list if num == 0)
#
# print("Сгенерированный список:", random_list)
# print("Минимальный элемент:", min_value)
# print("Максимальный элемент:", max_value)
# print("Количество отрицательных элементов:", negative_count)
# print("Количество положительных элементов:", positive_count)
# print("Количество нулей:", zero_count)





# expression = input("Введите арифметическое выражение: ")
# operators = {
#     '+': operator.add(),
#     '-': operator.sub(),
#     '*': operator.mul(),
#     '/': operator.truediv()
# }
# operands = expression.split()
# first_operand = float(operands[0])
# operator_symbol = operands[1]
# second_operand = float(operands[2])
# if operator_symbol in operators:
#     result = operators[operator_symbol](first_operand, second_operand)
#     print("Результат выражения: ", result)
# else:
#     print("Неверная операция")












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