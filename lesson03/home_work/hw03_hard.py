# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
#2



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

#1

from fractions import Fraction

#arr = '-2 3/4 - 2 5/42'
arr = '-2 -1/2 - -5 -2/6'


def find():

    count = 0

    for i in arr:

        if i == '+':

            summ = True
            arr.pop(count)
            return(count,summ)

        elif i == '-':

            summ = False
            arr.pop(count)
            return (count,summ)

        count += 1



def sum(summ,x,y):

    if summ:

        if y ==2:

          a = Fraction(arr[0])
          b = Fraction(arr[1])

        if y == 3:

          a = Fraction(arr[0])
          b = Fraction(arr[1])
          c = Fraction(arr[2])
          b = b + c
          return a + b

        if y == 4:

          a = Fraction(arr[0])
          b = Fraction(arr[1])
          c = Fraction(arr[2])
          d = Fraction(arr[3])
          a = a + b
          b = c + d
          return a + b

    if summ == False:

      if y ==2:

        a = Fraction(arr[0])
        b = Fraction(arr[1])
        return a + b

      if y == 3 & x == 1:

        a = Fraction(arr[0])
        b = Fraction(arr[1])
        c = Fraction(arr[2])
        b = -b + c
        return a + b

      if y == 3 & x == 2:

        a = Fraction(arr[0])
        b = Fraction(arr[1])
        c = Fraction(arr[2])
        b = b - c
        return a + b

      if y == 4:

        a = Fraction(arr[0])
        b = Fraction(arr[1])
        c = Fraction(arr[2])
        d = Fraction(arr[3])
        a = a + b
        b = -c + d
        return a + b

def q(str):

    str = str.split('/')
    a = int(str[0])
    b = int(str[1])

    if a > b:
        unit =  a // b
        part =  a % b
        print ('{} {}/{}'.format(unit,part,b))

    else:

        print('{}/{}'.format(a, b))



arr = arr.split(' ')
x , summ = find()

result = (str(sum(summ,x,len(arr))))

if result == '0':

    print('0')

else:

    q(result)
    
#2
import os

DIR = 'data'
FILE = 'workers'
FILE_2 = 'hours_of'

def read_data():

    f = open(os.path.join(DIR, FILE), 'r', encoding='UTF-8')

    while read(f):

     continue

def read(f):

    readed = f.readline().splitlines()

    if readed == []:

        return False

    readed = readed[0].split()
    print(readed)
    find(readed)

    return True

def find(file):

    FILE_2 = 'hours_of'
    f = open(os.path.join(DIR, FILE_2), 'r', encoding='UTF-8')
    print(f.read(1))

    while compare(file,f):

        continue

def compare(file,f):

        z = (f.readline().splitlines()[0].split())

        if (z[0] == file[0]) & (z[1]==file[1]):

            new_file(z,file)

        else:

            return True

def new_file(z,file):

    with open(os.path.join( DIR, 'new'), 'a', encoding='UTF-8') as f:
        f.write(' '.join(file))
        f.write(' ' + z[2])

        if file[0] == 'Имя':

            f.write(' Зарплата\n')

        else:

            f.write(' ' + (new_add(z,file)))
            f.write('\n')
            
def new_add(z,file):
    
    print(file[4],z[2])
    
    if ((int(file[4]) >= int(z[2]))):
        
        tt = (int(z[2]) / int(file[4])) * int(file[2])
        print(tt)
        tt = round(tt, 2)
        return str(tt)

    else:

        tt = (int(z[2]) - int(file[4]))/int(file[4])*(int(file[2])*2)+int(file[2])
        tt = round(tt, 2)
        return str(tt)





read_data()

#3

import os

DIR = 'data'
FILE = 'fruits.txt'
Alhabet = (list(map(chr, range(ord('А'), ord('Я')+1))))




def write_fruit(fruit,letter):

    FILE = 'fruit_' + letter
    DIR = 'data'
    type = 'a'

    with open(os.path.join( DIR, FILE), type, encoding='UTF-8') as f:

        f.write(fruit + '\n')

def read_fruit(f, i):

    readed = f.readline().splitlines()

    if readed == []:

        f.close()
        return False

    elif readed[0] == '':
        return True


    elif list(readed[0])[0] == i:

            write_fruit(readed[0], i)
            return True
    else:

        return True

for i in Alhabet:

     f = open(os.path.join(DIR, FILE), 'r', encoding='UTF-8')

     while read_fruit(f, i):

         continue
