'''
Задача № 17.
Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

'''
# ВАРИАНТ 1: 
'''
Метод split() делит введенную строку на список подстрок.
После этого map() выполняет функцию int() для каждого элемента списка.
Input: 1  1  2  0  -1  3  4  4
Output: [1, 2, 0, -1, 3, 4] - лист чисел!
Output:6
'''
# first = input("  Введите список через пробел: ").split()
first = list(map(int, input("  Введите список через пробел: ").split()))
second = []
for i in first:
    if i not in second:
        second.append(i)
print(second)
print(len(second))

# # ВАРИАНТ 2:
# '''
# Метод split() делит введенную строку на список подстрок.
# Можно вводит строковые значения разделенные пробелом
# Input: 1  1  2  0  -1  3  4  4
# Output: ['1', '2', '0', '-1', '3', '4'] - лист строк!
# Output: 6
# '''
# first = input("  Введите список через пробел: ").split()
# # first = list(map(int, input("  Введите список через пробел: ").split()))
# second = []
# for i in first:
#     if i not in second:
#         second.append(i)
# print(second)
# print(len(second))



# entered_list = input("  Введите список чисел, разделенных пробелом: ").split()
# print("  Введенный список:", entered_list)

# num_list = list(map(int, entered_list))
# print("Список чисел: ", num_list)
# print("Сумма списка:", sum(num_list))