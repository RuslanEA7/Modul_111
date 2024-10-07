# string = (input("Введите числа через пробел и знак: ").split(" "))

# print(eval(string))
#
# number1 = float(string[0])
# number2 = float(string[1])
# number3 = float(string[2])
#
# znak = string[3]
# if znak =="+":
#     result = number1 + number2 + number3
#     print(result)
# elif znak =="*":
#     result = number1 * number2 * number3
#     print(result)
# elif znak =="-":
#     result = number1 - number2 - number3
#     print(result)
# elif znak =="/":
#     result = (number1 / number2 / number3).__format__(".3f")
#     print(result)
# else:
#     print("Неккорректные данные")


# string = input("Введите 3 чсила: ").split(" ")
# number = []
# for i in string:
#     number.append(float(i))
#
# print("Max: ", max(number))
# print("Min: ", min(number))
# print("Avg: ", sum(number) / len(number))


# string = input("Введите количество метров: ").split(" ")
#
# number1 = float(string[0])
#
# znak = string[1]
# if znak == "M":
#     result = (number1 / 0.00062).__format__(".3f")
#     print("Мили:", result)
#
# elif znak == "D":
#     result = (number1 * 39.3701).__format__(".3f")
#     print("Дюймы:", result)
#
# elif znak =="Y":
#     result = (number1 * 1.09361).__format__(".3f")
#     print("Ядры:", result)
# else:
#     print("Неккорректные данные")