'===========================Циклы============================='
# Циклы - это блок кода, который отрабатывает несколько раз
# 1. For - цикл, который работает до конца итерируемого обьекта
# 2. While - цикл, который работает пока условие истина (True)

"FOR"
# stroka = 'hello world'
# for i in stroka:
#     print(i)

# list_ = [1]
# for i in list_:
#     print(i)

# range - диапазон числе range(start, end, step)
# for i in range(1,11):
#     print(i)


# text = """Пробелы - самый предпочтительный метод отступов.
# Табуляция должна использоваться только для поддержки кода, написанного с отступами с помощью табуляции.
# Python 3 запрещает смешивание табуляции и пробелов в отступах.
# Python 2 пытается преобразовать табуляцию в пробелы."""

# text1 = text.replace('.', '').replace(',', '')
# text2 = text1.split()
# counter = 0
# for word in text2:
#     if word.isalpha() and len(word) > 3:
#         counter += 1

# print(f'Слов в нашем тексте: {counter}')

#WHILE

# count = 1
# while count<=10:
#     print('hello world')
#     count +=1
# print(1)
# text = print(f'Введите какой-либо текст, если хотите закончить введите выход: ')
# active = True
# while active:
#     message = input()
#     if message == 'выход':
#         active = False
#     else:
#         print(message)

'============================Breake and continue======================='
# breake - оператор, который остнавливает цикл(выходит из цикла)
# continue - оператор, который переходит к следующей итерации

# for i in range(1, 10):
#     print(i)
#     if i ==3:
#         break
# for i in range(10):
#     if i==3:
#         continue
#     print(i)
'=============================Вложенные циклы==========================='
#  Влоденный цикл располоден еще в одном цикле, т.е. внутри тела другого
# циклы
# import time
# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(f'{hours}:{minutes}:{seconds}')
#             time.sleep(1)
# Вложенный цикл выполняет все свои итерации для каждой отдельной итерации внешнего цикла
# итерации внешнего цикла
# вложенные циклы завершают свои итерации быстрее чем внешние циклы

# for i in range(8):
#     for j in range(i+1):
#         print(i)
#         print('*', end='')
#     print()
# n = 5
# for n in range(5 * 3):
#     for b in range(1):
#         for c in range(1):
#             print(n * 3, end='')
#     print()
#             # print(f'{n}, {b}, {c}')
# n = 5
# for i in range(n):
#     print(n, n, n)
# n = 8
# for i in range(1,n+1):
#     for j in range(1, 5+1):
#         print(i, end= " ")
#     print()
# m = 13
# n = 19
# if m > n:
#     for m in range(n, m+1):
#         print(m)
# elif m < n:
#     for n in range(n, m, -1):
#         print(n)
# a = 1
# b = 10
# for num in range(1, a + 1):
#     for j in range(1, 10):
#         print(f'{num} + {j} = {num + j}')
#     print()
# Даны два натуральных числа m и n (m≤n). Напишите программу, которая выводит все целые числа от m до n включительно, удовлетворяющие хотя бы одному из условий:
#  • число кратно 17
#  • число оканчивается на 9
#  • число кратно 3 и 5 одновременно.
# Пример
# 1
# 20
# Вывод
# 9
# 15
# 17
# 19
# m = 1
# n = 20
# for num in range(m,n):
#     if num % 17 == 0:
#         print(f'{num} число кратно 17')
#     elif num % 10 == 9:
#         print(f'{num} число оканчивается на 9')
#     elif num % 3 == 0  and num % 5 == 0:
#         print(f'{num} число кратно 3 и 5 одновременно. ')
# n = 15
# j = 1
# for i in range(1, n):
#     j += 1
#     if n % j == 0:
#         print(int(j))
#         break

        
# number = 20
# number2 = [x**2 for x in range(1,number) if x % 2 == 0 if x % 6 == 0]
# print(number2)
# S = [x**2 for x in range(10)]
# # print(S)

# list_ = [1,2,3,4,5]
# spisok = []
# for i in range(list_):
#     i + spisok
#     print(spisok)
# list_ = [1, 2, 3, 4, 5]
# spisok = []
# for i in list_:
#     spisok.append(i)
#     print(spisok)
list_ = [1,2,3,4,5,6]
integer = [2,3,4,5,6]
list3 = list_.extend(integer)
print(list3)