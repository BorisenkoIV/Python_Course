'''
Задача 28
Напишите рекурсивную функцию sum(a, b),возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
Input: 2> 2>   Output: 4
'''
## Проверка введенного числа:
try:
    a = int(input('  Введите натуральное число А: '))
except ValueError:
    print("  Вы ввели не число!")
    a = int(input('  Введите число А: '))
try:
    b = int(input('  Введите натуральное число А: '))
except ValueError:
    print("  Вы ввели не число!")
    b = int(input('  Введите число В: '))


def recursive_sum(a, b):
    if a == 0: # базовое условие рекурсии
        return b
    else:
        return recursive_sum (a - 1, b + 1) # рекурсивный вызов

print (f'Сумма А + В = {recursive_sum(a, b)}')


# def summa(a, b):
#     a += 1
#     b -= 1
#     if b > 0:
#         return summa(a, b)
#     else:
#         return a
 
# print (f'Сумма А + В = {summa(a, b)}')