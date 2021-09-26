
import ru_local
import math
import random
import datetime



file = open('input.txt', encoding='utf-8')
azs = open('azs.txt', encoding='utf-8')

price = {'АИ-80': 32, 'АИ-92': 46, 'АИ-95': 49, 'АИ-98': 59} #цены на бензин
petrol_with_machine = {} #словарь бенизн + номера автоматов
machine_with_petrol = {} #словарь номера автомата + бензины
machine_with_max_quantity = {} #словарь с номером автомата + макс очередь
departure_time = {} #словарь с данными отъезда
arrival_time = {} #словарь с данными приезда
quantity_people_near_machine = {} #словарь с количество людей возле автомата в данный момент
cars_near_the_machine = {} #время приезда + номер автомата
the_number_of_cars_left = 0
amount_of_petrol = {}

for line in azs:

    data_input = list(line.split())

    machine = data_input[0]
    max_quantity = data_input[1]
    petrols = list(data_input[2:])
    for petrol in petrols:  # создаёт словарь с бензином и какие колонки есть
        if petrol not in petrol_with_machine:
            petrol_with_machine[petrol] = [int(machine)]
        else:
            petrol_with_machine[petrol].append(int(machine))
        if int(machine) not in machine_with_petrol:
            machine_with_petrol[int(machine)] = [petrol]
        else:
            machine_with_petrol[int(machine)].append(petrol)

        if petrol not in amount_of_petrol:
            amount_of_petrol[petrol] = 0

    machine_with_max_quantity[int(machine)] = int(max_quantity) #создаёт словарь словарь с номером автомата + макс очередь
    quantity_people_near_machine[int(machine)] = 0 #создает словарь с номеромом автомата + количество людей сейчас


for line in file:
    time, liter, petrol = line.split()
    hours_in, minutes_in = map(int, time.split(':'))
    time = str(datetime.timedelta(hours=hours_in, minutes=minutes_in))[:-3]
    if int(liter) > 10:
        refueling_time = math.ceil(int(liter) / 10) + random.randint(-1, 1)
    else:
        refueling_time = math.ceil(int(liter) / 10) + random.randint(0, 1)
    if time not in arrival_time:
        arrival_time[time] = [time, petrol, liter, refueling_time]
    else:
        arrival_time[time].append([time, petrol, liter, refueling_time])

    time_near_the_machine = str(datetime.timedelta(hours=hours_in, minutes=minutes_in)
                                + datetime.timedelta(hours=0, minutes=refueling_time))[:-3]


main_time = datetime.timedelta(hours=0, minutes=1)
while main_time != datetime.timedelta(hours=24, minutes=0):
    if str(main_time)[:-3] in departure_time:
        quantity_people_near_machine[cars_near_the_machine[departure_time[str(main_time)[:-3]][0]]] -= 1
        print('В', str(main_time)[:-3], 'клиент', departure_time[str(main_time)[:-3]][0],
              departure_time[str(main_time)[:-3]][1], departure_time[str(main_time)[:-3]][2],
              departure_time[str(main_time)[:-3]][3], 'заправил свой автомобиль и покинул АЗС')
        for i in range(len(machine_with_max_quantity)):
            print('Автомат №', i + 1, ' ', ' максимальная очередь: ', machine_with_max_quantity[i + 1],
                  ' Марки бензина: ', ', '.join(machine_with_petrol[i + 1]), ' ', ' -> ',
                  '*' * quantity_people_near_machine[i + 1], sep='')

    if str(main_time)[:-3] in arrival_time:
        machine = 0
        quantity_machine = 0
        for i in range(1, len(machine_with_max_quantity) + 1):
            quantity_machine += machine_with_max_quantity[i]
        i = 0

        while i != (len(petrol_with_machine[arrival_time[str(main_time)[:-3]][1]])):
            if quantity_people_near_machine[petrol_with_machine[arrival_time[str(main_time)[:-3]][1]][i]] !=\
                    machine_with_max_quantity[petrol_with_machine[arrival_time[str(main_time)[:-3]][1]][i]]:
                if quantity_machine > quantity_people_near_machine[petrol_with_machine[arrival_time[str(main_time)[:-3]][1]][i]]:
                    machine = petrol_with_machine[arrival_time[str(main_time)[:-3]][1]][i]
                    quantity_machine = quantity_people_near_machine[petrol_with_machine[arrival_time[str(main_time)[:-3]][1]][i]]

            i += 1

        if machine == 0:
            print('В', str(main_time)[:-3], 'новый клиент:', arrival_time[str(main_time)[:-3]][0],
                  arrival_time[str(main_time)[:-3]][1], arrival_time[str(main_time)[:-3]][2],
                  arrival_time[str(main_time)[:-3]][3], 'не смог заправить свой автомобиль и покинул АЗС')
            for i in range(len(machine_with_max_quantity)):
                print('Автомат №', i + 1, ' ', ' максимальная очередь: ', machine_with_max_quantity[i + 1],
                      ' Марки бензина: ', ', '.join(machine_with_petrol[i + 1]), ' ', ' -> ',
                      '*' * quantity_people_near_machine[i + 1], sep='')
            the_number_of_cars_left += 1


        else:
            cars_near_the_machine[str(main_time)[:-3]] = machine
            quantity_people_near_machine[machine] += 1

            if str(main_time + datetime.timedelta(hours=0, minutes=(arrival_time[str(main_time)[:-3]][3])))[:-3] not in departure_time:
                departure_time[str(main_time + datetime.timedelta(hours=0,minutes=(arrival_time[str(main_time)[:-3]][3])))[:-3]] = arrival_time[str(main_time)[:-3]]
            else:
                departure_time[str(main_time + datetime.timedelta(hours=0, minutes=(arrival_time[str(main_time)[:-3]][3])))[:-3]].append(arrival_time[str(main_time)[:-3]])

            print('В ', str(main_time)[:-3], ' ', 'новый клиент ', arrival_time[str(main_time)[:-3]][0], ' ',
                  arrival_time[str(main_time)[:-3]][1], ' ', arrival_time[str(main_time)[:-3]][2], ' ',
                  arrival_time[str(main_time)[:-3]][3], ' ', 'встал в очередь к автомату №', machine, sep='')
            for i in range(len(machine_with_max_quantity)):
                print('Автомат №', i + 1, ' ', ' максимальная очередь: ', machine_with_max_quantity[i+1],
                      ' Марки бензина: ', ', '.join(machine_with_petrol[i + 1]), ' ', ' -> ',
                      '*' * quantity_people_near_machine[i+1], sep='')

            amount_of_petrol[arrival_time[str(main_time)[:-3]][1]] += int(arrival_time[str(main_time)[:-3]][2])

    main_time += datetime.timedelta(hours=0, minutes=1)

print()
sum_petrols = 0
for i in amount_of_petrol:
    print('Бензина по марке', i, 'продано', amount_of_petrol[i], 'л')
    sum_petrols += amount_of_petrol[i] * price[i]
print()
print('Общая сумма продаж за сутки равна', sum_petrols, 'руб.')
print()
print('Количество клиентов, которые покинули АЗС не заправив автомобиль из-за «скопившейся» очереди:',
      the_number_of_cars_left)