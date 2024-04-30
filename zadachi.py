# a = 'ada#bootcamp#программирование#it#курсы'
# b = a.split('#')
# print(b)
# 'zadanie 2'

# dlinna = len(input('dlinna'))
# if dlinna >= 5:
#     print('True')
# else:
#     print('False')

# 'zadanie 3'
# chislo = int(input('chislo: '))
# if chislo > 0:
#     print('positive')
# elif chislo == 0:
#     print('Zero')
# else:
#     print('negative')

# 'zadanie 4'
# mesyac = int(input('vvedite ot 1  do 12'))
# if mesyac < 3 or mesyac == 12:
#     print('zima')
# elif mesyac >= 3 and mesyac <= 6:
#     print('vesna')
# else:
#     print('osen')
# 'zadanie 5' ne zakonchil
# slova = input('slova: ').split()
# slova2 = slova.index(1)
# print(slova2)
# print(dir(list))

# slova = []
# num = []
# for i in range(5):
#     word = input("slova: ")
#     slova.append(word)
#     num.append(len(word))
# print(num)
# print(slova)
'zadanie 6'
# nums2 = []
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in nums:
#     if i < 5:
#         nums2.append(i)
# print(nums2)

'zadanie 7'
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = a.copy()
# for key, value in b.items():
#     if value % 2 == 0:
#         b[key] = 2
# print(b)


'povtorenie'
# person = {
#     'name' : 'Jonh',
#     'national': 'Kyrgyz',
#     'age': 25
# }
# print(person)
# person['job'] = 'enginer' 
# print(person)
# person2 = {}
# person2['kak dela'] = 'otlichno'
# person2['age'] = 2
# person2[22] = 2.2
# print(person2)
# print(person2[22],['age'])
# person = {
#     'name' : 'Jonh',
#     'national': 'Kyrgyz',
#     'age': 25
# }
# person2 = {
#     'lyubov' : 'Aidana',
#     'date' : '20.10.22',
#     'range': '2 yeaars'
# }
# # person.update(person2)
# # print(person)
# person = person | person2
# print(person)


# # задание
# # Есть список словарей со студентами `students`. В каждом объекте есть имя и фамилия студента,
# # а также список оценок (целых чисел). Нужно написать функцию get_best_students, которая берёт студентов и находит того,
# # у кого средний балл наибольший. Возвращает функция список студентов с лучшим баллом. У некоторых студентов в оценках
# # есть None: их среднюю оценку мы считаем равной 0.


# # students = [
#     {"name": "John", "surname": "Doe", "grades": [5, 5, 4, 4]},
#     {"name": "Jane", "surname": "Doe", "grades": [4, 3, 4, 3, 5]},
#     {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]},
#     {"name": "Steve", "surname": "Jobs", "grades": [3, 5, 4, 3, 3, 5]},
#     {"name": "Guido", "surname": "Van Rossum", "grades": [5, 3, 5, 4, 5, 5, 3, 5]},
#     {"name": "Elon", "surname": "Musk", "grades": None}
# ]



'list'
# num = input().split()
# print(sum(num))
# # print(sum(num2))
# number = input("chislo")
# number_list = number.split()
# for num in number_list:
#     num_of_number = sum(int(number))
#     print(num_of_number)
# number = ['apple', 'kfensflknsekf', 'fesjknfjnsjkfnsjnefkjsnef']
# index_ = number[2]
# print(len(index_))
'for'
# world = 'salam braooooot, kak dela?'
# count_o = 0
# for i in world:
#     if i == 'o':
#         count_o += 1
#         print(i)
# print(count_o)


# for i in range(1, 10):
#     for j in range(1, 10):
#         num3 = i * j
#         print(f'{i} * {j}= {num3}' )
#     print()

    # for i in num2:
    #     num2 * i
    # print(i * num2)
# for i in range(1, 10):
#     print(type(i))

'funkcii'

# def find_min_number(l):
#     min_number = l[0]
#     for i in l:
#         if i < min_number:
#             min_number = i
#     print(min_number)


# num1 = [1, 2, 3 ,4, 6, 7,8, 0.1]
# find_min_number(num1)

# def find_average(l):
#     l = sum(l) / len(l)
#     print(l)
# numbers = [45, 23, 123, 55]
# find_average(numbers)
# def find_letter(l):
#     letter = ' '
#     for char in l:
#         if char.isalpha():
#             letter += char
#     print(letter)
#     print(len(letter))
#     return
# find_letter('sala21312412m 4124aleikum')
'zadanie3'
# import random
# names = ['Beka', 'Alymbek', 'Aziz', 'Nursultan', 'Timur', 'Dastan', 'ISA', 'Emir', 'Ilim']
# for i in range(3):
#     names3 = random.choice(names)
#     print(names3)

'zadanie 6'
# import random
# def gen_password():
#     num3 = ''
#     num2 = [1,2,3,4,5,6,7,8,9]
#     num = int(input("skajite chislo: "))
#     for i in range(1,num):
#         gen_password2 = str(random.choice(num2))
#         num3 += gen_password2
#     print(num3)
# gen_password()

# import string

'zadanie 7'
# import random
# def game_play():
#     name = input('napiwite vawe imya: ')
#     print(f"{name} давайте играть")
#     igra = ['камень', 'ножницы', 'бумага']
#     robot = random.choice(igra)
#     human = input("выберите бумага, камень, ножницы")
#     if human == "бумага" and robot == 'камень' or human == 'ножницы' and robot == 'бумага' or human == 'камень' and robot == 'ножницы':
#         print(f"вы выйграли!!!bot vybral {robot}")
#     elif robot == "бумага" and human == 'камень' or robot == 'ножницы' and human == 'бумага' or robot == 'камень' and human == 'ножницы':
#         print(f"vy proigrali!!! bot vybral {robot}")
#     else:
#         print("ничья")
# game_play()

'zadanie 4'
# import sys
# os_name = sys.platform
# print(os_name)

# import sys
# num1 = 100
# num2 = 200
# print(sys.getsizeof(num1))
# print(sys.getsizeof(num2))

'zadanie 8'
# from datetime import datetime, timedelta
# # current_date = datetime.datetime.now()
# # date_100days = current_date + datetime.timedelta(days=100)
# # print(current_date)
# # print(date_100days)
# time_ = datetime.now().time()
# print(time_)

'zadanie 10'
my_list_1 = [10, 20, 30, 40, 50]
my_list_2 = ['Python', 'Django', 'Rest', 'PostgreSQL', 'GIT']
for i in range(len(my_list_1)):
    print(f"{ my_list_1[ i]} { my_list_2[i]}")