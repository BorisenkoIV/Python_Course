'''
Задача № 23
Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество 
элементов массива, больших предыдущего (элемента с предыдущим номером) 
Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

'''
# ВАРИАНТ 1:
# nums = int(input("Введите кол-во элементов: "))
# some_list = []
# for _ in range(nums):
#     some_list.append(int(input()))
# print("Исходный список: ", some_list)
# count=0

# for i in range(0, len(some_list)-1):
#     if some_list[i] < some_list[i + 1]:
#          count += 1
# print(count)

# ВАРИАНТ 2:
try:
    some_list = list(map(int, input("  Введите список чисел через пробел: ").split()))
except ValueError:
    print("  Вы ошиблись при вводе списка чисел!")
    some_list = list(map(int, input("  Введите еще раз - список чисел через пробел: ").split()))
print("Исходный список: ", some_list)

count=0
for i in range(0, len(some_list)-1):
    if some_list[i] < some_list[i + 1]:
         count += 1
print('Кол-во элементов массива, больших предыдущего: ',count)