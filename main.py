import os
import time
import colorama
from colorama import *


'''
created by Litring.
version 0.1
'''


class VisualMenu:

    def __init__(self, title='Меню', terminal=True):
        self._title = title
        self._terminal = terminal
        self.__terminal_check()

        self._item = {}
        self._itemCommand = {}
        self._itemDescription = {}

        colorama.init()

    # Добавляет элемент
    def add_menu_item(self, context, command=None, description=None, index=None):
        if index is None:
            index = len(self._item)

        self._item[index] = context
        self._itemCommand[index] = command
        self._itemDescription[index] = description

    # Выполнение команды
    def execute_command(self, index):
        if self._itemCommand.get(index) is not None:
            self._itemCommand.get(index)()
        else:
            print(Fore.RED, 'Инструкции небыли переданы', Fore.RESET)
            input('Для продолжения нажмите Enter ')

    # Рисуем / выводим меню
    def print_menu(self):
        if self._terminal is False:
            os.system('cls')
        else:
            for i in range(100):
                print('')

        print('      ', self._title)
        for x in range(len(self._item)):
            print(f"{Style.BRIGHT}[{x}] - {self._item[x]}",
                  f"{Style.NORMAL}    {self._itemDescription[x]}",
                  Fore.RESET)

    # Получение индекса через наименование
    def get_index_item(self, name):
        name = str.lower(name)
        for x in range(len(self._item)):
            if name == str.lower(self._item.get(x)):
                return int(x)
        return int(-1)

    # Проверка на наличие экрана
    def __terminal_check(self):
        try:
            os.get_terminal_size()
            self._terminal = False
        except ValueError:
            pass
