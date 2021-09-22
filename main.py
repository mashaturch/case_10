import sys
import ru_local
import math
import random
import datetime



file = open('input.txt', encoding='utf-8')
azs = open('azs.txt', encoding='utf-8')

price = {'АИ-80': 32, 'АИ-92': 46, 'АИ-95': 49, 'АИ-98': 59} #цены на бензин
petrol_with_machine = {} #словарь номер автомата + какие там есть бензины
machine_with_set_time = {} #словарь с номером автомата + до скольких машина там находится
machine_with_max_quantity = {} #словарь с номером автомата + макс очередь
departure_time = {} #словарь с данными отъезда
arrival_time = {} #словарь с данными приезда



for line in azs:

    data_input = list(line.split())

    machine = data_input[0]
    max_quantity = data_input[1]
    petrols = list(data_input[2::])
    for petrol in petrols:  #создаёт словарь с бензином и какие колонки есть
        if petrol not in petrol_with_machine:
            petrol_with_machine[petrol] = [int(machine)]
        else:
            petrol_with_machine[petrol].append(int(machine))

    machine_with_max_quantity[int(machine)] = int(max_quantity) #создаёт словарь словарь с номером автомата + макс очередь

print (petrol_with_machine)
print(machine_with_max_quantity)

"""import datetime

tm3 = datetime.timedelta(hours=0, minutes=30) + datetime.timedelta(hours=2, minutes=30)
print('0' + ((str(tm3)).split(':')[0]))
"""


for line in file:
    time, liter, petrol = line.split()
    hours_in, minutes_in = map(int, time.split(':'))
    if int(liter) >= 20:
        refueling_time = math.ceil(int(liter) / 10) + random.randint(-1, 1)
    else:
        refueling_time = math.ceil(int(liter) / 10)
    if time not in arrival_time:
        arrival_time[time] = [time, petrol, liter, refueling_time]
    else:
        arrival_time[time].append([time, petrol, liter, refueling_time])

    time_near_the_machine = str(datetime.timedelta(hours=hours_in, minutes=minutes_in) + datetime.timedelta(hours=0, minutes=refueling_time))[::-2]

    if time_near_the_machine not in departure_time:
        departure_time[time_near_the_machine] = [time, petrol, liter, refueling_time]
    else:
        departure_time[time_near_the_machine].append([time, petrol, liter, refueling_time])

print (arrival_time)
print()
print(departure_time)

        



