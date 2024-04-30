'=========================Встроенные функции========================='
# map, filter, reduce, zip, enumerate, all, any
# from itertools import zip_longest
# zip - соединяет несколько последовательностей(получаем генератор, в котором элементы - tuple)
# list_ = [1,2,3,4]
# string_ = 'abcsd'
# set_ = {1.5, 2.5, 3.5}
# zipped = zip(list_, string_, set_)
# print(zipped)
# print(list(zipped))

# names = ['Anton', 'Dima', 'Max']
# ages = [20, 18, 12]
# people = dict(zip(names,ages))
# print(people)

# for name, age in zip(names, ages):
#     print(name, age)

# enumerate - нумерует последовательность (по дефолту начиная с 0), тоже получаем генератор
# names = ['Anton', 'Dima', 'Max']
# enumerated = enumerate(names)
# print(next(enumerated))
# print(next(enumerated))
# print(next(enumerated))
# enum_list = list(enumerated)
# print(enum_list)

# enum_string = 'hello world'
# enum_str = enumerate(enum_string, start=1)
# print(list(enum_str))

# names = ['Anton', 'Dima', 'Max']
# dict_names = dict(enumerate(names, start=1))
# print(dict_names)
# print(dict_names[3])

# map - функция высшего порядка, принимает другую функцию и итерируемый обьект, выполняет заданную функцию на каждый элемент последовательности
# spisok = input('Введите числа через пробел').split()
# print(spisok)
# nums = [ int(num) for num in spisok]
# nums = list(map(int, spisok))
# print(sum(nums))
# print(nums)

# spisok = input('Введите числа через пробел').split()
# print(spisok)
# def quad(x):
#     try:
#         x = int(x)
#         return x**2
#     except:
#         return 0

# quad_list = list(map(quad, spisok))
# print(quad_list)


# filter - функция высшего порядка, возращающий генератор, с элементами прощедшими фильтр (какое-то условие), принимает функции и последовательность (func, iterable)

# people = [
#     ('Jonh', 22),
#     ('Adriana', 14),
#     ('Adam', 12),
#     ('Mark', 19),
#     ('Sam', 18),
# ]
# def age_control(person):
#     return person[1] >= 18
# filtered = list(filter(age_control, people))
# print(filtered)

'=====================Lambda================='
# lamda - анонимная функция с телом, но без имени
# Общий синтаксис: lambda список_параметров: выражение

# nums = [1,2,3,4,5]
# quadra_nums = list(map(lambda x: x**2, nums))
# print(quadra_nums)

# people = [
#     ('Jonh', 22),
#     ('Adriana', 14),
#     ('Adam', 12),
#     ('Mark', 19),
#     ('Sam', 18),
# ]
# filtered = list(filter(lambda person: person[1]>=18, people))
# print(filtered)

# reduce - функция высшего порядка, которая принимает другую функцию и последовательность, возращает один элемент
from functools import reduce

# list_ = [1,2,3,4,5]
# sum_numbers = reduce(lambda x, y: x+y, list_)
# print(sum_numbers)
# string = 'hello'
# print(reduce(lambda x,y: x + '|' + y, string))
# min_number = reduce(lambda x, y: x if x<y else y, list_)
# max_number = reduce(lambda x, y: x if x>y else y, list_)
# print(min_number, max_number)

# users = [
#     {'name': 'Anton', 'age': 19},
#     {'name': 'Alina', 'age': 20},
#     {'name': 'Adilet', 'age': 12},
#     {'name': 'Max', 'age': 15},
#     {'name': 'Kristina', 'age': 30},
# ]
# max_person = reduce(lambda x,y: x if x['age']> y['age'] else y, users)
# min_person = reduce(lambda x,y: x if x['age']< y['age'] else y, users)
# print(f'Самый взрослый человек: {max_person["name"]}')
# print(f'Самый молодой человек: {min_person["name"]}')


# all - функция которая итерируемый обьект и возращает True, если все елементы последовательнсти True иначе False
# spisok = [True, 0, {'name': 'anton'}, 'hello']
# print(all(spisok))

my_list = [12,6,8,14,10,2,4]
result = all(x % 2 == 0 for x in my_list)
# print(result)

# any - функция которая принимает последовательность и возращает True, если хотя бы один элемент был истинной (True) иначе False

# print(any([False, False, False]))
# print(any([False, False, True]))

# my_list = [1,2,3,4,5]
# result = any(x>5 for x in my_list)
# print(result)

'Задача: Проверить, все ли строки списка содержат только буквы.'
# my_list = ['abc', 'def123', 'ghy']
# result = all([x.isalpha() for x in my_list])
# a = list(map(str.isalpha, my_list))
# print(a)
# result1 = all(map(str.isalpha, my_list))
# print(result)
# print(result1)


# def sort_by(element) -> int:
#     return len(element)
# print(sort_by('banana'))

# sorted_lambda = lambda element: len(element)
# print(sorted_lambda('kak ty brat?'))

# fruits = ['banana', 'apple', 'grape']
# sorted_fruits = sorted(fruits, key = lambda element: len(element))
# print(sorted_fruits)

# longest_word = max(fruits, key = lambda element: len(element))
# print(longest_word)

# s = lambda a, b: a + b
# s(1, 2)

'================================Lambda================================='
# hello = lambda : 'hello'
# print(hello())

# sum_kvad = lambda a, b, c: a**2+b**2+c**2
# print(sum_kvad(1,2,3))

# Анонимная функция - функция с телом, но без имени

