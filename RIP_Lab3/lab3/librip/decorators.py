def print_result(func):
    def data(*arg):

    # печатаем имя функции
        print('\n{}\n'.format(func.__name__))

        if isinstance(func(*arg), list):
            print_list(func(*arg))
        else:
            if isinstance(func(*arg), dict):
                print_dict(func(*arg))
            else:
                print(func(*arg))
        return func(*arg)
    return data

def print_list(l):
    for j in l:
        print(j)
    return

def print_dict(d):
    for i in d:
        print('{} = {}'.format(i, d[i]))
    return

# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2
