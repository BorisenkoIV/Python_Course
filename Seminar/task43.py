'''
Задача № 43
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Вводится список чисел. Все числа списка находятся на разных строках.
Ввод:  1 2 3 2 3    Вывод: 2
'''

# a = [int(s) for s in input().split()]
a=[1, 2, 3, 2, 3]
count = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            count += 1
print(count)

## Вариант 2 (встренный метод):
# print(sum(a.count(x) - 1 for x in a) // 2)