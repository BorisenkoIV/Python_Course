# Вводятся числа, пока не введут 0. Найти произведение чисел, оканчивающихся на 4.
# (найти произведение, множители которых оканчиваются на 4)

mult = 1  # если ищем сумму или количество, то == 0.
number = int(input('Введите числа:\n'))
# Инпритатор понимает: все, что находится на табуляцию правее - находится внутри # цикла!!!
while number != 0:
	if number % 10 == 4:	# остаток деления == 4
		n1=mult     # временно храним 1-е число
		n2=number   # временно храним 2-е число
		mult *= number # при умножении "mult" не может быть нулем!
	number = int(input()) # здесь "number" не принадлежит условию if и
			              # мы всегда можем ввести следующее число...
# if mult == 1:	# проверка, если ввели 0 !
# 	mult = 0
#print (mult)
print (f'Числа: {n1} и {n2},  произведение: {mult}')
