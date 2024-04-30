'==================================ASCII======================================='
# ASCII - предатсавляет собой набор из 128 цифровых кодов, которые обозначают латиниские буквы.

'====================================Unicode==================================='
#Unicode - таблица символов Unicode представляет собой набор цифровых символов, которые включает в себя
# знаки почти всех письменных языков
#Первые 128 кодов из таблицы символов Unicode совпадает с ASCII
# Unicode = это не кодировка , это таблица символов
# Кодировка на таблице символов Unicode - например UTF - 8

'====================================ORD======================================='
# Ord - позволяет определить код некоторого символа в таблице символов
# Unicode 
ord1 = ord('a')
ord2 = ord('а')
ord3 = ord('b')
ord4 = ord('c')
# print(ord1, ord2, ord3, ord4)

'====================================Char======================================'
#Chr - позволяет по коду символа оперделить сам символ
chr1 = chr(65)
chr2 = chr(66)
chr3 = chr(67)
# print(chr1, chr2, chr3)

# a = 1
# b = 97
# finish = (chr(i) for i in range(a, b))
# print(finish)
text = 'salam aleikum'
spisok = []
for i in text:
    spisok.append(ord(i))
# print(spisok)

'=================================декотраторы с параметрами======================'
# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator


# def my_func(text):
#     print(text)
# my_func("hello, world")

# from  functools import wraps
# def limit_calls(max_calls):
#     def decorator(func):
#         call_count = 0
#         @wraps(func)
#         def wrapper (*args, **kwargs):
#             nonlocal call_count
#             if call_count >= max_calls:
#                 print(f'funkciya {func.__name__} dostigla limita vyzova ({max_calls})')
#                 return
#             call_count += 1
#             result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
# @limit_calls(3)
# def my_function():
#     print('vyzvana funkciya my_function')
# my_function()
# my_function()
# my_function()
# my_function()
def make_bold(fun):
    def wrapper(*args, **kwargs):
        func = fun(*args, **kwargs)
        new_shrift = f'<b> {func} </b>'
        return new_shrift
    return wrapper
def make_italic(fun2):
    def wrapper(*args, **kwargs):
        func2 = fun2(*args, **kwargs)
        new_shrift = f''

@make_bold
def hello():
    return 'HELLO WORLD!'
print(hello())