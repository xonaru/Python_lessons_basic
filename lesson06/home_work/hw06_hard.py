# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os


class Worker:
    def __init__(self, line):

        name, second_name, pay, post, task = line.split()
        self.fullname = name + ' ' + second_name
        self.pay = float(pay)
        self.task = float(task)

    def calc(self):

        worked = hours.get(self.fullname)

        if worked >= self.task:

            f_pay = self.pay * (2 * (worked / self.task - 1) + 1)

        else:

            f_pay = self.pay * (worked / self.task)
            
        return f_pay


def new(x):

    name, second_name, hours_w = x.split()
    return name + ' ' + second_name, float(hours_w)


path_w = os.path.join('data', 'workers')
path_h = os.path.join('data', 'hours_of')

with open(path_w, "r", encoding='UTF-8') as f:
    f.readline()  # Удаляем заголовок
    workers = list(map(Worker, f.readlines()))

with open(path_h, "r", encoding='UTF-8') as f:
    f.readline()  # Уаляем заголовок
    hours_of = f.readlines()

hours = {person: hours for person, hours in map(new, hours_of)}

print({worker.fullname: round(worker.calc(), 2) for worker in workers})
