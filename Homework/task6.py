# Д.Задача № 6
# Оределить счастливый билет общественного транспорта по его номеру.
# (385916 -> yes; 123456 -> no)
print('  Задача № 6')
print('  Определить счастливый билет по номеру:')

print('Введите номер билета:\t')
s = [int(i) for i in input()]
if sum(s[:3]) == sum(s[3:]):
    print(f'Билет - счастливый')
else:
    print(f'Билет - несчастливый')