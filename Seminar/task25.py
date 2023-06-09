'''
Задача 25
Напишите  программу,  которая  принимает  на  вход строку, и отслеживает,
сколько раз каждый символ уже встречался. Количество повторов добавляется
к символам с помощью постфикса формата _n
Для решения данной задачи используйте функцию .split()
Input: a a a b c a a d c d d  Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
'''
# # РЕШЕНИЕ 1
# str = input('  Введите строку символов, разделенных пробелом:\n').split()
# result = {}
# print('  Результат:')
# for i in str:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1

# РЕШЕНИЕ 2 (семинар)
some_dict = {}
word = input()
for letter in word:
    if letter not in some_dict:
        some_dict[letter] = 1
    else:
        some_dict[letter] += 1
print(some_dict)
