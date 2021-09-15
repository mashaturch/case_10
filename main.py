import sys
import ru_local

file = open('input.txt', encoding='utf-8')
azs = open('azs.txt', encoding='utf-8')

price = {'АИ-80': 32, 'АИ-92': 46, 'АИ-95': 49, 'АИ-98': 59} #цены на бензин
petrol_with_machine = {} #словарь номер автомата + какие там есть бензины
machine_with_set_time = {} #словарь с номером автомата + до скольких машина там находится
machine_with_max_quantity = {} #словарь с номером автомата + макс очередь


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

for line in file:
    time, liter, petrol = line.split()
    hours, minutes = time.split(':')

    print(time)


