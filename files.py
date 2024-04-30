# '=========================Файлы==================================='
# # Файл - это данные или программа, имеющая имя, размер, данные внутри и расширение, которое хранит информацию в долговременной памяти компьютера как единое целое

# # Модуль - это любой файл который имеет расширение .py
# # Пакет - это папка с набором модулей (в папке обязательно должен быть файл __init__.py )

# '=========================Работа с файлами=========================='
# # open - функция, которая открывает файл в определенном режиме
# # 1. Путь к файлу
# # 2. Режим работы

# '''
# Режимы:
# 'r' - read (только для чтения)
# 'w' - write (только для записи, каждый раз очищает файл)
# 'a' - append (только для добавления записи, добавляет в конец)
# 'x' - создает файл, но если он уже существует, выдаст ошибку
# 'b' - binary (открывает файл в бинарном виде)
# '''

# '===========================Read==============================='
# file = open('files/test.txt', 'r')
# # print(dir(file))
# # print(file)

# print(file.writable()) # метод проверяет можно ли что то записать в файл
# print(file.readable()) # метод проверяет можно ли прочитать файл

# print(file.read()) # метод читает весь файл
# file.seek(0) # возращает курсор в начало файла
# # print(file.readline().upper()) # выводит только строку документа, возращает тип данных str, можно использовать методы строк
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())

# print(file.readline(5)) # выводит только 5 первых символа
# print(file.readline().replace('\n', ''))
# file.seek(0)

# print(file.readlines()) # возращает список с элементами строки

# file.seek(0)
# print(file.tell()) # смотрит расположение курсора (начало = 0)
# file.read()
# print(file.tell())
# file.seek(20)
# print(file.readline().replace('\n', ''))

# file.close() # нужен после открытия, open обязательно нужно закрыть файл


# '=======================Write============================'
# # file = open('files/test2.txt', 'w')
# #перед тем как записать что то в файл он его полностью очищает

# # print(file.writable())
# # print(file.readable())

# # text = input("Введите ваше имя и возраст")

# # file.write(text)
# # file.writelines(['ada ', 'python ', 'django'])
# # принимает только список со строками

# # file.close()

# '=======================Append=========================='
# # file = open('files/test3.txt', 'a')
# # print(file.readable())
# # print(file.writable())
# # for i in range(1, 101):
# #     file.write(f'Порядковый номер : {str(i)}\n')

# # file.close()

# '=====================Контекстный менеджер====================='
# # Конструкция with работает с любыми обьектами у которых есть 2 метода: __enter__, __exit__.
# # __enter__ срабатывает в начале конструкции with
# # __exit__ срабатывает в конце, когда конструктор закончил работу или вышла ошибка в этой консрукции

# with open('files/test2.txt', 'r') as file:
#     print(file.read())

# with open('files/users.txt', 'a') as a:
#     a.write(input('Введите свой логин и пароль: ')+'\n')

# with open('files/test.txt') as file:
#     content = file.read()
#     if 'w' in content.lower():
#         print('Да в тексте есть буква w')
#     else:
#         print('нету')


'===========================JSON================================'
# JavaScript Object Notation - универсальный формат, в котором мы можем хранить данные в типах данных, понятных почти для всех языков программирования

import json
# Десериализация - перевод с json строки в python обьект
# loads - метод для десериализации c json строки
# load - метод для десериализации c json файла

# Сериализация - перевод python обьекта в json строку
# dumps - метод для сериализации в json строку
# dump - метод для сериацлизации в json файл

# with open('files/test_js.json', 'w') as file:
#     json.dump({'anton': 25, 'adilet': 15}, file)

# with open('files/test_js.json') as file:
#     content = json.load(file)
#     print(content)
#     print(type(content))
#     for key, value in content.items():
#         print(type(key))
#         print(type(value))

# str_js = json.dumps({"anton": 25, "adilet": "15"})
# content = json.loads(str_js)
# print(content)
# print(type(content))
# for key, value in content.items():
#     print(type(key))
#     print(type(value))

'--------------------------CRUD------------------------'
# CRUD - CREATE READ UPDATE DELETE

def read_json(id=None):
    with open('files/db.json') as file:
        text = json.load(file)
        if id == None:
            print(text)
        else:
            for i in text:
                if i['id'] == id:
                    print(i)

def create_json(id, title, description, price):
    with open('files/db.json') as file:
        content = json.load(file)
    with open('files/db.json', 'w+') as file2:
        content.append({'id':id, 'title': title, 'description': description, 'price': price})
        json.dump(content, file2)

# create_json(1, 'iphone13', 'smartphone', 1000)
# create_json(2, 'iphone15', 'smartphone', 1500)
# create_json(3, 'samsung', 'smartphone', 700)
# read_json()


# 2)Создайте файл users.txt. Напишите программу которая спрашивает у пользователя его Логин и Пароль и записывает в файл users.txt.
# with open('Files/users.txt', 'w') as users:
#     users.write(input('Введите свой логин и пароль:') + '\n')

# def add_user():
#     with open('Files/users.txt', 'r') as f:
#             database = f.read()
#             database = database.split('\n')
#             print(database)
#     with open('Files/users.txt', 'w') as users:
#         id = input('Введите имя:')
#         parol = input('Введите пароль')
#         for user in database:
#             if id in user:
#                 print('Такой юзер уже существует')
#                 users.write('\n'.join(database))
#                 return
#         database.append(f'{id} {parol}')
#         users.write('\n'.join(database))
#         print(database)
# add_user()

# 4) Создайте текстовый файл python.txt и запишите в него
# текст #1 из github: Затем, считайте его. Найдите слова
# которые содержат букву  "o" и запишите в список
# o_words=[] и   выведите на экран все полученные слова.

# текст 1
text = """
Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
"""

# with open('files/python.txt', 'w') as file:
#     file.write(text)

# with open('files/python.txt') as file:
#     text = file.read()
#     words = text.split()
#     print(words)
#     o_words = [word.strip('.,') for word in words if 'o' in word]
#     print(o_words)
#     print(len(o_words))

# text = '''.detacilpmoc naht retteb si xelpmoC
# .xelpmoc naht retteb si elpmiS
# .ticilpmi naht retteb si ticilpxE
# .ylgu naht retteb si lufituaeB
# '''

# with open('files/test2.txt') as file:
#     lines = file.readlines()
#     reverse_text = [i[::-1].replace('\n', '') for i in lines]
#     result = '\n'.join(reverse_text)
#     with open('files/test2.txt', 'w') as f:
#         f.write(result)
text = """123
aaa456
fxdya 5 0 0
"""
# with open('files/test3.txt', 'w') as f:
#         f.write(text)
with open('files/test3.txt', 'r') as f:
    lines = f.readlines()
    # spisok = []
    # for line in lines:
    #     stroka = ''
    #     for number in line:
    #         if number.isdigit():
    #             stroka += number
    #     spisok.append(int(stroka))
    print(sum([int(''.join([simvol for simvol in line if simvol.isdigit()])) for line in lines]))
