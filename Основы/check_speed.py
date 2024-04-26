from collections import Counter

import time
import json
import random
import calendar
from zipfile import ZipFile
from datetime import datetime
from datetime import date, timedelta
from typing import Generator
from string import punctuation
from functools import reduce

# d = ['str'+str(i) for i in range(1000)]
my_month = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
# test_month = list(set([random.choice(my_month) for _ in range(9)]))
# test_list = [random.choice(d) + ' 10 ' + random.choice(my_month) for _ in range(1000)]
#    with open('words_400k.txt', 'r', encoding='utf-8') as file:
#        return  sorted({line:1 for line in file.read().upper().split() if line.endswith('ЕЯ')}, key = lambda x: (len(x), x))
# inp = ' '.join([str(random.choice(range(-100, 100))) for _ in range(10000)])
# lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
stroka_chisel = ' '.join([str(random.randint(1, 5)) for _ in range(100_000)])
stroka_bukv = ' '.join([random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm ') for _ in range(100_000)])
stroka_slov = ' '.join(
    [''.join(random.sample('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm', 4)) for _ in range(1_000)])
stroka_bukv_i_chisel = [random.choice(['Q', 1]) for _ in range(10_000)]
list_num = [random.randint(0, 1_000) for _ in range(100_000)]
list_num_and_str = [random.choice([-3.5, 3.5, -2, -1, 2, 1, 0, 'r', 'R']) for _ in range(1_000)]
slovar = {str(key): value for key, value in enumerate(stroka_chisel)}
list_list = [[random.randint(-1_000, 1_000) for _ in range(random.randint(1, 1_000))] for _ in
             range(random.randint(1, 1_000))]

human = {
    "id": 1,
    "parents": [1, 2, 3, 4],
    "chief": {
        "name": "Paul",
        "age": 50
    },
    "age": 22
}


def check():
    #    with open('words_400k.txt', 'r', encoding='utf-8') as file:
    #        return {k:1 for k in file.read().split()}
    lst = list(map(int, stroka_chisel.split()))
    return lst == sorted(lst)

# чужая функция
def check2():
    # with open('words_400k.txt', 'r', encoding='utf-8') as file:
    #    return {k for k in file.read().split()}
    lst = list(map(int, stroka_chisel.split()))
    flag = True
    for key, value in enumerate(lst[1:]):
        if value < lst[key]:
            flag = False
            break
    return flag



test_range = 1_000
_print = True
if _print:
    print(check())
    print(check2())

print('--------------Starting...------------------')

time_1_monotonic = 0
for _ in range(test_range):
    start_monotonic = time.monotonic()
    check()
    time_1_monotonic += time.monotonic() - start_monotonic
print('25%...', end='')
time_2_monotonic = 0
for _ in range(test_range):
    start_monotonic = time.monotonic()
    check2()
    time_2_monotonic += time.monotonic() - start_monotonic
print('50%...', end='')
time_1_perf_counter = 0
for _ in range(test_range):
    start_perf_counter = time.perf_counter()
    check()
    time_1_perf_counter += time.perf_counter() - start_perf_counter
print('75%...', end='')
time_2_perf_counter = 0
for _ in range(test_range):
    start_perf_counter = time.perf_counter()
    check2()
    time_2_perf_counter += time.perf_counter() - start_perf_counter
print('100%...')
# print = print2

print('-------------- Тест через monotonic --------------')
print('---- Моя функция -- ', end='')
print(f'Время выполнения: {str(round(time_1_monotonic, 10))}')
print('-- Чужая функция -- ', end='')
print(f'Время выполнения: {str(round(time_2_monotonic, 10))}')
print('----------- Тест через perf.counter -------------')
print('---- Моя функция -- ', end='')
print(f'Время выполнения: {str(round(time_1_perf_counter, 10))}')
print('-- Чужая функция -- ', end='')
print(f'Время выполнения: {str(round(time_2_perf_counter, 10))}')
