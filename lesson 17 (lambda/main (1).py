# from human import eat
# from animal import *

# eat('Человек','Плов')
# get_voice('Кот', 'Мяу')


# try:
#     num = int(input())
#     raise ZeroDivisionError
#     print(num)
# except (ValueError, TypeError):
#     print('error')
# except ZeroDivisionError:
#     print('error delete on zero')

# import random

# spiskok_names = ['Beka', 'Alymbek', 'Aziz', 'Nursultan', 'Timur', 'Dastan', 'ISA', 'Emir', 'Ilim']
# new_spisok = []
# for i in range(3):
#     new_spisok.append(random.choice(spiskok_names))
# print(new_spisok)

# import sys

# num1 = input()
# num2 = input()
# print(sys.getsizeof(num1))
# print(sys.getsizeof(num2))
# if sys.getsizeof(num1) >sys.getsizeof(num2):
#     print('NUM 1 больше ')
# elif sys.getsizeof(num1) < sys.getsizeof(num2):
#     print('NUM 2 больше')
# else:
#     print('равны')

# import string
# import random

# letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# password = []
# print(letters)
# n = int(input("Введите длину пароля: "))
# for i in range(n):
#     password.append(random.choice(letters))
# print(''.join(password))


# from datetime import datetime, timedelta

# # current_date = datetime.now()
# # date_100 = current_date + timedelta(days=100)
# # print(date_100)


# current_time = datetime.now().time()
# print(current_time)

# my_list_1 = [10, 20, 30, 40, 50]
# my_list_2 = ['Python', 'Django', 'Rest', 'PostgreSQL', 'GIT']
# kolichesto_my_list1 = len(my_list_1)
# print(kolichesto_my_list1)
# for i in range(kolichesto_my_list1):
#     print(f'{my_list_1[i]} {my_list_2[i]}')
