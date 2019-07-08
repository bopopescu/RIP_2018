import random

#Генератор последовательных значений ключей

def field(items, *args):

    assert len(args)>0

    for i in items:
        d = dict()

        for arg in args:

            #если передается только 1 аргумент, сразу возвращаем значение
            if (len(args) == 1) and (arg in i.keys()):
                yield i[arg]

            #если передается несколько аргументов, записываем значение в словарь, затем возвращаем словарь
            if (len(args) > 1) and (arg in i.keys()):
                d[arg] = i[arg]
                yield d


#Генератор случайных чисел

def gen_random(begin, end, nums):

    for num in range(nums):
        yield random.randint(begin, end)
