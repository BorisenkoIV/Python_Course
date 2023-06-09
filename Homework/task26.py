'''
Задача 26
Напишите программу, которая на вход принимаетдва числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵) 
A = 2; B = 3 -> 8

'''
print('Задача 26')
print('Возведение числа А в целую степень B:')
## Проверка введенного числа:
try:
    a = int(input('  Введите натуральное число А: '))
except ValueError:
    print("  Вы ввели не число!")
    a = int(input('  Введите число А: '))
try:
    b = int(input('  Введите степень В: '))
except ValueError:
    print("  Вы ввели не число!")
    b = int(input('  Введите степень В: '))


## Метод возведения в степень методом рекурсии:
def power(a, b):
    if (b == 1): # базовое условие рекурсии
        return (a)
    if (b != 1):
        return (a * power(a, b - 1)) # рекурсивный вызов
    
print("Результат возведения в степень равен: ", power(a, b))

