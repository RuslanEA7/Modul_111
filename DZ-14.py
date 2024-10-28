# Задание №1.


# s1 = input().split(" ")
# s2 = input().split(" ")
#
# numbers = []
# s = s1+s2
# for i in s:
#     numbers.append(int(i))
# print(numbers)


# Задание №2.

# s1 = input().split(" ")
# s2 = input().split(" ")
#
# numbers = []
# s = s1+s2
# for i in s:
#     numbers.append(int(i))
# print(set(numbers))


# Задание №4.

# s1 = input().split(" ")
# s2 = input().split(" ")
#
# numbers1 = []
# numbers2 = []
# s = s1+s2
# for i in s1:
#     numbers1.append(int(i))
# numbers1 = list(set(numbers1))
# print(numbers1)
# for i in s2:
#     numbers2.append(int(i))
# numbers2 = list(set(numbers2))
# print(numbers2)
# numbers = numbers1 + numbers2
# print(numbers)


# Задание №3.

# s1 = input().split(" ")
# s2 = input().split(" ")
#
# numbers = []
# numbers1 = []
# numbers2 = []
# s = s1+s2
# for i in s1:
#     for j in s2:
#         if i == j:
#             numbers.append(int(i))
# print(list(set(numbers)))


# Задание №5.

# s1 = input().split(" ")
# s2 = input().split(" ")
# numbers = []
# numbers1 = max([int(s) for s in s1]), min([int(s) for s in s1])
# numbers2 = max([int(s) for s in s2]), min([int(s) for s in s2])
# print(numbers1)
# print(numbers2)