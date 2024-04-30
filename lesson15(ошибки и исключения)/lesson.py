'==============================Try Except=================================='
# исключение - это обьекты которые прерывают работу кода, 
# если не были обработаны(связаны с логикой нашей программы)
# print(10 + '10') #TypeError
#Ошибки - обьекты, которые прерывают работу и их нужно обработать
# (связаны по большой части с разработчиком)
# print( #SyntaxError: '(' was never closed

SyntaxError
#ошибка, которая выходит, когда в коде допущена синтаксическая ошибка
# '''
# # 'SyntaxError: unterminated triple-quoted string literal (detected at line 12)'
# # когда мы не закрыли скобку либо кавычки

# a = 
# SyntaxError: invalid syntax

NameError
#исключение, которые выходит когда мы обращаемся к несуществующей переменной
name = 'Tilek'
# print(Name)
# NameError: name 'Name' is not defined. Did you mean: 'name'?


IndexError
# исключение, котороые вызодит когда мы обращаемся по несуществующему индексу
list_ = [1,2,3]
#print(list_[3])
'IndexError: list index out of range'
# list_.pop(4)
'IndexError: pop index out of range'

KeyError

#исключение, которое выходит когда мы обращаемся по несуществующему ключу
# dict_ = {'a': 1}
#print(dict_['b'])
"KeyError: 'b'"
#dict_.pop('b)
"KeyError: 'b'"

ValueError
# исключение, когда мы передаем функцию не коректный для нее данных
# int('12d')
"ValueError: invalid literal for int() with base 10: '12d'"
# когда мы распоковываем итерируемый обьект на несколько переменных и количество переменных
# не совпадает с количеством элементов внутри итерируемого обьекта
# a,b,c = [1,2]
# ValueError: not enough values to unpack (expected 3, got 2)
TypeError
# Исключение, когда мы пытаемся использовать методы не свойственный какому-то типу данных или когда мы пытаемся
# передать функции больше или меньще аргументов, чем принимает эта функция
# for i in range 12345:
#     print(i)
# "TypeError: 'int' object is not Iterable"
# '5' + 5 #TypeError: can only concatenate str (not "int" to str)
# {[1,2,3]: 'gel'} # Type Error:unhashable type:'list'
# input('hello!', 'world')#TypeError:input excepted at most 1 argument, got 2


ZeroDivisionError
#выходит при деление на ноль 
# 5/0 
'ZeroDivisionError: division by zero'

AttributeError
# выходит, когда мы обращаемся к несуществующему мутоду или атрибуту у обьекта (типа данных)
#[].replace()
"AttributeError: 'list' object has no attribute 'replace'"
IndentationError
#выходит когда мы не правильно используем отступы
    # a = 5
"IndentationError: unexpected indent"
# for i in 'abs':
# print(i)
# "IndentationError: expected an indented block after 'for' statement on line 74"

Exception
# исключение, которое мы сами создали, чтобы его вызвать
"Вызов исключений происходит с помощью ключевого слова : raise"
# raise Exception('ошибка')

'==================================обработка исключений=================================='
# чтобы код не прекращал свою работу, мы можем использовать конструкцию
# try - except и обрабатывать вызванное исключение

# try:
#     #код, который возможно вызовет ошибку
#     num = int(input("vvedite chislo: "))
# except ValueError: #исключение которое может возникнуть
#     print("Вы ввели не число") # код который отработает только если ошибка вызвалась
# else:  #код который отработает только если никакая ошибка не вышла
#     print('вы ввели число',  num)
# finally: #код который отработает в любом случае
#     print('do svidanie')

# try:
#     while True:
#         num = int(input('vvedite'))
#         num2 = int(input('vvedite'))
#         print(num/num2)
# except ZeroDivisionError:
#     print('delit na nol nelzya')
# except ValueError:
#     print('nujno bylo vvesti chislo')

# try:
#     num = int(input('vvedite chislo'))
#     if num == 0:
#         raise ValueError
# except (SyntaxError, NameError, ValueError):
#     print('vywla kakayato owibka')
    

# try:
#     raise Exception
# except:
#     print("lyubaya owibka")

# try:
#     raise TypeError("owibka tipa dannyh") # prosmotert' osobo ne ponyal
# except Exception as error:
#     print(error)

# try:
#     num1 = input('vvedite chislo')
#     num2 = input('vvedite chislo')
#     print(int(num1) + int(num2))
# except:
#     print(num1+num2)

try:
    age = int(input('vvedite vaw vozvrast'))
    if age > 0:
        print(age)
    else:
        raise Exception
except:
    print("ne dopustimiy vozsrat")
