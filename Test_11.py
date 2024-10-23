# Пример №1.

# list1 = [i*2 for i in range(100) if i % 3==0]
# print(list1)
#
# list2 = []
# for i in range(100):
#     if i % 3 == 0:
#         i *= 2
#         list2.append(i)
# print(list2)
#
# print(list1 := [i*2 for i in range(100) if i % 3==0])


# Пример №2.

# names = ['Bob','Anna','Joe','Bill','Nick']
# list2 = [i for i in names if i != names[2]]
# print(list2)

# Пример №3.

# customers = [1,7,3,2,10]
# list2 = [i for i in customers]
# print(list2)
# result = 1
# for i in customers:
#     result *= i
# print(result)


# Пример №4.

# list = [i*i for i in range(1,11) if i % 2 == 0]
# print(list)


# Пример №5.

# customers = ['Bob','Anna','Joe','Bill','Nick']
# # print(customers[-1])
# result = ""
# for i in customers:
#     result += i + "-"
#     print(i)
# print(result[:-1])
# print(result.split("-")[:-1])
# print(result.rstrip("-"))
# print(result.rstrip("-").split("-")[:3])


# Пример №6.

# a1 = 10
# b1 = 20
# matrix = [[1,2,3] , [4,5,6] , [7,8,9] , [a1,[13,14,[15,16,"OK"]],12,b1]]
# search = "OK"
# for  i in matrix:
#     print("Уровень:", i)
#     if search in i:
#         print("Нашли OK:")
#         break
#     else:
#         for vtoroy in i:
#             if search == vtoroy:
#                 print("Нашли OK:")
#                 break
#             else:
#                 if type(vtoroy) is list:
#                     print("Второй уровень:", vtoroy)
#                     for tretiy in vtoroy:
#                         print(tretiy)
#                         if search == tretiy:
#                             print("Нашли OK:")
#                             break
#                         else:
#                             if type(tretiy) is list:
#                                 for chetvertiy in tretiy:
#                                     print(chetvertiy)
#                                     if search == chetvertiy:
#                                         print("Нашли OK")
#                                         break

# print(matrix[3][1][2][2])