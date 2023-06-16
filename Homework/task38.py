'''
Задача 38
Создать телефонный справочник возможностью добавления записей и чтения.
Пользователь также может ввести фамилию, тогда программа должны вывести 
на экран все записи с этой фамилий. Также пользователь может добавлять
новых людей в справочник в режиме - импорт из файла.
'''

### 1 - Ввод данных нового контакта:
def new_contacts():
    surname = input(' Введите фамилию (с заглавной буквы): ')
    name = input(' Введите имя (с заглавной буквы): ')
    patronymic = input(' Введите отчество (с заглавной буквы): ')
    phone = input(' Введите телефон (начиная с 8-ки): ')
    return surname, name, patronymic, phone

### 1 - Создать контакт:
def creating():
    user = ' '.join(new_contacts())
    # file = 'test.txt'
    with open(file, 'a', encoding='utf-8') as data:
        # data.write('\n')
        data.write(f'{user}\n')

### 2 - Найти контакт:
def search_contact(phonebook):
    with open(phonebook,'r', encoding='utf-8') as f: # открываем файл на чтение
        x=(f.read()).split('\n') # читаем, разбиваем текст на строки по символу переноса строки (\п)
        # print(f'{x}\n')
        seach_msg=input(' Введите данные клиента ФИО (с заглавной буквы), телефон (начиная с 8-ки):\n')
        seach=False
    for n in x: # пробегаемся по тексту
        if n!= '': # пропускаем пустые строки
            n=n.split(' ') # разбиваем подстроки по символу 'пробел'
            if seach_msg==n[0] or seach_msg==n[1] or seach_msg==n[2] or seach_msg==n[3]:
                print(f'{n[0]} {n[1]} {n[2]} {n[3]}')
                seach=True
    if seach==False:
        print('Клиента с такими данными нет в списке!')

# ### 3 - Удалить контакт:
# def delete_contact(file_name):
#     with open(file_name, 'w+', encoding='utf-8') as file:


### 4 - Вывести все контакты в консоль:
def print_contacts():
    with open(file, 'r', encoding='utf-8') as data:
        text = data.read()
        print(text)

### 5 - Добавить (импортировать) контакты из файла:
def import_data(file_to_add, phonebook):
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_contacts: 
            with open(phonebook, 'a', encoding='utf-8') as file:
                contacts_to_add = new_contacts.readlines()
                file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'Файл: {file_to_add} не найден!')

### ОСНОВНОЕ МЕНЮ РАБОТЫ с АДРЕСНОЙ КНИГОЙ:
def action(phonebook):
    while True:
        try:
            mode = int (input ('\nВведите режим:\n 1 - добавить контакт\n 2 - найти контакт(ы)\n 4 - вывести все контакты\n 5 - импорт контактов\n 0 - завершить\n'))
        except ValueError:
            print('  Вы ввели не число!\n')
            mode = int (input ('Введите режим:\n 1 - добавить контакт\n 2 - найти контакт(ы)\n 4 - вывести все контакты\n 5 - импорт контактов\n 0 - завершить\n'))
        if mode == 1:
            creating()
        elif mode == 2:
                search_contact(phonebook)
        # elif mode == 3:
        #     delete_contacts()
        elif mode == 4:
            print_contacts()
        elif mode == 5:
            file_to_add = input('Введите название импортируемого файла: ')
            import_data(file_to_add, phonebook)
        elif mode == 0:
            break
        else:
            print('Некорректный режим')
        continue

file = 'test_book.txt'
action(file)
    # text = file.read().splitlines()
    # print(text)