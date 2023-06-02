'''
Задача 24hard
Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте. НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ МЕТОД SPLIT
'''
some_str ='''She sells sea shells on the sea shore The shells that she sells are sea shells
I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea 
shore shells.'''

## ВАРИАНТ 1 без split:
# words = ""
# word_set = str(input("Введите текст: "))
# first_letter = word_set [0]
# word_set =set()
# for i in range(len(word_set)):
#     if word_set[i] not in " ?!:;,.": # символы:"пробел?!:;,." не содержатся в (not in)... 
#         words = words + word_set[i]
#     else:
#         word_set.add(words)
#         words = ""
# print(word_set)  # вывод результирующего множества
# print(len(set(word_set)))# вывод кол-ва эл-ов множества

## ВАРИАНТ 2 с split:
# some_str = input() # вводим текстовую строку
some_list = some_str.split() # создаем список из текстовой строки
some_set = set() # создаем пустое множество
for word in some_list: # проходим по словам и удаляем знаки препинания
    # проверяем, чтобы "word" состояло только из букв (метод: isalpha)
    if not word[-1].isalpha(): # проверяем - последний символ [-1] в "word" не знак препинания 
        word = word[:-1] # срезаем знак препинания в "word" и перезаписываем
    some_set.add(word) # добавляем "word" в множество
print(some_set)  # выводи полученное ммножество  
print(len(some_set)) # выводим количество неповторяющихся слов в тексте