
'''
Задача 31 (метод РЕКУРСИИ)
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ...,
где a(0) = 0, a(1) = 1, a(k) = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7 Output: 21

'''
import time

# 	#ЗАДАЧА Фибонначи (рекурсия)
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(7))


	##ЗАДАЧА 31 Фибонначи (на циклах, работает очень быстро!)

def fib_better(n):
    if n == 1:
        return 0
    if n == 1:
        return 1
    first = 0
    second = 1
    third = first + second
    count = 2
    while count < n:
        first = second
        second = third
        third = first + second
        count += 1
    return third

#print(fib_better(6))
start = time.perf_counter()
print(fib_better(8))
end = time.perf_counter()
duration = end - start
print(duration)


