# Задача № 5
# За день машина проезжает n километров. Сколько дней нужно,
# чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

print('  Задача № 5')
print('  Сколько дней нужно, чтобы проехать маршрут длиной m километров?\n')

n = int(input('Paсстояние за день:\t'))
m = int (input('Общее растояние:\t' ))
m = -m
res = -(m // n)
print('Нужно дней: ',res)