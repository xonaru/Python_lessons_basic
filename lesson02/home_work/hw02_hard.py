# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

#1

equation = 'y = -12x + 11111140.2121'
x = 2.5
b = 1

equation = equation.split(' ')
print(equation)

for num in equation:
    if num == 'y':
        continue
    elif num == '=':
        continue
    elif num == '+':
        operation = True
        continue
    elif num == "-":
        operation = False
        continue
    elif num.find('x') >= 0:
        k = num.split('x')
        k = k[0]
        k = float(k)
    else:
        b = num
        b = float(b)


if operation:
    function = k*x + b
    print('{} = {} * {} + {}'.format(function, k, x, b))
else:
    function = k*x - b
    print('{} = {} * {} - {}'.format(function, k, x, b))



#2

date = '01.11.1985'

month_max_len = 0
month_name = ''
error = 0
error_d = 0
error_y = 0

months = [['01','Январь',31],['02','Февраль',28],['03','Март',31],['04','Апрель',30],['05','Май',31],['06','Июнь',30],['07','Июль',31],['08','Август',31],['09','Сентябрь',30],['10','Октябрь',31],['11','Ноябрь',30],['12','Декабрь',31]]

date = date.split('.')

for month in months:
    if month[0] == date[1]:
        A = True
        month_max_len = month[2]
        month_name = month[1]
        break
    else:
        error = error +1
if error == 12:
    print('Ошибка ввода месяца')

if int(date[0]) < 1 | int(date[0]) > month_max_len | len(date[0]) != 2:
    print('Ошибка ввода дня')
    error_d = 1
elif int(date[2]) < 1 | int(date[2]) > 9999 | len(date[2]) != 4:
    print('Ошибка ввода года')
    error_y = 1
elif (error != 12) | (error_y != 1) | (error_d != 1):
    print('GOOD')


#3

import math

max_flat = 2 * 10 ** 9

N_Y = True
data = []
start_floor_of_cell = 1
sum_flats = 0
cell = 1
position = 0
remains = 0
floor = 0
max_flat_in_cell = 0
count = 2

while sum_flats <= max_flat:
    sum_flats = sum_flats + cell ** 2
    start_floor_of_cell = start_floor_of_cell + cell - 1
    data[len(data):] = [cell, start_floor_of_cell, sum_flats]
    cell = cell + 1

while N_Y:
    number = int(input('Введите номер квартиры от 1 до 2*10^9 : '))

    while ((number <= 1) | (number >= 2 * 10 ** 9)):
        print('Ошибка')
        number = int(input('Введите номер квартиры от 1 до 2*10^9 : '))

    while number > max_flat_in_cell:
        max_flat_in_cell = data[count]
        count = count + 3

    cell_of_number = data[count - 5]
    start_floor_of_number = data[count - 4]

    floor = start_floor_of_number + (cell_of_number - 1 - ((max_flat_in_cell - number) // cell_of_number))
    remains = ((max_flat_in_cell - number) % cell_of_number)

    if remains > 0:
        position = cell_of_number - remains

    else:
        position = cell_of_number

    print('На {} этаже {} по счету слева'.format(floor, position))
    while True:
        answer = input('Повторим N \ Y ? : ')
        if (answer == 'N') | (answer == 'n'):
            N_Y = False
            break
        elif (answer == 'y') | (answer == 'Y'):
            N_Y = True
            break
        else:
            print('Ошибка')

  
