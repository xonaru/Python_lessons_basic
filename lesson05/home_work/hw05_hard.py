# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil

print("sys.argv = ", sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_namec> - создание директории")
    print("cp <file_name> - создание копии указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")

def make_dir():
        if not dir_name:
            print("Необходимо указать имя директории вторым параметром")
            return
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.mkdir(dir_path)
            print('директория {} создана'.format(dir_name))
        except FileExistsError:
            print('директория {} уже существует'.format(dir_name))

def copy_file():
    if not dir_name:
        print(" Необходимо указать имя копируемого файла")
        return

    file_path = os.path.join(os.getcwd(), dir_name)
    splitext = os.path.splitext(file_path)
    spli = os.path.splitext(dir_name)

    if os.path.isfile(file_path):

        shutil.copy2(file_path, os.path.join(os.getcwd(), '{}_copy2{}'.format(splitext[0], splitext[1])))
        print('Файл {} успешно скопирован как {}_copy2{}'.format(dir_name, spli[0],spli[1]))

    else:
        print('Копируемый объект не является файлом')


def remove_file():

    if not dir_name:

        print(" Необходимо указать имя удаляемого файла")
        return

    if os.path.isfile(os.path.join(os.getcwd(), dir_name)):

        answer = input('Вы уверенны, что хотите удалить файл "{}"? [Y/N]'.format(dir_name))

        if answer == 'y' or answer == 'Y':

            try:

                os.remove(dir_name)
                print("Файл {} успешно удален".format(dir_name))

            except Exception:

                print("Файл занят другой программой")
        else:
            print(" Удаление файла {} отменено ".format(dir_name))
    else:
        print('Файл не существует')


def change_dir():
    if not dir_name:

        print("Необходимо указать имя директории вторым параметром")
        return

    try:

        os.chdir(dir_name)
        print('Новая дериктория {}'.format(os.getcwd()))

    except FileNotFoundError:

        print('Такой папки не существует')


def full_dir():

    print(" Полный путь текущей директории : " + os.getcwd())


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": full_dir,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
