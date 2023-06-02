'''
Задача 22
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
Input: 11  6 > 2 4 6 8 10 12 10 8 6 4 2 > 3 6 9 12 15 18
Output: 6  12

'''

## ЗАДАЧА 22 (вариант 1):
print('Задача № 22')
#print('Найти пересечение множеств А и В:')
print('Операции над множествами А и В:')

# Проверка на исключения при вводе чисел:
try:
    num_setA = set(map(int, input("  Введите множество чисел А, через пробел: ").split()))
except ValueError:
    print("  Вы ошиблись при вводе чисел множества!")
    num_setA = set(map(int, input("  Введите еще раз - множество чисел через пробел: ").split()))
try:
    num_setB = set(map(int, input("  Введите множество чисел В через пробел: ").split()))
except ValueError:
    print("  Вы ошиблись при вводе чисел множества!")
    num_setB = set(map(int, input("  Введите еще раз - множество чисел через пробел: ").split()))
print('Множество А: ',num_setA)
print('Множество В: ',num_setB)
num_setC = num_setA.intersection(num_setB)
print('  Пересечение множеств А и В: ',num_setC)
num_setC = num_setA.union(num_setB)
print('  Обьединение множеств А и В: ',num_setC)
num_setC = num_setA.difference(num_setB)
print('  Вычитание множества В из А: ',num_setC)

## ЗАДАЧА 22 (идеальное решение):
# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')
