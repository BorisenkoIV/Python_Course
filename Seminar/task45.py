
'''
Задача № 45
Два  различных  натуральных  числа n  и m  называются дружественными,  если  сумма  делителей  числа n 
(включая  1,  но  исключая  само n)  равна  числу m  и наоборот. Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа 
получает  на  вход  одно  натуральное  число k,  не превосходящее  10в5.  Программа  должна  вывести    все 
пары  дружественных  чисел,  каждое  из  которых  не превосходит k. Пары необходимо выводить по одной в 
строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую 
пару не дает).
Ввод: 300        Вывод: 220 и 284
'''


### ВАРИАНТ 2 (от преподавателя):
### Сергей Сердюк 23:33
n = int(input())
list_1 = list()
for i in range(n):
    summa = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summa += j
    list_1.append(tuple([i, summa]))
print(i, summa)
### 5 и 15

### ВАРИАНТ 1 (мое решение):
# def getSum(value):
#     res = 1
#     for i in range(2, int(value**0.5) + 1):
#         if value % i == 0:
#             res += i + value // i
#     return res
# #for i in range(10, 10000):
# for i in range(200, 300):
#     sum1 = getSum(i)
#     sum2 = getSum(sum1)
#     if sum2 == i and sum1 != sum2:
#         print(i, sum1)

