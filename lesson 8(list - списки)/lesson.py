# # '===============================List============================'
# # Списки (list) - изменяемый, индексируемый, упорядочный итерируемый тип данных,
# # предназначенный для хранения любых данных в определенном порядке.
# # 'Создание списка'
# # numbers = [2, 4, 6, 8]
# # letters = ['a', 'b', 'c', 'd']
# # list1 = [1, 2, 3, 'hello', [1, 2, 3], None, True]
# # list1[1]
# # # list[3]
# # # list[4][0]
# # list2 = list('ada')
# # list3 = list(range(1,11))
# # #range - генератор какого-нибудь диапазона range(start, end, step)
# # list2 = list('ada')
# # list3 = list(range(1,11))
# # # сцепление списков
# # list_sum = list2 + list3
# # # дублирование 
# # list4 = list2 * 4
# # print(list4)
# # # нахождения длинны
# # print(len(list4))
# # # "==================================min и max=================================="
# # # max() - функция, которая возвращает максимальное значение
# # # min() - функция, которая возвращает минимальное значение
# # # sum() - функция, которая возвращает сумму всех значений
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(sum(numbers))
# # print(min(numbers))
# # print(max(numbers))


# # numbers[-2] = -2
# # print(min(numbers))
# # print(numbers)
# # '=================================оператор принадлежности in==================================='
# # numbers = [2, 4, 5, 6]
# # if 2 in numbers:
# #     print("spisok soderjit chislo 2")
# # else:
# #     print('kak ty brat')

# # # so str kak rabotaet
# # if 'a' in 'abc':
# #     print('yes')
# # '=============================================методы списка==================================='
# # print(dir(list))
# # # append - добавляет элемент в конец списка
# # list.append(name)
# # list1 = []
# # print(list1)
# # # pop - udalyaet element iz spiska po indeksu i vozvrawaet etot udalenniy
# # # element esli ne ukazyvat' index to on udalit posledniy element
# list1 = [1,1,1,1,1,1,1, 2, 3, 4, 5, 6, 'ada', True]
# pop_element = list1.pop(1)
# print(pop_element)
# print(list1)

# # remove - udalyaet element iz spiska po znacheniyu
# list1.remove('ada')
# print(list1)

# # count - metod kotoriy schitaet kolichestvo prinyatogo elementa v spiske
# print(list1.count(1))

# # index - vozvrawaet index prevogo vhojdeniya elementa
# list2 = ['ada', 1, 2, 3, 4, 5, 6, 7, 'ada']
# print(list2.index('ada'))

# # insert - dobavlyaet  element v spisok po indexu
# list2 = [1,2,3,4,5,6]
# list2.insert(2, 3) # perviy argument eto indeks a vtoroi to chto my hotim dobavit' v spisok
# print(list2)

# # extand - raswiryaet spisok zaschet drugogo spiska
# list1 = [0, 0, 0]
# list2 = [1, 1, 1]
# # list1.append(list2)
# list1.extend(list2)
# print(list1)
# # reverse - izmenyaet spisok rastavlyaya ego elementy v obratnom poryadke
# list1.reverse()
# print(list1)
# # sort - sortiruet spisok, sostoyavwiy iz elementov odnogo tipa dannyh
# list1 = [1, 2, 3, 4, 5, 43, 7, 8, 32]
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# # clear - ochiwaet spisok
# print(list2)
# list2.clear()
# print(list2)
# # copy - method dlya kopirovaniya dannyh vnutri spiska
# list = [1,2,3]
# a = list1
# print(a)

# # a,b,c = [1,2,3] множественное присвоение
# name, age = input(), input()
# print(name, age)
# list1 = list('hello world')
# print(list1)
# list2 = '-'.join(list)
# print(list2)
# print(*list1) # raspokovka spiska

# n = 10
# if i in range(1, n):
#     print(i)
'==================================Turple==================================='
'urple(кортеж) - неизменяемый тип данных, упорядочен, индексируемый и итерируемый'
'''kortje yavlyaetsya neizmenyaemiym tipom dannyh chto oznachaet posle sozdaniya ego soderjaimoe 
nel'zya izmenit

упорядочен - это означает что порядок эдлементов в кортеже сохраняется
индексируемый - что позваляет получить доступ к его элементам по индексу
итерируемый - это означает, что мы можем перебрать все его элементы в цикле'''
# turple_ = (1,2,3) #kortej
# print(type(turple_))
# turple_1 = () #truple
# turple_2 = (1,)# truple
# truple_3 = 1, # turple
# print(type(turple_4))
# turple_5 = turple('hellowrold')
# print(turple_5)
# print(dir(turple))

