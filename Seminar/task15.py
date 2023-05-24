# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза.
print('  Задача № 15')
print('  Определить легкий и тяжелый арбуз:\n')

watermelons = int(input('Введите кол-во арбузов: '))

max_kg = int(input('Введите массу арбуза: '))
min_kg = max_kg
for _ in range(watermelons - 1):
    weight = int(input('Введите массу арбуза: '))
    if weight > max_kg:
        max_kg = weight
    else:
        if weight < min_kg:
            min_kg = weight
print(f'  Для себя любимого - {max_kg}, для любимой тещи - {min_kg}')