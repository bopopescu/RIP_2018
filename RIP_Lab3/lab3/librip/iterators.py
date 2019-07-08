import types

class Unique:

    def __init__(self, items, ignore_case = False, **kwards):

        if isinstance(items, types.GeneratorType):        #инициализация для генератора
            self.items = list(items)

        else:                                             #инициализация массива

            self.items = items

        self.long = len(self.items)                       #длина списка

        self.index = 0                                    #текущий элемент списка

        self.showel = []                                  #список выведенных элементов

        self.ignore_case = ignore_case

    def __next__(self):

        while self.index < self.long:

            if not self.ignore_case:
                if self.items[self.index] not in self.showel:
                    self.showel.append(self.items[self.index])
                self.index += 1

            else:
                if str(self.items[self.index]).lower() not in (str(i).lower() for i in self.showel):
                    self.showel.append(self.items[self.index])
                self.index += 1

        return self.showel


    def __iter__(self):
        return self
