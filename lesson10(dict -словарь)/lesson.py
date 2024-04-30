# '================================Словарь (dict)========================================'
# # словарь - это изменяемый, итерируемый, неупорялочный, неидексируемый, тип данных, 
# # хранит в парах {ключ: значение} {key: value}
# user = {'name': 'tilek', 'login': 'anton1123', 'password': 12345}
# print(user['name'])
# # ключами в словаре могут быть только неизменяемые типы данных
# # ключи должны быть уникальными , не должны повторятся, если же они  повторяются то сохранится последний
# dict_ = {1: 'Anton', 2: 'Ainazik', 3:'Alina', 1:'Max'}
# print(dict_[1])
# # значение могут быть любые типы данных, могут повторятся
# # print(dict[4]) Key Error: 4
# '==================================Создание словарей====================================='
# # dict_ = {'1': 'a', '2': 'b', '3': 'c'}
# # dict_2 = dict([('1', 'a'), ('2', 'b'), ('3', 'c')])
# # print(dict_)
# # print(dict_2)

# # dict_['1'] = 'tilek'
# # dict_['2'] = 'aidana'
# # dict_['3'] = 'tilek2'
# # print(dict_)
# '==================================Методы словарей========================================='
# # get - метод, который возвращает значение по ключу, если такого ключа нет, 
# # то возвращает None или дефолтное значение
# dict_ = {1:'Anton', 2:'Ainazik', }
# print(dict_.get(2))
# # pop - метод, удаляет пару по ключу и возвращает значение
# remove_element = dict_.pop(1)
# print(remove_element)

# # popitem - метод, удаляет последнюю пару и возвращает ее
# print(dict_.popitem())

# # update - метод, который расширяет словарь парами из другого словаря
# dict_3 = {1:'Akmaral', 4:'Seit'}
# print(dict_)

# # clear - очищает словарь
# dict_.clear()
# print(dict_)

# # fromkeys - метод, который создает новый словарь используя список ключей
# dict_1 = dict.fromkeys([1,2,3,4,5,], 'name')
# print(dict_1)

# # keys, values, items
# # keys - метод, который возвращает все ключи
# # values - метод, который возвращает все значения
# # items -  метод, который возвращает tuple(ключ, значение)
# print(dict_1.keys())
# print(dict_1.values())
# print(dict_1.items())
'========================================итерирование словарей==========================================='

user = {'name': 'tilek', 'login': 'anton1123', 'password': 12345}
# for key in user.keys():
#     print(key)
for values in user.values():
    print(values)

# for key, value in user.items():
#     print(key, value)
# new_user = {}
# for key, value in user.items():
#     new_user[value] = key
# print(new_user)
# print(user)

# university = {'программирование': 10, 'экономика': 9, 'медицина': 8}
# university['программирование'] = 12
# university['лингвистика'] = 10
# university.pop('медицина')
# sum_ = 0
# for value in university.values():
#     sum_ += value
# print(sum_)
# print(sum(university.values()))
# nachalo = {1: 'a', 2: 'b', 3: 'c'}
# new_dict = {}
# for key, value in nachalo.items():
#     new_dict[value] = key
# print(new_dict)

# gosti = int(input("kolichistvo goste: "))
# new_dict = {}
# party = []
# for i in range(1, gosti + 1):
#     names = input('imya gostya')
#     party.append(names)
#     new_dict[i] = names
# print(party)
# print(new_dict)
# d1 = {"a": 100, "b": 200, "c":300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# print(d1["b"] == d2["b"])
# person = {"name": "Kelly", "age":25, "city": "New york"}
# values_ = person['age']
# print(values_)


# set_ = {6, 4, 2, 5, 7, 8, 10, 9}
# set_.discard(2)
# print(set_,'salam aleikum')
set_ = {'Python', 'it', 'c++', 'java', 'programming'}
set2 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
set3 =  set.intersection(set2)
print(set3)