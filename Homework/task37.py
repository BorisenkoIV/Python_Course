
'''
Задача 37
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и
использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4 Output: 4 3

РЕШЕНИЕ:
1-вводим строку и записывается в отдельную переменную.
2-переменную передаем в качестве аргумента в рекурсивную функцию
3-качестве базового условия рекурсии принимаем равенство длины строки нулю
  (в этом случае возвращается нулевая строка и функция завершает свою работу)
4-рекурсивно вызываем эту же функцию, но без первого символа, и просто прибавляем к ней этот символ.
  (в результате накапливается эта же строка, но в обратном порядке)
5-выводим результат на экран

'''
### ВАРИАНТ 1 (мое решение):
# print('Задача 37')
# print('Провести инверсию натурального числа N:')
# N = str(input('  Введите натуральное число N: '))

# # Метод инверсии строки 
# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
    
# print(N)
# print(reverse(N))


### ВАРИАНТ 2 (от преподавателя)
### Сергей Сердюк 22:22
def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n - 1) + f' {k}'

n = int(input())
print(f(n))