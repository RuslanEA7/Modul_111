# Задание №1.

# lower = int(input("Введите начало диапазона:"))
# upper = int(input("Введите конец диапазона:"))
# primes = []
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             primes.append(num)
# print(f"Простые числа между {lower} и {upper}: {primes}")


# Задание №2.

# n = int(input("Введите число:"))
# for i in range(1,10 + 1):
#     k=n*i
#     print(n,"*",i,"=",k)

# Задание №3.

# start = int(input('Введите начальное значение: '))
# end = int(input('Введите конечное значение: '))
# for i in range(start, end + 1):
#     for j in range(1, 11):
#         result = i * j
#         print(f'{i} * {j} = {result}')