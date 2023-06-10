'''
СЕМИНАР 7
Теория и Решение задач
'''


# Александр LyraX 21:17
# # def sq1(x):
# #     print(x ** 2)
# #
# #
# # print(sq1(10))
# #
# # def sq2(x):
# #     return x ** 2
# #
# #
# # print(sq2(20))

# # def c(x):
# #     return x ** 3
# #
# #
# # some_list = [1, 2, 3, 4, 5]
# #
# # new_list = []
# #
# # for el in some_list:
# #     new_list.append(c(el))
# #
# # print(new_list)

# def c(x):
#     return x ** 3


# some_list = [1, 2, 3, 4, 5]
# new_list = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, some_list))
# print(new_list)


# Александр LyraX 21:24
# def even(a):
#     return a % 2 == 0


# some_list = [1, 2, 3, 4, 5]

# new_list = list(filter(lambda a: a % 2 == 0, some_list))
# print(new_list)

# Александр LyraX 21:24
# def even(a):
#     return a % 2 == 0


# some_list = [1, 2, 3, 4, 5]

# new_list = list(filter(lambda a: a % 2 == 0, some_list))
# print(new_list)


# Александр LyraX 21:35
# # import random
# #
# # some_list = []
# # for _ in range(100):  # 0, 1, 2, 3, 4, 5, 6, 7... 99
# #     number = random.randint(1, 10)
# #     if number % 2 == 0:
# #         some_list.append(number)
# #
# #
# # some_list = [random.randint(1, 10) for _ in range(100)]
# #
# # some_list = [int(input()) for _ in range(int(input()))]


# Сергей Романов 22:08
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def s(x):
#     if x[0] == x[1]:
#         return 0
#     return x[0] * x[1]

# mult = list(map(s, orbits))
# print(mult)
# maxx = mult.index(max(mult))
# print(orbits[maxx])


# Edgar Akopyan 22:12--???
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(max(orbits, key=lambda x: x[0]*x[1] if x[0] != x[1] else 0))     подглядел в сети такое решение
# sergeykostiv  кому  Все 22:12
# Все мой мозг ушел
# Александр LyraX 22:14
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# print(list(filter(lambda y: y[0] * y[1] == max(list(map(lambda x: x[0] * x[1] if x[0] != x[1] else 0, orbits))), orbits))[0])

#      ЗАДАЧА 51
# Сергей Романов 22:30
# def same_by(characteristic, objects):
#     new_objects = list(filter(characteristic, objects))
#     if len(objects) == len(new_objects) or len(new_objects) == 0:
#         return True
#     return False

# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')


# sergeykostiv  кому  Все 22:31
# def same_by(characteristic, objects):
#     new_objects = list(filter(characteristic, objects))
#     if len(objects) == len(new_objects) or len(new_objects) == 0:
#         return True
#     return False

# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
# Сергей Романов 22:31
# def same_by(characteristic, objects):
#     new_objects = list(filter(characteristic, objects))
#     if len(objects) == len(new_objects) or len(new_objects) == 0:
#         return True
#     return False
    

# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# к ЗАДАЧЕ 34 ДЗ
# Александр LyraX 22:45
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     print(operation, num_rows, num_columns)


# print_operation_table(lambda x: x, 7, 10)



