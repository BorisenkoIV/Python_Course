# print (round(1.4))  # = 1
# print (round(1.5))  # = 2
# print (round(2.4))  # = 2
# print (round(2.5))  # = 2
# print (round(2.6))  # = 3
# print (round(-2.4)) # = -2
# print (round(-3.6)) # = -4
""" Задача #1 """
""" Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод """
"""
num = int(input('Введите число: '))
copy_num = num
total = 0

if num < 0:
    num *= -1

for i in range(3):
    total += num % 10
    num = num // 10

print(f'Сумма цифр числа {copy_num} = {total}')
"""

""" Задача #2 """
"""
total = int(input('Сколько журавлей всего сделано?: '))
# Более костыльное решение
kate = 0
petya = 0
sergey = 0

flag = True

while flag == True:
    petya += 1
    sergey +=1
    kate = (petya+sergey)*2
    if kate + petya + sergey == total:
        flag = False
        break

print(f'Петя и Сергей сделали {petya+sergey}, Катя сделала {kate}.')

# Более симпотичное решение

total = int(input('Введите число, кратное 6: '))

k, s, p = 0, 0, 0

for i in range(1, total+1):

    if i%5 == 0 or i%6 == 0:
        s += 1
        p += 1
    else:
        k += 1

print(f'Катя - {k}, Петя - {p//2}, Сергей - {s//2}')

"""

""" Задача #3 """
"""
ticket_num = input('Введите номер билета: ')

left_num = int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2])
right_num = int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5])

if left_num == right_num:
    print('Поздравляю! Ваш билет счастливый!')
else:
    print('Увы! Ваш билет не счастливый.')
"""

""" Задача #4 """
"""
n = int(input('Ширина шоколадки, долек: '))
m = int(input('Длина шоколадки, долек: '))
k = int(input('Сколько долек вы хотите отломить: '))

if k == n * m:
    print('Вы съедите всю шоколадку.')
elif k > n * m:
    print('Превышен размер шоколадки.')
elif k <= 0:
    print('Вы ничего не отломили.')
elif k < n * m and (k % n == 0 or k % m == 0):
    print('Вы отломили шоколадку!')
else:
    print('Что то пошло не так.')
"""