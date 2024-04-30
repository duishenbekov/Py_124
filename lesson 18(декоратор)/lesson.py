'================================Декоратор============================='
# Декоратор это функция высшего порядка, 
# которая нужна чтобы расширять функционал другой функции не изменяя ее(функция обвертка)
# Функция высшего порядка - эта та функция которая принимает в аргументы другую функцию, создает внутри себя функцию
# и вызвывает функцию и возвращает функцию

# def my_func(name):
#     print(f'Hello{name}')

# my_func('ada')

# def new_funcc(func):
#     print('ya funkciya kotoraya prinimaet druguyu funkciyu')
#     func('python')
#     print('konec funkcii')

# new_funcc(my_func)


# def decorator(func):
#     def wrapper():
#         print("ya kod do vyzova funkcii")
#         func()
#         print('ya - kod, posle vyzova funkcii')
#     return wrapper

# def hello():
#     print('Hello word')

#decorator(hello)() # первый способ вызова декоратора


# hello_ = decorator(hello) # второй способ вызова декоратора
# hello_()

# @decorator # третий способ вызова декоратора
# hello()

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(res * 2)
#     return wrapper
# @decorator
# def my_func(name):
#     return f'hello {name}'
# @decorator
# def sum_num(a,b):
#     return a+b

# my_func('Tilek')
# sum_num(4,4)
# def decrator(func):
#     def wrapper(*args, **kwargs):
#         return wrapper
# @decrator 
# def my_func(name):
#     return f'hello {name}'
# @decrator
# def my_func2(name):
#     return f'good bye {name}'
# my_func('tilek')

# def text_decor(func): посмотреть что то не получилось
#     def wrapper(*args, **kwargs):
#         print("hello! {name}")
#         func(*args, **kwargs)
#         print('good bye {name}')
#     return wrapper

# @text_decor
# def my_name(a,b):
#     return


# from datetime import datetime
# import time
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('start: ', datetime.now())
#         func(*args, **kwargs)
#         print('finish: ', datetime.now())
#     return wrapper
# @decorator
# def time_10sek():
#     for i in range(10):
#         print(i)
#         time.sleep(1)
# time_10sek()


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(res * 2)
#     return wrapper
# @decorator
# def my_func(name):
#     return f'hello {name}'
# @decorator
# def sum_num(a,b):
#     return a+b
# def decorator(func):
#     def wrapper(*args)
'zadanie 1'
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args,**kwargs)
#         print(res ** 2)
#     return wrapper
# @decorator
# def multiply(a, b):
#     return a * b
# multiply(2,2)

# 'zadanie 2'
# def decorator(func):
#     def wrapper(spisok):
#         print(func(spisok).upper())
#     return wrapper
# import random
# @decorator
# def random_(spisok):
#     return random.choice(spisok)
# random_(['Marat', 'Tilek', 'Anton'])




    

# def decorator(func):
#     def wrapper(*args):

'zadanie 3 anton'


# import random
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func()
#         print(f'rezultat do funkcii {(result)}')
#         new_list = list(set(result))
#         print(f'posle{new_list}')
#         return new_list
#     return wrapper
# @decorator
# def random_num():
#     numbers = [random.randint(10,50) for i in range(100)]
#     return numbers
# print(random_num())

'zadanie 3'
# def decorator(fun):
#     def wrapper(*args, **kwargs):
#         numbers = fun()
#         num_ = list(set(numbers))
#         return num_
#         # print(f' ishodnya funkciya: {num_}')
        
#         # print(f'posle {num_}')
#     return wrapper


# import random


# @decorator
# def random_num():
#     numbers = [random.randint(10,50) for i in range(100)]
#     return numbers

# random_num()
# def secter_login_pass():
#     def wrapper(*args, **kwargs):

# 'zadanie 4'

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         login, password = func()
#         encrypted_login = ''.join([chr(ord(bukva)+1) for bukva in login])
#         encrypted_password = ''.join([chr(ord(bukva)+1) for bukva in password])
#         return encrypted_login, encrypted_password
#     return wrapper

# @decorator
# def login_password(): 
#     login = input("vvedite login: ")
#     password = input('vvedite password: ')
#     return (login, password)
# print(login_password())

'zadanie 5'
# def decorator(func):
#     def wrapper():
#         with open('text.txt', 'a') as file:
#             file.write(str(func()))
#             login, password = func()
#             text = f'login:{login}  parol;{password} '
#             file.write(text)
#     return wrapper
    
# @decorator
# def login_password(): 
#     login = input("vvedite login: ")
#     password = input('vvedite password: ')
#     return (login, password)
# login_password()
'zadanie 6'
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'imya finkcii : {func.__name__}')
        print(f"spisok argumentov{args}")
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

@log
def sum_numbrs(*args):
    return sum(args)
print(sum_numbrs(1,2,3,4,5,6,7,8))

