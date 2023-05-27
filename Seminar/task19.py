'''
Задача № 19.
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
K – положительное число.
Input:  [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

'''

# # РЕШЕНИЕ 1:
# n = int(input('  Введите кол-во элементов: '))
# list_1 = []
# for _ in range(n):
#     list_1.append(int(input('  Введите значения: ')))
# print(list_1)

# k = int(input('  Введите число K: '))

# for i in range(k-1):
#     list_1.insert(0,list_1[-1])
#     list_1.pop(-1)
# print(list_1)

# # РЕШЕНИЕ 2:

# list_1 = list(map(int, input("  Введите список через пробел: ").split()))
# k = int(input('  Введите число сдвига K: '))
# # if k>0:
# #     print('К>0 - сдвиг ВПРАВО:')
# # else:
# #     print('К<0 - сдвиг ВЛЕВО:')
# for i in range(k-1):
#     list_1.insert(0,list_1[-1])
#     list_1.pop(-1)
# print(list_1)

# # РЕШЕНИЕ 3:
# # Метод циклического сдвига ВПРАВО - ВЛЕВО: 
# def shift(lst, steps): 
#     if steps < 0:
#         print('  К<0 - сдвиг ВЛЕВО:')
#         steps = abs(steps)
#         for i in range(steps):
#             lst.append(lst.pop(0))
#     else:
#         print('  К>0 - сдвиг ВПРАВО:')
#         for i in range(steps):
#             lst.insert(0, lst.pop())
 
# nums = list(map(int, input("  Введите список через пробел: ").split()))
# print(nums)
# k = int(input('  Введите число сдвига K: '))
# shift(nums, k)
# print(nums)

###################################################
# РЕШЕНИЕ 4: с обработкой ошибок при вводе чисел...
###################################################

# Метод циклического сдвига ВПРАВО - ВЛЕВО: 
def shift(lst, steps): 
    if steps < 0:
        print('  К<0 - сдвиг ВЛЕВО:')
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        print('  К>0 - сдвиг ВПРАВО:')
        for i in range(steps):
            lst.insert(0, lst.pop())
############################################ 
try:
    nums = list(map(int, input("  Введите список чисел через пробел: ").split()))
except ValueError:
    print("  Вы ошиблись при вводе списка чисел!")
    nums = list(map(int, input("  Введите еще раз - список чисел через пробел: ").split()))

print(nums)
# k = int(input('  Введите число сдвига K: '))
try:
    k = int(input('  Введите число сдвига K: '))
except ValueError:
    print("  Вы ввели не число!")
    k = int(input('  Введите число сдвига K: '))
shift(nums, k)
print(nums)
#################################################

