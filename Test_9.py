# string = input()
#
# if 0 < int(string) > 100:
#     print("Ошибка")
# else:
#     number = int(string)
#     if number % 3 == 0 and number % 5 != 0:
#         print("Fizz")
#     if number % 5 == 0 and number % 3 != 0:
#         print("Buzz")
#     if number % 15 == 0:
#             print("Fizz Buzz")
#     else:
#         print("Число:", number)


# string = input("Введите число и степень:").split(" ")
#
# number = int(string[0])
# stepen = int(string[1])
# if 0 <= stepen <=7:
#     result = number ** stepen
#     print("Результат:", result)
# else:
#     print("Ошибка")


# string = input("Введите стоимость, с кого звоним, куда звоним:").split(" ")

# price = float(string[0])
# mtot = 0 # с мтс на теле2 0.2
# # mtob = 1 # с мтс на билайн 0.3
# # ttob = 2 # с теле2 на билайн 0.4
# # mtob = 3 # мтс 0.1
# # btob = 4 # билайн 0.1
# # ttot = 5 # теле2 0.1

# if string[1] == "m" and string[2] == "t":
#     result = price * 0.2
#     print(result)
# if string[1] == "m" and string[2] == "b":
#     result = price * 0.3
#     print(result)
# if string[1] == "t" and string[2] == "b":
#     result = price * 0.4
#     print(result)
# if string[1] == "m" and string[2] == "m":
#     result = price * 0.1
#     print(result)
# if string[1] == "t" and string[2] == "t":
#     result = price * 0.1
#     print(result)
# if string[1] == "b" and string[2] == "b":
#     result = price * 0.1
#     print(result)


# string = input("Введите уровень продаж:").split(" ")
# base = 200 # Базовая ставка 200$
# percent = 0
# premiya = 0
# status = 0
# if int(string[0]) > int(string[1]) > int(string[2]) or int(string[0]) > int(string[2]) > int(string[1]):
#     status = 0
#     print("Премия начислиться менеджеру №:", status)
# if int(string[1]) > int(string[2]) > int(string[0]) or int(string[1]) > int(string[0]) > int(string[2]):
#     status = 1
#     print("Премия начислиться менеджеру №:", status)
# if int(string[2]) > int(string[1]) > int(string[0]) or int(string[2]) > int(string[0]) > int(string[1]):
#     status = 2
#     print("Премия начислиться менеджеру №:", status)
# k = 0
# for i in string:
#     zp = int(i)
#     if 0 < zp < 500:
#         percent = 0.03
#     elif 500 <= zp < 1000:
#         percent = 0.05
#     elif zp >= 1000:
#         percent = 0.08
#     if k == status:
#         premiya += 200
#         print("Менеджер №:",k+1,":", base * (1 + percent) + premiya)
#     else:
#         print("Менеджер №:", k+1, ":", base * (1 + percent))
#     k += 1