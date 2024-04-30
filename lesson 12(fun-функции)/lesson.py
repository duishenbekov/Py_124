'================================функция =============================='
# Функция - это именованный блок кода, который вызывает множество раз в других частях программы
# они создаются благодаря ключевому слову def
# при наименовании функции придерживаются стилю Snake_case

# def name_of_functions(a, b - параметры функции, их может быть сколько угодно):
    #<body> код, который имеет некую логику
    #return оператор, который возвращает результат выполнения функции
# def my_func():
#     a = 4
#     b = 5 
#     print(a + b)
#     return a + b
# print(my_func())

# list_numbers = [2, 3 ,4, 6,10 ,7 ,7,8, 8]
# def find_even():
#     for el in list_numbers: 
#         if el % 2 == 0:
#             print(f'chetnoe chislo:{el}')
# find_even()
#     [print(f'chetno chislo: {el}') for el in list_numbers if el % 2 ==0]
# find_even()
# def say_hello_world():
#     name = input('name')
#     print(f'{name} hello world')
#     print(f'{input('vvedite vawe imya: ')} govorit hello world!')

# say_hello_world()


'zadanie 2'

# def summa_n():
#     summa_ = []
#     t = int(input('chislo'))
#     s = sum([i for i in range(1, t+1)])
#     print()
            
            
# summa_n()

# def exponentiation():
#     num = int(input('chislo:'))
#     print(f'{num**2} {num*num*num}')
# exponentiation()


def sum_num():
    pustaya = []
    stroka = input()
    for i in stroka:
        if stroka.isdigit():
            pustaya.append(int(i))
            print(sum(pustaya))
sum_num()


# stroka = input()
# if stroka.isdigit:
#     print(type(stroka))
