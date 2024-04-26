import csv
from datetime import datetime
import time
import calendar
from datetime import date, timedelta
import json
import random

from string import punctuation

#d = ['str'+str(i) for i in range(1000)]
#my_month = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
#test_month = list(set([random.choice(my_month) for _ in range(9)]))
#test_list = [random.choice(d) + ' 10 ' + random.choice(my_month) for _ in range(1000)]

stroka_chisel = ' '.join([str(random.randint(1, 20_000)) for _ in range(100_000)])

# моя функция
def check():
    with open('word_4k.txt', 'r', encoding='utf-8') as file:
        return len(file.read().split('ея'))-1

# чужая функция
def check2():
    with open('word_4k.txt', 'r', encoding='utf-8') as file:
        return any('ея' in word.lower() for word in file.read().split())
    
test_range = 500

print('--------- Тест через monotonic --------')
print('--- Моя функция ---', end='')
time_1_monotonic = 0 
for _ in range(test_range):
    start_monotonic = time.monotonic()
    check()
    time_1_monotonic += time.monotonic() - start_monotonic

print(' ' + str(time_1_monotonic))
print('-- Чужая функция --', end='')

time_2_monotonic = 0 
for _ in range(test_range):
    start_monotonic = time.monotonic()
    check2()
    time_2_monotonic += time.monotonic() - start_monotonic

print(' ' + str(time_2_monotonic))
print()
print('------ Тест через perf.counter --------')
print('--- Моя функция ---', end='')

time_1_perf_counter = 0
for _ in range(test_range):
    start_perf_counter = time.perf_counter()
    check()
    time_1_perf_counter += time.perf_counter() - start_perf_counter

print(' ' + str(time_1_perf_counter))
print('-- Чужая функция --', end='')

time_2_perf_counter = 0
for _ in range(test_range):
    start_perf_counter = time.perf_counter()
    check2()
    time_2_perf_counter += time.perf_counter() - start_perf_counter

print(' ' + str(time_2_perf_counter))