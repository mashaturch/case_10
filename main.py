"""Case-study #10 Refueling analysis
Developers:
Турчинович М. (90%), Зубарева Т. (40%) , Костылев М. (39%)
"""


import ru_local
import math
import random
import datetime



file = open('input.txt', encoding='utf-8')
azs = open('azs.txt', encoding='utf-8')

price = {ru_local.a80: 32, ru_local.a92: 46, ru_local.a95: 49, ru_local.a98: 59} #petrol prices
petrol_with_machine = {} #dictionary petrol and petstop number
machine_with_petrol = {} #dictionary petstop number and petrols
machine_with_max_quantity = {} #dictionary petstop number and max queue
departure_time = {} #dictionary with time of leaving
arrival_time = {} #dictionary with time of arriving
quantity_people_near_machine = {} #dicitionary with people at petrol right now
cars_near_the_machine = {} #time of arrining + petrol number
the_number_of_cars_left = 0
amount_of_petrol = {}

for line in azs:

    data_input = list(line.split())

    machine = data_input[0]
    max_quantity = data_input[1]
    petrols = list(data_input[2:])
    for petrol in petrols:  #makes the dictionary with petrol and petstops
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

    machine_with_max_quantity[int(machine)] = int(max_quantity) #makes the dictionary with petstop number and max queue
    quantity_people_near_machine[int(machine)] = 0 #makes the dictionary with petstop number and number of people now


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
        print(ru_local.ins, str(main_time)[:-3], ru_local.client, departure_time[str(main_time)[:-3]][0],
              departure_time[str(main_time)[:-3]][1], departure_time[str(main_time)[:-3]][2],
              departure_time[str(main_time)[:-3]][3], ru_local.leave)
        for i in range(len(machine_with_max_quantity)):
            print(ru_local.leave, i + 1, ' ', ru_local.max_qu, machine_with_max_quantity[i + 1],
                  ru_local.st_oil, ', '.join(machine_with_petrol[i + 1]), ' ', ' -> ',
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
                if quantity_machine > quantity_people_near_machine[petrol_with_machine[arrival_time[str(main_time)\
                        [:-3]][1]][i]]:
                    machine = petrol_with_machine[arrival_time[str(main_time)[:-3]][1]][i]
                    quantity_machine = quantity_people_near_machine[petrol_with_machine[arrival_time[str(main_time)\
                        [:-3]][1]][i]]

            i += 1

        if machine == 0:
            print(ru_local.ins, str(main_time)[:-3], ru_local.new_cl, arrival_time[str(main_time)[:-3]][0],
                  arrival_time[str(main_time)[:-3]][1], arrival_time[str(main_time)[:-3]][2],
                  arrival_time[str(main_time)[:-3]][3], ru_local.cant)
            for i in range(len(machine_with_max_quantity)):
                print(ru_local.aut, i + 1, ' ', ru_local.max_qu, machine_with_max_quantity[i + 1],
                      ru_local.st_oil, ', '.join(machine_with_petrol[i + 1]), ' ', ' -> ',
                      '*' * quantity_people_near_machine[i + 1], sep='')
            the_number_of_cars_left += 1


        else:
            cars_near_the_machine[str(main_time)[:-3]] = machine
            quantity_people_near_machine[machine] += 1

            if str(main_time + datetime.timedelta(hours=0, minutes=(arrival_time[str(main_time)[:-3]][3])))[:-3] \
                    not in departure_time:
                departure_time[str(main_time + datetime.timedelta(hours=0,minutes=(arrival_time[str(main_time)\
                    [:-3]][3])))[:-3]] = arrival_time[str(main_time)[:-3]]
            else:
                departure_time[str(main_time + datetime.timedelta(hours=0, minutes=(arrival_time[str(main_time)\
                    [:-3]][3])))[:-3]].append(arrival_time[str(main_time)[:-3]])

            print('В ', str(main_time)[:-3], ' ', ru_local.new_cl, arrival_time[str(main_time)[:-3]][0], ' ',
                  arrival_time[str(main_time)[:-3]][1], ' ', arrival_time[str(main_time)[:-3]][2], ' ',
                  arrival_time[str(main_time)[:-3]][3], ' ', ru_local.get, machine, sep='')
            for i in range(len(machine_with_max_quantity)):
                print(ru_local.aut, i + 1, ' ', ru_local.max_qu, machine_with_max_quantity[i+1],
                      ru_local.st_oil, ', '.join(machine_with_petrol[i + 1]), ' ', ' -> ',
                      '*' * quantity_people_near_machine[i+1], sep='')

            amount_of_petrol[arrival_time[str(main_time)[:-3]][1]] += int(arrival_time[str(main_time)[:-3]][2])

    main_time += datetime.timedelta(hours=0, minutes=1)

print()
sum_petrols = 0
for i in amount_of_petrol:
    print(ru_local.oil_st, i, ru_local.sell, amount_of_petrol[i], ru_local.litr)
    sum_petrols += amount_of_petrol[i] * price[i]
print()
print(ru_local.total_rate, sum_petrols, ru_local.price)
print()
print(ru_local.numb_cl,
      the_number_of_cars_left)