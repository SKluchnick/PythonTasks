# 1. Реализовать программу, которая принимает на вход через консоль с помощью
# класса Scanner, число, соответствующее количеству этажей в здании. Используя
# условный оператор if, необходимо вывести в консоль сообщение о типе такого дома.
# Условия: если этажей 1-4 - “Малоэтажный дом”, 5-8 - “Среднеэтажный дом”, 9 и более
# - “Многоэтажный дом”. Так же, необходимо учесть что может быть введено
# отрицательное значение, в таком случае сообщить “Ошибка ввода”.

enter = int(input("Please write num: "))

if 1 <= enter <= 4:
    print('Малоэтажный дом')
elif 5 <= enter <= 5:
    print('Среднеэтажный дом')
elif enter >= 9:
    print('Многоэтажный дом')
else:
    print('Ошибка ввода')


# 2. Есть два числа, которые задаются пользователем через консоль (назовем эти два
# числа a и b). Используя цикл for, вывести все числа из диапазона между a и b,
# которые делятся на 5 без остатка, но при этом не делятся на 10 без остатка.
# Например, число 15 подходит под наше условие (делится на 5 без остатка и не
# делится на 10 без остатка), но число 20 не подходит под наше условие (делится на 5
# без остатка и делится на 10 без остатка). Сами числа a и b в диапазоне не учитывать.
# Если a >= b вывести сообщение "Некорректный ввод".
# Пример:
# Вводим в консоли: 7 78
# Вывод: 15 25 35 45 55 65 75

enter = int(input("Please write num: "))
enterTwo = int(input("Please write num: "))

for i in range(enter,enterTwo+1):
    if i % 5 == 0 and i % 10 != 0:
        print (i)