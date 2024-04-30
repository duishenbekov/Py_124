'=====================Функция======================='
# Функция - это именованный блок кода, который вызывается множество раз в других частях программы
# Они создаются благодаря ключевому слову def
# При наименовании функции придерживаются стилю Snake_case

# def name_of_functions(a, b - параметры функции, их может быть сколько угодно):
    # <body> код, который имее некую логику
    # return оператор, который возращает результат выполнения функции

# def my_func():
#     a = 4
#     b = 5
#     print(a + b)
# print(my_func())

# list_numbers = [1,2,22,33,12,13,15,2,6,7]
# def find_even():
#     # for el in list_numbers:
#     #     if el %2 == 0:
#     #         print(f'четное число: {el}')
#     result = [f'четное число: {el}' for el in list_numbers if el %2 == 0]
#     return result

# print(find_even())
# print(name)


'''Всеми любимая программа «hello world». Создайте функцию с именем say_hello_world , которая принимает на вход имя человека в виде строки и печатает фразу «{name} говорит hello world!»
'''
# def say_hello_world():
#     print(f'{input("Введите ваше имя: ")} говорит hello world!')

# say_hello_world()

'''
Напишите функцию summa_n, которая принимает одно целое положительное t число и находит сумму всех чисел от 1 до t включительно. Программа должна распечатать сообщение

"Я знаю, что сумма чисел от 1 до {t} равна {S}", где в качестве t и S вам необходимо подставить значения '''
# def summa_n():
#     t = int(input())
#     # S = sum([i for i in range(1, t+1)])
#     # S = sum(list(range(1,t+1)))
#     # print(f"Я знаю, что сумма чисел от 1 до {t} равна {sum([i for i in range(1, t+1)])}")
#     spisok = []
#     for i in range(1, t+1):
#         spisok.append(i)
#     spisok2 = sum(spisok)
#     print(spisok2)
# summa_n()

'''
Напишите функцию exponentiation, которая принимает на вход целое число и выводит на экран через пробел квадрат и куб этого числа. '''
# def exponentiation():
#     num = int(input())
#     print(f'Квадрат чилса равен {num**2}\nКуб числа равен {num**3}')
# exponentiation()

'''
Напишите функцию sum_num для суммирования всех цифр строки.
Функция должна принимать строку, суммировать все ее символы, которые являются цифрами,
и в качестве ответа выводить найденную сумму.
123asdavd1sss5
12
'''
# def sum_num():
#     stroka = input()
#     spisok = []
#     for i in stroka:
#         if i.isdigit():
#             spisok.append(int(i))
#     print(sum(spisok))
    # result = sum([int(num) for num in stroka if num.isdigit()])
    # print(result)

# sum_num()
'================================Функции=================================='
'''Функция - это именованный блок кода, который вызывается множество раз в других частях программы
Они создаются благодаря ключевому слову def
При наименовании функции придерживаются стилю Snake_case
'''
# параметры функции - это переменые которые будут принимать наша функция, 
# для того чтоб мы смогли работать с данными которые попадают в нашу
# функцию через аругументы
# Аргументы функции - это данные которые мы передаем для параметров при вызове функции.
# return - это оператор, который нужен, чтобы функция возвращала результат(по умолчанию None)

# string = '1234abs'
# def our_len(stroka):
#     count = 0
#     for _ in stroka:
#         count +=1
#     return count
# print(our_len(string))
# print(our_len('123'))


'=================================Виды Аргументов============================='
# '1. Позиционные (по позиции)'
# '2. Именованные (по названию параметра - значение)
# '# def add(num1, num2):
# #     return num1 + num2
# print(add(1,2))
# print(add(num1=5, num2=6))
# print(add(num2=5, num1=6))
# print(add(6, num2=5))
'=================================виды параметров=============================='
# '1. Обязательные'
# '2 Необязательные'
#     # c дефолтным значением(с значением по умолчанию, которые передается при создании функции)
# 'необязательные'  # args (все позиционные аргументы, которые не попали в обязательные или с дефолтом)
# 'необязательные'  # kwargs (все лишние именованные параметры)

# def greet(*args):
#     print(type(args))
#     print(args)
#     for name in args:
#         print(f'privet{name}')
# greet('anton', 'rawid', 'belek', 'sultan')

# def my_greet(**kwargs):
#     name = kwargs.get('name')
#     age = kwargs.get('age')
#     print(f'privet {name}, tvoi vozrast {age}')
# my_greet(age=12, name='anton')

# dict_ = {'age': 1, 'name': 'tilek'}
# print(**dict_)

# чем же хороши функции?
'''
1. Помогают избегать повторения одинаковых фрагментов кода
2. Упрощают внесение изменений в повторяемых блоках кода
3. Позволяет разбить задачу на подзадачи

Функции соблюдают принцип DRY(don't repeat yourself)
'''
'============================Регистер, Логин с помощью функции===================='
# database = [
#     {'name': 'user1', 'password': 12345},
#     {'name': 'user2', 'password': 12345},
#     {'name': 'user3', 'password': 12345},
# ]

# def in_database(name):
#     for user in database:
#         if user["name"] == name:
#             return False
#     return False

# def register_datebase(name, password1, password2):
#     if in_database(name):
#         return 's takim imenem uje suwestvuet'
#     if password1 != password2:
#         return 'paroli sovpali'
#     user = {'name': name, 'password': password1}
#     database.append(user)
#     return 'vy uspewno zaregistrirovalis'

# def login_database(name, password):
#     if not in_database(name):
#         return 'polzovatel ne naiden'
#     for user in database:
#         if user['name'] == name:
#             if user['password'] != password:
#                 return 'parol ne verniy'
#             return 'vy uspewno vowli'

# def main():
#     print('dobor pojalovat')
#     while True:
#         action = input('vvedite chto to iz etogo ----> register: 1/nLOGIN\2\next:3')
#         if action == '3':
#             break
#         elif action == '1':
#             name = input('vvedite imya polzovatelya')
#             password1 = input('vedi parol')
#             password2 = input('vedi parol povtorno')
#             print(register_datebase(name, password1, password2))
#         elif action == '2':
#             name = input('vvedite imya polzovatelya')
#             password1 = input('vvedite parol')
#             print(login_database(name, password1))
#         else:
#             print('ne kotrektniy vybor')
# main()
# def count_letter(text, letter):
#     count = 0
#     for i in text:
#         if i == letter:
#             count +=1
#     print(count)
# count_letter('jefskaaaaafjsne', 'a')

# # count_letter('jefskaaaafjsne', 'a')
# # # print(dir(str))

# def count_letter(text, letter):
#     print(text.count(letter))
# count_letter('jefskaaaaaafjsne', 'a')

# def count_letter(text, letter):
#     count = ([1 for i in text if i == letter])
#     print(sum(count))
# count_letter('jefskaaaaafjsne', 'a')

# def print_fio(name, surname, patrnomic):
#     count = surname[0] + name[0] + patrnomic[0]
#     print(count)
# print_fio('aleksandr', 'puwkin', 'sergeevich')

# def print_digit_sum(number):
#     result = ([int(num) for num in str(number)])
#     print(result)

# print_digit_sum(12345)