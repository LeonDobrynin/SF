
weight = 77
sum_weight = 0
people_count = 0

while sum_weight <= 400:
    sum_weight += weight
    people_count += 1
else:
    print('Перевес', sum_weight-400, 'кг')