# calc = {
#     "+":lambda n1,n2:n1 +n2,
#     "-":lambda n1,n2:n1 -n2,
#     "*":lambda n1,n2:n1 *n2,
#     "/":lambda n1,n2:n1 /n2,
#     "%":lambda n1,n2:n1 %n2,
#     "//":lambda n1,n2:n1 // n2,
# }
# def main():
#     try:
#         num1 = int(input("chsilo"))
#         num2 = int(input("chislo2"))
#         operator = input('vvedite operatora(+,-,*,/,%,//)')
#         func_ = calc[operator]
#         result = func_(num1, num2)
#         return result
#     except ValueError:
#         print("vy vveli ne chislo")
#         main()
#     except ZeroDivisionError:
#         print("delit' na bol' nel'zya")
#         main()
#     except KeyError:
#         print("Takogo operatora net")
#         main()
# print(main())

f1 = lambda x, y, z=3: sum((x,y,z))
# print(f1(1,2))
# print(f1(1,2,3))
f2 = lambda *args: sum(args)
# print(f2(1,2,2,3,3,4,5,6,76,78,8,34,5))
f3 = lambda *args, **kwargs: sum(kwargs.values())
# print(f3(n1=1,n2=2,n3=3))


#Основные качества lambda
# 1. Однокраиное использование функции
# 2. Передача функции в качестве аргумента другим функциям
# 3. Возвращение только одного значения

# strings = ['a', 'b', 'c', 'd', 'e']
# numbers = [3,3,3,3,3,]
# new_string = list(map(lambda x,y: x*y,strings,numbers))
# print(new_string)

# numbers = [1,2,3,4,5]
# itog = list(map(lambda x: x**2,numbers))
# print(itog)


# numbers = [-11,2,3,4,-1, 6]
# positive_numbers = list(filter(lambda x: x>0,numbers))
# large_numbers = list(filter(lambda x: x>30,numbers))
# even_numbers = list(filter(lambda x: x%2==0,numbers))
# print(positive_numbers,large_numbers,even_numbers)

list1 = [1,2,2,1]
list2 = [5,6,7,8]
zipped = zip(list1, list2)
# print(list(zipped))
itog = list(filter(lambda x: sum(x)==9, zipped))
# print(itog)
# itog = list(filter(lambda x,y: x+y, ))
# print(itog)

'===================================Рекурсия=================================='
# Рекрусивная функция - это функция, которая вызывает сама себя , и при каждом очередном вызове использует данные
# созданные во время предыдущего вызова
#1. Граничный случай, при котром функция завершает свою работу и возвращает данные в основную программу
#2. Рекурсивный случай, при котром функция продолжает вызывать себя 
def greetings(string):
    print(string)
    if len(string) == 0:
        return # Граничный случай
    else:
        greetings(string[:-1]) #Рекурсивный случай
greetings("hello world")


# def factorial(n): # c рекурсией
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(10))

# def fact(n):
#     factorial = 1
#     for i in range(1, n+1):
#         factorial *= i
#     return factorial
# print(fact(10))


# def even_num(spisok_num):
#     num = spisok_num.pop()
#     if num % 2 == 0:
#         print(num)
#     if len(spisok_num) == 0:
#         return
#     else:
#         even_num(spisok_num)
# numbers = [1,2,3,4,5,6,7,8]
# even_num(numbers)


# strings = ['a', 'b', 'c', 'd', 'e']
# numbers = [3,3,3,3,3,]
# new_string = list(map(lambda x,y: x*y,strings,numbers))
# print(new_string)

# n1 = 1
# n2 = 2
# n3 = 3

# multipl = lambda x,y,t: f'obem korovki {x*y*t}'
# print(multipl(n1,n2,n3))
# n1 = 3
# n2 = 4
# kub = lambda x,y: f"summa dvuh argumenta {n1**3 + n2**3}"
# print(kub(n1,n2))

'zadanie 3'
# def not_even_number(spisok_num):
#     num = spisok_num.pop()
#     if num % 2 > 0:
#         print(num)
#     if len(spisok_num) == 0:
#         return
#     else:
#         not_even_number(spisok_num)


# list_ = [1,2,3,4,5,6,7,8,9,10]
# not_even_number(list_)

'zadanie 4'
# days_2024 = 31+29+30+22
# days_to2025 = lambda x:f'stolko dnei ostalos do ng{365 - days_2024}'
# print(days_to2025(days_2024))
data_new_year = lambda days_pass: 365 - days_pass
print(data_new_year(43))


'zadanie 5'
# years = 5
# years_to_days = lambda x:f"stolko dnei v {x*365}"
# print(years_to_days(years))
'zadanie 6'

# list_ = [1,2,3,4,5,6,7]
# def delete_num(spisok_num):
#     num = spisok_num.pop()
#     if num == True:
#         print(num)
#     if len(list_) == 1:
#         return
#     else:
#         delete_num(spisok_num)
# delete_num(list_)

# list_ = [1,2,3,4,5,6,7]
# def remove_one(lst):
#     if not lst:
#         return
#     lst.pop()
#     print(lst)
#     remove_one(lst)
# print(remove_one(list_))
'zadanie 7'
# list_ = [2, 5, 20, 100, 9, 1, 6, 7, 12, 8]
# number = list(map(lambda x: x**3,list_))
# print(number)
'zadanie 8'
# list_ = [2, 5, 20, 100, 9, 1, 6, 7, 12, 8]
# number_ = filter(lambda x: x % 3 == 0, list_)
# print(list(number_))
'zadanie 9'
# def sum_num(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sum_num(n//10)
# print(sum_num(256))