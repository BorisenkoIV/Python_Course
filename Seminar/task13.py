# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50.

print('  Задача № 13')
print('  Определить какой сезон :\n')

num_day = int(input('Введите колличество дней: '))

max_count = 0
old_temperature = 0
temp_count = 0

for _ in range(num_day):
    temperature = int(input('Введите температуру: '))
    if temperature >= 0:
        temp_count += 1
    else:
        if temp_count > max_count:
            max_count = temp_count
        temp_count = 0
    if temp_count > max_count:
        max_count = temp_count
print(max_count)
