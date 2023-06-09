'''
Задача 32
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''
import random

print('Задача 32')
print('Определить индексы элементов в массиве, не меньше заданного минимума и не больше заданного максимума:')

count = int(input('  Введите кол-во чисел в массиве: '))
maxi = int(input('  Введите максимальное значение в диапазоне 1-99: '))
mini = int(input('  Введите минимальное  значение в диапазоне 1-99: '))
list_1 = []
list_2 = []
for _ in range(count):
    number = random.randint(1, 99)
    list_1.append(number)
print(f'  Исходный массив:\n{list_1}')

### ВАРИАНТ 1:
# for i in range(len(list_1)):
#     if list_1[i] >= mini and list_1[i] <= maxi:
#         list_2.append(i)
# print(f'  Искомые индексы в массиве:\n{list_2}')

### ВАРИАНТ 2 (короткая запись):
print('  Искомые индексы в массиве:')
for i in range(len(list_1)):
    if mini <= list_1[i] <= maxi:
        print(i, end=' ')

# ### ВАРИАНТ (идеальное решение)
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
# print(i)