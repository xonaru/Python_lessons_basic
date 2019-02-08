#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random
MAX_Bo4enki = 90



class Bo4enki:
    def __init__(self):

        self.bo4 = [i for i in range(1,MAX_Bo4enki + 1)]

    @property
    def give(self):
        if len(self.bo4) == 0:
            return None
        return self.bo4.pop(random.randint(1, len(self.bo4)) - 1)


class NewCard(Bo4enki):
    def __init__(self):
        Bo4enki.__init__(self)
        self.cardd = []

    def line(self):
        g = [self.give, self.give, self.give, self.give, self.give]
        g.sort()
        for i in range(4):
            g.insert(random.randint(0,9),' ')
        return g

    def card(self):

        for i in range(3):
            self.cardd.extend(self.line())
        return self.cardd


class Control(NewCard):
    def __init__(self):

        NewCard.__init__(self)
        self.a1 = NewCard().card()
        self.a2 = NewCard().card()
        self.b0 = self.give
        self.i = self.a1.count(self.b0)
        self.j = self.a2.count(self.b0)
        self.a1_i, self.a2_j = 0, 0
        self.win = True
        self.print

    @property
    def print(self):
        print('Новый бочонок: {} (осталось {})'.format(self.b0, len(self.bo4)))
        print('------ Ваша карточка -----')
        print('{} {} {} {} {} {} {} {} {}'.format(self.a1[0], self.a1[1], self.a1[2], self.a1[3], self.a1[4], self.a1[5], self.a1[6], self.a1[7], self.a1[8]))
        print('{} {} {} {} {} {} {} {} {}'.format(self.a1[9], self.a1[10], self.a1[11], self.a1[12], self.a1[13], self.a1[14],self.a1[15], self.a1[16], self.a1[17]))
        print('{} {} {} {} {} {} {} {} {}'.format(self.a1[18], self.a1[19], self.a1[20], self.a1[21], self.a1[22], self.a1[23],self.a1[24], self.a1[25], self.a1[26]))
        print('--------------------------\n-- Карточка компьютера ---')
        print('{} {} {} {} {} {} {} {} {}'.format(self.a2[0], self.a2[1], self.a2[2], self.a2[3], self.a2[4], self.a2[5], self.a2[6], self.a2[7], self.a2[8]))
        print('{} {} {} {} {} {} {} {} {}'.format(self.a2[9], self.a2[10], self.a2[11], self.a2[12], self.a2[13], self.a2[14], self.a2[14], self.a2[16], self.a2[17]))
        print('{} {} {} {} {} {} {} {} {}'.format(self.a2[18], self.a2[19], self.a2[20], self.a2[21], self.a2[22], self.a2[23], self.a2[24], self.a2[25], self.a2[26]))
        print('--------------------------')

    def update(self, bool):
        if self.j > 0:
            self.a2_j += 1
            self.a2.insert(self.a2.index(self.b0), 'X')
            self.a2.remove(self.b0)
        if bool:
            self.a1_i += 1
            self.a1.insert(self.a1.index(self.b0), 'X')
            self.a1.remove(self.b0)
        if a.a2_j == 15 and a.a1_i == 15:
            print("Ничья, игра окончена")
            self.win = False
            return False
        elif a.a2_j == 15:
            print("Выйграл компьютер, игра окончена")
            self.win = False
            return False
        elif a.a1_i == 15:
            print("Вы выйграли, игра окончена")
            self.win = False
            return False
        else:
            self.b0 = self.give
            self.i = self.a1.count(self.b0)
            self.j = self.a2.count(self.b0)
            return
        self.b0 = self.give
        self.i = self.a1.count(self.b0)
        self.j = self.a2.count(self.b0)


a = Control()
count = 0
while a.win:
    print(a.i, a.j,"\n", a.a1_i, a.a2_j)
    answer = input('Зачеркнуть цифру? (Y/N)')

    if count == 1:
        print("Неверная команда, игра окончена")
        break

    elif (answer == 'N' or answer == 'n') and a.i > 0:
        print("Вы не заметили цифру, игра окончена")
        break
    elif answer == 'N' or answer == 'n'and a.i == 0:
        print('Верно, цифры нет')
        if a.update(False) == True:
            a.print
    elif (answer == 'Y' or answer == 'y') and a.i == 0:
        print("Цифры не было, игра окончена")
        break
    elif (answer == 'Y' or answer == 'y') and a.i > 0:
        print('Верно, цифра есть')
        if a.update(True) == True:
            a.print
    else:
        print('Некоректный ввод, попробуйте еще раз')
        count +=1



