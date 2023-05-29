'''
Задача 27
Пользователь вводит текст(строка). Словом считается последовательность непробельных
символов идущих подряд, слова разделены одним или большим числом пробелов.
Определите, сколько различных слов содержится в этом тексте:
Input: She sells sea shells on the sea shore The shells that she sells are sea shells
I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea 
shore shells
Output: 19
'''

# # ВАРИАНТ 1:
# import re # Подключаем регулярные выражения
# a='''She sells sea shells on the sea shore The shells that she sells are sea shells
# I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea 
# shore shells.'''
# # a = '''She sells sea shells on the sea shore;
# # The shells that she sells are sea shells I'm sure.
# # So if she sells sea shells on the sea shore,
# # I'm sure that the shells are sea shore shells.'''
 
# print(len({x for x in re.findall(r'\w+', a)}))

# ВАРИАНТ 2:
some_dict = {}
word = input('  Введите слово:\n')
for letter in word:
    if letter not in some_dict:
        some_dict[letter] = 1
    else:
        some_dict[letter] += 1
print(some_dict)