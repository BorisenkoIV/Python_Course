'''
Задача № 51. 
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение 
некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов 
отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это 
функция, которая принимает объект и вычисляет его характеристику.
Ввод:                                                                             Вывод: same
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
print('same') 
else:
print('differen')

'''

## Сергей Романов 22:30 решение в зале:
def same_by(characteristic, objects):
    new_objects = list(filter(characteristic, objects))
    if len(objects) == len(new_objects) or len(new_objects) == 0:
        return True
    return False

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')