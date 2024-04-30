'====================================Область видимости================================'
# LEGB - local Enclosed Global Build-in
# a = 5
# def func(a):
#     b = 10
#     print(a)
# func(1)
# print(b)
'===================================BUILD IN===================================='
# Встроенное пространство имен(list, sum, print,input, max...)
# our_len = len
# print(our_len('123456'))
'================================= Global========================================'
# Все переменные, которые мы создали внутри одного файла(модуля) чтобы посмотреть 
# глобальные переменные можно использовать globals
# a = 5
# b = 6
# c = 1
# print(globals())
'==============================Encloused(nonlocal)==============================='
# замкнтуное простанство - локальное пространство, у которого есть внутрннее локальное пространство.
# var = 'globals'
# def func():
#     var = 'encloused'
#     def inner_func():
#         var = 'local'
#         print(var)
#     print(var)
#     inner_func()
# print(var)
# func()
'=====================================Local========================================'
# Локальное пространство имен - переменные, созданные внутри функции(можно посмотретьс помощью locals()
# a = 10
# def func (a,b):
#     print('global: ', globals())
#     print('Locals: ', locals())
#     print(a,b)
# func(5,6)

# count = 1
# def count_():
#     global count # доступ на изменение переменной глобального пространства
#     print(count)
#     count += 1
#     print(count)
# count_()
 
#  count = 1
# def count_():
#     count2 = 0
#     def inner_func():
#         nonlocal count2
#         global count
#         count2 = 10
#         count = 100
#     inner_func()
#     print(count2)
# count_()
# print(count)


# matrewka = 100
# def counter():
#     matrewka2 = 50
#     def counter2():
#         nonlocal matrewka2
#         global matrewka
#         matrewka2 = matrewka2 + matrewka
#     counter2()
#     print(matrewka2)
# counter()
# print(matrewka)

# matreshka = 100
# def func(matreshka_2):
#     global matreshka
#     matreshka = matreshka + matreshka_2
#     def func2(matreshka_3):
#         global matreshka
#         matreshka = matreshka + matreshka_3
#     func2
# func(1)

# num = 3
# def mul():
#     global num
#     num = num **2
# mul()
# mul()
# mul()
# print(num)


spisok = []
def add():
    global spisok
    name = input("napiwite imena: ")
    spisok.append(name)
    return spisok

def remove():
    global spisok
    index_ = int(input('ukajite kakoi index udalit'))
    user = spisok.pop(index_)
    return spisok
def random_func(number):
    import random
    for i in range(number):
        ran = random.randint(0,1)
        if ran == 0:
            add()
        else:
            remove()
    return spisok
print(random_func(10))

