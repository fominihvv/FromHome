import csv
from datetime import datetime
import time
import calendar
from datetime import date, timedelta
import json
import random

from string import punctuation

# d = ['str'+str(i) for i in range(1000)]
my_month = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
# test_month = list(set([random.choice(my_month) for _ in range(9)]))
# test_list = [random.choice(d) + ' 10 ' + random.choice(my_month) for _ in range(1000)]


#    with open('words_400k.txt', 'r', encoding='utf-8') as file:
#        return  sorted({line:1 for line in file.read().upper().split() if line.endswith('ЕЯ')}, key = lambda x: (len(x), x))


# inp = ' '.join([str(random.choice(range(-100, 100))) for _ in range(10000)])
# lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']

stroka_chisel = ' '.join([str(random.randint(1, 20_000)) for _ in range(100_000)])
stroka_bukv = ' '.join([random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm') for _ in range(10_000)])
stroka_bukv_i_chisel = (random.choice(['Q', 1]) for _ in range(100_000))
numbers = list(range(1, 1_000))

# моя функция
def check():
    #    with open('words_400k.txt', 'r', encoding='utf-8') as file:
    #        return {k:1 for k in file.read().split()}
    return sum(1 for arg in stroka_bukv_i_chisel if isinstance(arg, str))


# чужая функция
def check2():
    # with open('words_400k.txt', 'r', encoding='utf-8') as file:
    #    return {k for k in file.read().split()}
#    return len([1 for arg in stroka_bukv_i_chisel if isinstance(arg, str)])
    return sum(isinstance(args, str) for args in stroka_bukv_i_chisel)


test_range = 10000

print('-------------- Тест через monotonic -------------')
print('---- Моя функция -- ', end='')
time_1_monotonic = 0
for _ in range(test_range):
    start_monotonic = time.monotonic()
    check()
    time_1_monotonic += time.monotonic() - start_monotonic

print('Время выполнения: ' + str(time_1_monotonic))
print('-- Чужая функция -- ', end='')

time_2_monotonic = 0
for _ in range(test_range):
    start_monotonic = time.monotonic()
    check2()
    time_2_monotonic += time.monotonic() - start_monotonic

print('Время выполнения: ' + str(time_2_monotonic))
print('----------- Тест через perf.counter ------------')
print('---- Моя функция -- ', end='')

time_1_perf_counter = 0
for _ in range(test_range):
    start_perf_counter = time.perf_counter()
    check()
    time_1_perf_counter += time.perf_counter() - start_perf_counter

print('Время выполнения: ' + str(time_1_perf_counter))
print('-- Чужая функция -- ', end='')

time_2_perf_counter = 0
for _ in range(test_range):
    start_perf_counter = time.perf_counter()
    check2()
    time_2_perf_counter += time.perf_counter() - start_perf_counter

print('Время выполнения: ' + str(time_2_perf_counter))