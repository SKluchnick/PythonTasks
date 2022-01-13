# Напишите программу:
# Тимофей обычно спит ночью XX часов и устраивает себе днем тихий час на YY минут.
# Определите, сколько всего минут Тимофей спит в сутки.
# Внимание, программа принимает значения XX и YY из стандартного потока ввода
# (функция input), результат надо выводить в стандартный поток вывода (функция print).
# Обратите внимание на то, что приглашение, переданное в качестве аргумента в функцию input,
# считается выводом вашей программы. Используйте эту функцию без аргументов:
# Sample Input 1:
# 7
# 30
# Sample Output 1:
# 450
X = int(input())
Y = int(input())
print(X*60 + Y)

# Коля каждый день ложится спать ровно в полночь и недавно узнал,
# что оптимальное время для его сна составляет XX минут.
# Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через XX минут
# после полуночи, однако для этого необходимо указать время сигнала в формате часы, минуты.
# Помогите Коле определить, на какое время завести будильник.
# Часы и минуты в выводе программы должны располагаться на разных строках (см. пример работы программы)
# Помните, что для считывания данных нужно вызывать функцию input без аргументов!
# Sample Input 1:
# 480
# Sample Output 1:
# 8
# 0
X = int(input())
print(X//60)
print(X%60)

# Катя узнала, что ей для сна надо XX минут. В отличие от Коли,
# Катя ложится спать после полуночи в HH часов и MM минут.
# Помогите Кате определить, на какое время ей поставить будильник,
# чтобы он прозвенел ровно через XX минут после того, как она ляжет спать.
# На стандартный ввод, каждое в своей строке, подаются значения XX, HH и MM.
# Гарантируется, что Катя должна проснуться в тот же день, что и заснуть.
# Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.
# Sample Input 1:
# 480
# 1
# 2
# Sample Output 1:
# 9
# 2
X = int(input())
H = int(input())
M = int(input())
A = (X // 60)
B = (X % 60)
C = ((M + B) // 60) + A + H
print(C)
D = (X + M) % 60
print(D)

# Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы AA часов в сутки,
# но пересыпать тоже вредно и не стоит спать более BB часов. Сейчас Аня спит HH часов в сутки.
# Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
# Если Аня спит менее AA часов, выведите “Недосып”, если же более BB часов, то выведите “Пересып”.
# Получаемое число AA всегда меньше либо равно BB.
# На вход программе в три строки подаются переменные в следующем порядке: AA, BB, HH.
# Обратите внимание на регистр символов: вывод должен в точности соответствовать описанному в задании,
# т. е. если программа должна вывести "Пересып", выводы программы "пересып", "ПЕРЕСЫП", "ПеРеСыП" и другие не будут считаться верными.
# Это первое не самое тривиальное задание на условное выражение. В случаях, когда разбить исполнение программы на несколько направлений,
# стоит внимательно обдумать все условия, которые нужно использовать.
# Особое внимание стоит уделить строгости используемых условных операторов: различайте \lt< и \le≤; \gt> и \ge≥.
# Для того, чтобы понимать, какой из них стоит использовать, внимательно прочитайте условие задания.
# Sample Input 1:
# 6
# 10
# 8
# Sample Output 1:
# Это нормально
# Sample Input 2:
# 7
# 9
# 10
# Sample Output 2:
# Пересып
# Sample Input 3:
# 7
# 9
# 2
# Sample Output 3:
# Недосып

A = int(input())
B = int(input())
H = int(input())
A <= B
if A <= H <=B:
    print('Это нормально')
elif H < A:
    print('Недосып')
elif H > B:
    print('Пересып')

# Требуется определить, является ли данный год високосным.
# Напомним, что високосными годами считаются те годы, порядковый номер которых либо кратен 4,
# но при этом не кратен 100, либо кратен 400 (например, 2000-й год являлся високосным, а 2100-й будет невисокосным годом).
# Программа должна корректно работать на числах 1900≤n≤3000.
# Выведите "Високосный" в случае, если считанный год является високосным и "Обычный" в обратном случае
# (не забывайте проверять регистр выводимых программой символов).
# Sample Input 1:
# 2100
# Sample Output 1:
# Обычный
# Sample Input 2:
# 2000
# Sample Output 2:
# Високосный
a = int(input())
if (a % 400 == 0) or (a % 4 == 0) and (a % 100 != 0):
    print('Високосный')
else:
    print('Обычный')

# В то далёкое время, когда Паша ходил в школу, ему очень не нравилась формула Герона для вычисления площади треугольника,
# так как казалась слишком сложной. В один прекрасный момент Павел решил избавить всех школьников от страданий и написать и
# распространить по школам программу, вычисляющую площадь треугольника по трём сторонам.
# Одна проблема: так как эта формула не нравилась Павлу, он её не запомнил.
# Помогите ему завершить доброе дело и напишите программу,
# вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона:
# На вход программе подаются целые числа, выводом программы должно являться вещественное число, соответствующее площади треугольника.
# Sample Input:
# 3
# 4
# 5
# Sample Output:
# 6.0
x = int(input())
y = int(input())
z = int(input())
p = 1 / 2 * (x + y + z)
RES = (p * (p - x) * (p - y) * (p - z)) ** 0.5
print(RES)
#
# Напишите программу, принимающую на вход целое число, которая выводит True,
# если переданное значение попадает в интервал (-15, 12] \cup (14, 17) \cup [19, +\infty)(−15,12]∪(14,17)∪[19,+∞)
# и False в противном случае (регистр символов имеет значение).
# Обратите внимание на разные скобки, используемые для обозначения интервалов. В задании используются полуоткрытые и открытые интервалы.
# Sample Input 1:
# 20
# Sample Output 1:
# True
x = int(input())
if (x > -15 and x <=12) or (x > 14 and x < 17) or (x >= 19 ):
    print(True)
else:
    print(False)

# Напишите простой калькулятор, который считывает с пользовательского ввода три строки
# : первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число")
# и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.
# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!
x = float(input())
z = float(input())
y = input()

if y == "+":
    print(x+z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    if z != 0:
        print(x / z)
    else:
        print("Деление на 0!")
elif y == "mod":
    if z != 0:
        print(x % z)
    else:
        print("Деление на 0!")
elif y == "pow":
    print(x ** z)
elif y == "div":
    if z != 0:
        print(x // z)
    else:
        print("Деление на 0!")
# Жители страны Малевии часто экспериментируют с планировкой комнат.
# Комнаты бывают треугольные, прямоугольные и круглые.
# Чтобы быстро вычислять жилплощадь, требуется написать программу,
# на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
# которая бы выводила площадь получившейся комнаты.
# Для числа π в стране Малевии используют значение 3.14.
# Формат ввода, который используют Малевийцы:
# треугольник
# a
# b
# c
# где a, b и c — длины сторон треугольника
# прямоугольник
# a
# b
# где a и b — длины сторон прямоугольника
# круг
# r
# где r — радиус окружности
# Sample Input 1:
# прямоугольник
# 4
# 10
# Sample Output 1:
# 40.0
# Sample Input 2:
# круг
# 5
# Sample Output 2:
# 78.5
# Sample Input 3:
# треугольник
# 3
# 4
# 5
# Sample Output 3:
# 6.0
type = input()
if type == "треугольник":
    x = float(input())
    y = float(input())
    z = float(input())
    p = 1 / 2 * (x + y + z)
    RES = (p * (p - x) * (p - y) * (p - z)) ** 0.5
    print(RES)
elif type == "прямоугольник":
    x = float(input())
    y = float(input())
    RES = x * y
    print(RES)
elif type == "круг":
    x = float(input())
    RES = 3.14 * (x**2)
    print(RES)

# Напишите программу, которая получает на вход три целых числа, по одному
# числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.
# Sample Input 1:
# 8
# 2
# 14
# Sample Output 1:
#
# 14
# 2
# 8
# Sample Input 2:
#
# 23
# 23
# 21
# Sample Output 2:
#
# 23
# 21
# 23
a = int(input())
b = int(input())
c = int(input())
s = a + b + c;
print(max(a,b,c))
print(min(a,b,c))
print(s - max(a,b,c) - min(a,b,c))

# Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное),
# выводящее это число в консоль вместе с правильным образом изменённым
# словом "программист", для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
# В комнате может быть очень много программистов. Проверьте,
# что ваша программа правильно обработает все случаи, как минимум до 1000 человек.
# Дополнительный комментарий к условию:
# Обратите внимание, что задача не так проста, как кажется на первый взгляд.
# Если ваше решение не проходит какой-то тест, это значит, что вы не рассмотрели какой-то из случаев входных данных
# (число программистов 0 \le n \le 10000≤n≤1000).
# Обязательно проверяйте свои решения на дополнительных значениях, а не только на тех, что приведены в условии задания.
# Так как задание повышенной сложности, вручную код решений проверяться не будет.
# Если вы столкнулись с ошибкой в первых четырёх тестах, проверьте, что вы используете только русские символы для ответа.
# В остальных случаях ищите ошибку в логике работы программы.
# Sample Input 1:
# 5
# Sample Output 1:
# 5 программистов
# Sample Input 2:
# 0
# Sample Output 2:
# 0 программистов
# Sample Input 3:
# 1
# Sample Output 3:

# 1 программист
# Sample Input 4:
#
# 2
# Sample Output 4:
#
# 2 программиста
s = int (input())
n1 =" программистов"
n2 =" программист"
n3 =" программиста"
if  s>=0:
  if s==0:
    print(str(s) + n1)
  elif s%100>=10 and s%100<=20:
    print(str(s) + n1)
  elif s%10==1:
    print(str(s) + n2)
  elif s%10>=2 and s%10<=4:
    print(str(s) + n3)
  else:
    print(str(s) + n1)

# Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
# которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
# На вход программе подаётся строка из шести цифр.
# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
# Sample Input 1:
# 090234
# Sample Output 1:
# Счастливый
# Sample Input 2:
# 123456
# Sample Output 2:
# Обычный
string = input()
if int(string[0])+int(string[1])+ int(string[2]) == int(string[3])+int(string[4])+ int(string[5]):
    print("Счастливый")
else:
    print("Обычный")

# Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке,
# и после первого введенного нуля выводит сумму полученных на вход чисел.
# Sample Input 1:
#
# 5
# -3
# 8
# 4
# 0
# Sample Output 1:
#
# 14
# Sample Input 2:
#
# 0
# Sample Output 2:
#
# 0
sum = 0
while True:
    integer = int(input())
    if integer != 0:
        sum += integer
    else:
        break

print(sum)

# В Институте биоинформатики между информатиками и биологами устраивается соревнование.
# Победителям соревнования достанется большой и вкусный пирог. В команде биологов aa человек, а в команде информатиков — bb человек.
# Нужно заранее разрезать пирог таким образом, чтобы можно было раздать
# кусочки пирога любой команде, выигравшей соревнование, при этом каждому участнику этой команды должно достаться
# одинаковое число кусочков пирога. И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.
# Напишите программу, которая помогает найти это число.
# Программа должна считывать размеры команд (два положительных целых числа aa и bb, каждое число вводится на отдельной строке) и
# выводить наименьшее число dd, которое делится на оба этих числа без остатка.
# Sample Input 1:
# 1
# 2
# Sample Output 1:
# 2
# Sample Input 2:
# 7
# 5
# Sample Output 2:
# 35
# Sample Input 3:
#
# 15
# 15
# Sample Output 3:
#
# 15

integer = int(input())
integer2 = int(input())

min  = min(integer,integer2)
while True:
    if min % integer == 0 and min % integer2  == 0:
        break
    else:
        min += 1

print(min)

# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.
# Sample Input 1:
#
# 12
# 4
# 2
# 58
# 112
# Sample Output 1:
#
# 12
# 58
# Sample Input 2:
#
# 101
# Sample Output 2:
#
# Sample Input 3:
#
# 1
# 2
# 102
# Sample Output 3:

while True:
    int1 = input()
    int1 = int(int1)
    if int1 > 100:
        break
    elif int1 < 10:
        continue
    else:
        print(int1)

# Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками.
# Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
# Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке.
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].
# Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a \le ba≤b, c \le dc≤d.
# Следуйте формату вывода из примера,
# для разделения элементов внутри строки используйте '\t' — символ табуляции.
# Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.﻿
# Sample Input 1:
# 7
# 10
# 5
# 6
# Sample Output 1:
# 	5	6
# 7	35	42
# 8	40	48
# 9	45	54
# 10	50	60
# Sample Input 2:
# 5
# 5
# 6
# 6
# Sample Output 2:
#
# 	6
# 5	30
# Sample Input 3:
# 1
# 3
# 2
# 4
# Sample Output 3:
#
# 	2	3	4
# 1	2	3	4
# 2	4	6	8
# 3	6	9	12
a, b, c, d = int(input()), int(input()), int(input()), int(input())
for i in range(c, d + 1):
    print('\t', i, end='')
print()
for j in range(a, b + 1):
    print(j, end='\t')
    for k in range(c, d + 1):
        print(j * k, end='\t')
    print()
#
# Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a; b][a;b], которые кратны числу 33.
# В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [-5; 12][−5;12].
# Всего чисел, делящихся на 3, на этом отрезке 6: -3, 0, 3, 6, 9, 12−3,0,3,6,9,12. Их среднее арифметическое равно 4.5
# На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3

# Sample Input:
#
# -5
# 12
# Sample Output:
#
# 4.5

x = int(input())
y = int(input())

count = 0
sum = 0
for j in range (x,y+1):
    if j % 3 != 0:
        continue
    else:
        count += 1
        sum += j
        aver = sum / count

print(aver)
#
# Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C
# (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
# Например, в строке "acggtgttat" процентное содержание символов G и C равно \dfrac4{10} \cdot 100 = 40.0
# 10
# 4
# ​
#  ⋅100=40.0, где 4 -- это количество символов G и C,  а 10 -- это длина строки.
# Sample Input:
# acggtgttat
# Sample Output:
#
# 40.0

string = input().strip().upper()
patternG = 'G'
patternC = 'C'
countG = 0
countC = 0
for i in string:
    if i == patternG:
        countG += 1
    elif i == patternC:
        countC += 1
    result = ((countG + countC) / len(string)) * 100

print(result)

# Узнав, что ДНК не является случайной строкой, только что поступившие в
# нститут биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной
# строки заменяются на этот символ и количество его повторений в этой позиции строки.
# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и
# выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
# Sample Input 1:
# aaaabbcaa
# Sample Output 1:
# a4b2c1a2
# Sample Input 2:
# abc
# Sample Output 2:
# a1b1c1
genome = input()+' '
s = 0
n=genome[0]
for i in genome:
    if n!=i:
        print(n + str(s), end = '')
        s=0
        n=i
    s+=1
# Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
# Используйте метод split строки. ﻿﻿
# Sample Input:
# 4 -1 9 3
# Sample Output:
# 15
array = input().split()
sum = 0
for elem in array:
    elem = int(elem)
    sum += elem

print(sum)

# Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
# Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
# Sample Input 1:
# 1 3 5 6 10
# Sample Output 1:
# 13 6 9 15 7
# Sample Input 2:
# 10
# Sample Output 2:
# 10

x = [int(i) for i in input().split()]  # получаем список чисел на входе
if len(x) == 1:
    print(x[0])
else:
    x.insert(0, x[-1])  # добавляем последнее число входной послед-ти в начало
    x.append(x[1])  # добавляем первое число входной послед-ти в конец
    for i in range(1, len(x) - 1):
        print(x[i+1] + x[i-1], end=' ')

# Напишите программу, которая принимает на вход список чисел в
# одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
# Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
# Sample Input 1:
#
# 4 8 0 3 4 2 0 3
# Sample Output 1:
#
# 0 3 4
# Sample Input 2:
#
# 10
# Sample Output 2:
#
# Sample Input 3:
#
# 1 1 2 2 3 3
# Sample Output 3:
#
# 1 2 3
# Sample Input 4:
#
# 1 1 1 1 1 2 2 2
# Sample Output 4:
#
# 1 2


x = [int(i) for i in input().split()]
x.sort()
x2 = set()
count = 0
for i in range(len(x)-1):
    if x[i] == x[i+1]:
        count +=1
        if count >= 1:
            x2.add(x[i])

for i in x2:
    print(i, end=" ")

# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
# пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0,
# после этого считывание продолжать не нужно.
# В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем,
# что сумма этих чисел равна нулю и выводим сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.﻿
#
# Sample Input:
#
# 1
# -3
# 5
# -6
# -10
# 13
# 4
# -8
# Sample Output:
#
# 340

lst = [int(i) for i in input().split()]
sum = 0
sum2 = 0
for i in range(len(lst)):
    sum += lst[i]
    sum2 = sum2 + (lst[i] ** 2)
    if sum == 0:
        break
print(sum2)



a1 = int (input())
s= a1
s2 = 0+abs(a1**2)
while s!=0:
    a1 = int(input())
    s = s + a1
    s2 = s2+abs(a1)**2
    if s==0:
        break
print(s2)

s=[int(input())]
while sum(s)!=0: s.append(int(input()))
print(sum([i**2 for i in s]))

s, d = 0, 0
while True:
    a = int(input())
    s += a
    d += a*a
    if s == 0:
        break
print(d)


#
# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
# ... (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число
# n — столько элементов последовательности должна отобразить программа.
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
# Sample Input:
# 7
# Sample Output:
# 1 2 2 3 3 3 4

S,n = [],int(input()) # создаем пустой список и вводим значение переменной n
for i in range(1, n + 1):#  для значения списка в промежутке от 1-го по n
    S.extend([i]*i) # добавляем в конец списка S возрастающую в i раз последовательность
print(*S[:n]) # выводим на печать весь список S (*S) от нуля по n

n = int(input())
a = []
i = 0
while len(a) < n:
    a += [i] * i
    i += 1
print(*a[:n])

n = int(input())
count = 0
curr = 1
for i in range(n):
    print(curr, end=' ')
    count += 1
    if count == curr:
        curr += 1
        count = 0

import math
x = int(input())
print(*[int( 1/2 + math.sqrt(2 * n) ) for n in range(1, x + 1)])

a = int(input())
c = 0
for i in range(a+1):
    for j in range(i):
        c += 1
        if c<a+1:
            print(i, end=' ')


n=int (input ()) # считуем переменную
i=1
count=0
while count<n:  # условие на превышение переборов
    for j in range (i):  # проходим необходимое количесвто переборов
        if count<n:  # условие на превышение переборов
            print(i, end=' ')
            count+=1
        else:
            break
    i+=1

n=int(input())
j=1
a=0
for i in range(1,n+1):
    j=0
    while j!=i and a!=n:
        print(i,end=' ')
        j+=1
        a+=1
