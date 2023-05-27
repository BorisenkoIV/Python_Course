'''
Задача 18
Требуется найти в списке N самый близкий по величине элемент к заданному числу А.
Пользователь в первой строке вводит натуральное число n – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
Input: 5 (1 2 3 4 5) 6 Output: 5

'''
print('Задача № 18')
print('Найти в списке чисел ближайший по величине к А элемент:')

# Проверка на исключения при вводе чисел:
try:
    num_list = list(map(int, input("  Введите список чисел через пробел: ").split()))
except ValueError:
    print("  Вы ошиблись при вводе списка чисел!")
    num_list = list(map(int, input("  Введите еще раз - список чисел через пробел: ").split()))

print('Исходный список: ',num_list)
try:
    A = int(input('  Введите число А: '))
except ValueError:
    print("  Вы ввели не число!")
    A = int(input('  Введите число А: '))

# ВАРИАНТ 1:
# ###########################################################
# # Поиск в списке ближайшего по величине к А элемента:
# raz_min=0 # Минимальная разность между А и элементом списка
# for i in range(len(num_list)):
#     # raz_min=()
#     if (A-num_list[i])<(A-raz_min) and (A-num_list[i])>0:
#         num=i
# print(f'Ближайший по величине элемент: {num_list[num]}')
# ###########################################################


# ВАРИАНТ 2:
# Поиск в списке ближайшего по величине к А элемента:
k=num_list[0]
for i in range(len(num_list)):
    if abs(num_list[i]-A)<abs(k-A) or abs(num_list[i]-A)==abs(k-A) and num_list[i]<k:
        k=num_list[i]
print(f'Ближайший по величине элемент: {k}')


# # ВАРИАНТ 3:
# N = int(input('Кол. чисел:'))
# a=[int(input('Ввести число:')) for i in range(N)]
# x=int(input('Заданное число:'))
# b=[abs(a[i]-x) for i in range(len(a))]
# print(a[b.index(min(b))])


# # ВАРИАНТ 4: 
# from random import randint 
# n = 10
# z = [randint(1,100) for i in range(n)]
# print(z)
  
# num = int(input('Введите число,которое хотите вывести: '))
# if num in z:
#     print(num)
    
# else:
#     z.append(num)
#     z.sort()
#     index_num = z.index(num)
#     len_z = len(z) - 1
#     print(z)
#     if index_num == 0:
#         print(z[1])
#     elif index_num == len_z:
#         print(z[len_z-1])
#     else:
#         left_num = z[index_num - 1]
#         right_num = z[index_num + 1]
#         if (num - left_num) < (right_num - num):
#             print(left_num)
#         else:
#             print(right_num)
