'====================================файлы====================================='
# файл это информация или программа, имеющая имя, размер, данные внутри и расширение,
# которое хранит информацию в долговременное памяти компьютера как единое целое
# МОДУЛЬ - это любой файл который имеет расширение . py
# ПАКЕТ - это папка с набором модулей (в папке обязательно должен быть файл___intin__.py)

'===================================работа с файлами==========================='
# open - функция, которая открывает файл в определенном режиме
# 1. Пути к файлу
# 2. Режим работы
"""
режимы:
'r' - read(только для чтения)
'w' - write (только для записи, каждый раз очищает файл)
'a' - append (только для добавления записи, добавляет в конец)
'x' - создает файл, но если он уже существует, выдаст ошибку
'b' - binary (открывает файл в бинарном виде)
"""
'======================================Read======================================'
# file = open('lesson 14 (files - файл)/test.txt', 'r')
# print(dir(file))
# print(file)
# print(file.writable()) # метод проверяет можно ли что то записать в файл
# print(file.readable()) # метод проверяет можно ли прочитать файл
# print(file.read()) # метод который читает весь файл
# file.seek(0) #возвращает курсор в начало файла
# print(file.readline().upper()) # вывод только строку документа, возвращает тип данных str, можно использовать методы строк
# print(file.readline(5)) #выводит только 5 первых символа
# print(file.readline().replace('\n', ''))
# file.seek(0)
# print(file.tell()) #смотрит расположение курсора (начало = 0)
# file.read()
# print(file.tell())
# print(file.readlines()) #возвращает список с элементами строки


# file.close() # обязательно нужно закрыть, после открытия

'====================================Write======================================'
# file = open('lesson 14 (files - файл)/test2.txt', 'w')
# text = 'delai  do konca!!!'
# #перед тем как записать что то в файле он его полностью очищает
# # print(file.writable())
# # print(file.readable())
# file.writelines(['ada ',  'python ',  'django ']) #принимает только список со строками

# file.close()

'==================================Append======================================='
# file = open('lesson 14 (files - файл)/test3.txt', 'a')
# print(file.readable())
# print(file.writable())
# for i in range(1, 101):
#     file.write(f'порядковый номер {str(i)}\n')

# file.close()

'===============================Контекстный менеджер========================='
# Конструкция with работает с любыми обьектами у которых есть 2 метода:
# __enter__, __exit__.
# file = open('files/test.txt')
# print(dir(file))
# file.close()
# __enter__ срабатывает в начале конструкции with
# __exit__ срабатывает в конце, когда конструктор закончил работу или вышла ошибка в этой конструкции
# with open('lesson 14 (files - файл)/test2.txt', 'r') as file:
#     print(file.read())

# with open('lesson 14 (files - файл)/test2.txt', 'a') as a:
#     a.write(input('vvedite svoi login i parol') + '\n')

# with open ('lesson 14 (files - файл)/test2.txt', 'r') as file2:
#     content = file2.read()
#     if 'a' in content.lower():
#         print('da')
#     else:
#         print('netu')

'===================================JSON===================================='
# JavaScript Object Notation - Униваерсальный формат, вкотором мы можем хранить данные в типах данных
# понятных почти для всех языков программирования

import json 
# Десериализация - перевод с json строки в Python обьект
# loads - метод для десериализации с json строки 
# load - метод для десериализации с json файлами
# сериализация - это перевод python обьекта в json строку
# dumps - метод для сериализации в json строку
# dump - метод для сериализации в json файл
# with open('lesson 14 (files - файл)/test_js.json', 'w') as file:
#     json.dump({"Tilek": 25, "adilte": 25}, file)

# with open('lesson 14 (files - файл)/test_js.json') as file:
#     content = json.load(file)
#     print(content)
#     print(type(content))
#     for key, value in content.items():
#         print(type(key))
#         print(type(value))

# str_js = json.dumps({"Tilek": 25, "adilte": 25})
# content = json.loads(str_js)
# print(content)
# print(type(content))
# for key, value in content.items():
#     print(type(key))
#     print(type(value))
'===========================================CRUD==================================='
'CRUD - CREAT READ UPDATE DELETE'
def read_json(id=None):
    with open('/Users/IT/Desktop/ada3/lesson 14 (files - файл)/db.json') as file:
        text = json.load(file)
        if id == None:
            print(text)
        else:
            for i in text:
                if i['id'] == id:
                    print(i)
def create_json(id, title, description, price):
    with open('/Users/IT/Desktop/ada3/lesson 14 (files - файл)/db.json') as file:
        content = json.load(file)
    with open('/Users/IT/Desktop/ada3/lesson 14 (files - файл)/db.json', 'w+') as file2:
        content.append({"id": id, "title": title, "description": description, "price": price})
        json.dump(content, file2)


# create_json(1, 'iphone 13', 'smarphone', 1000)
# create_json(2, 'iphone 15', 'smarphone', 1500)
# read_json(2)