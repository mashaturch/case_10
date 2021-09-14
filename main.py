import sys
import ru_local

file = open('input.txt', encoding='utf-8')

price = {'АИ-80': 32, 'АИ-92': 46, 'АИ-95': 49, 'АИ-98': 59}

station = {1: 0, 2: 0, 3: 0}
for line in file:
    time, liter, petrol = line.split()
    print(liter)
    if station[]
