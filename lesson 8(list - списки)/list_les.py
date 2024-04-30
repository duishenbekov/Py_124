# # '=======================LIST=========================='
# # # Списки (list) - изменяемый, индексируемый, упорядочный, итерируемый тип данных, предназначенный для хранения любых данных в опеределенном порядке
# # 'Cоздание списка'
# # numbers = [2,4,6,8]
# # letters = ['a', 'b', 'c', 'd']

# # list1 = [1,2,3,'hello', [1,2,3], None, True]
# # list1[1] # 2
# # list1[3] # hello
# # list1[4] # [1,2,3]
# # list1[4][0] # 1
# # list1[-1] # True

# # list2 = list('ada') # ['a', 'd', 'a']
# # list3 = list(range(1,11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # range - генератор какого-нибудь диапазона range(start, end, step)

# # # Cцепление списков
# # list_sum = list2 + list3 # ['a', 'd', 'a', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # Дублирование списка
# # list4 = list2 * 4
# # # Нахождение длины
# # print(len(list4)) # 12

# # '========================Max() Min() Sum()========================='
# # # max() - функция, которая возращает максимальное значение
# # # min() - функция, которая возращает минимальное значение
# # # sum() - функция, которая возращает сумму всех значений
numbers = [1, 2, 4, 11, 22, 333, -1]
print(sum(numbers))
print(min(numbers))
print(max(numbers))

# # numbers[-2] = -2
# # # print(numbers)
# # # print(min(numbers))
# # # print(max(numbers))

# # '=======================Оператор принадлежности in ===================='
# # numbers = [4,5,6]
# # # if 2 in numbers:
# # #     print("список содержит число 2")
# # # else:
# # #     print("в списке нет числа 2")

# # # counter = 0
# # # while True:
# # #     word = input()
# # #     if word in ['стоп', "хватит", "достаточно"]:
# # #         break
# # #     if not word:
# # #         continue
# # #     counter +=1
# # # print(counter)
# # # if 'a' in 'abc':
# # #     print('yes')

# # '============================Методы Списка======================'
# # # print(dir(list))

# # # append - добавляет элемент в конец списка
# # name = 'Anton'
# # list1 = []
# # list1.append(name)
# # list1.append('ada')
# # list1.append(2)
# # list1.append(2/2)
# # list1.append((1,2,3,4))
# # print(list1)

# # # pop - удаляет элемент из списка по индексу и возращает этот удаленный элемент, если не указать индекс то он удалит последний элемент

# # list1 = [1,1,1,1,1,1,1,2,3,'ada', True]
# # pop_element = list1.pop(1) # 2
# # list1.pop()
# # print(pop_element)
# # print(list1)

# # # remove - удаляет элемент из списка по значение
# # list1.remove('ada')
# # print(list1)

# # # count - cчитает количество принятого элемента в списке
# # print(list1.count(1))

# # # index - возращает индекс первого вхождения элемента
# # list2 = [1,2,2,3, 'ada']
# # print(list2.index('ada'))

# # # insert - добавляет элемент в список по индексу
# # list2 = [1,2,4,5,6]
# # list2.insert(2, 3) # первый агрумент это индекс, а второй то что мы хотим добавить в список(элемент)
# # print(list2)

# # # extand - расширяет список засчет другого списка
# # list1 = [0,0,0]
# # list2 = [1,1,1]
# # # list1.append(list2)
# # list1.extend(list2)
# # print(list1)

# # # reverse - изменяет список, раставляя его элементы в обратном порядке
# # list1.reverse()
# # print(list1)

# # # sort - сортирует список, состоящий из элементов одного типа данных
# # # list1 = [ 3,4,5,11,1,13,23,32]
# # # list1.sort()
# # # print(list1)
# # # list1.sort(reverse=True)
# # # print(list1)
# # list2 = ['b', 'c', 'd', 'e', 'a', "A"]
# # list2.sort()
# # print(list2)

# # # clear - очищает список
# # print(list2)
# # list2.clear()
# # print(list2)

# # # copy - метод для копирования данных внутри списка
# # # list1 = [1,2,3]
# # # a = list1.copy()
# # # list1.append(4)
# # # print(a)
# # # print(list1)

# # # a, b, c = [1,2,3] # множественное присвоение
# # # name, age = input(), input()
# # # print(name, age)
# # # name = input()
# # # age = input()

# # # list1 = list('helloworld')
# # # print(list1)
# # # list2 = '-'.join(list1) # склеивание списка в строку
# # # print(list2)
# # # print(*list1) # распаковка списка

# # '''
# # На вход программе подается одно число n. Напишите программу, которая выводит список [1, 2, 3, ..., n].
# # n = 10
# # [1,2,3,4,5,6,7,8,9,10]

# # '''
# # n = int(input())
# # print(list(range(1,n+1)))

# # '===========================Tuple================================'
# # # Tuple (кортеж) - неизменяемый тип данных, упорядочен, индексируемый, итерируемый
# # '''
# # Кортеж является неизменяемым типом данных, что означает после создания кортежа его содержимое нельзя изменить
# # Упорядочен - это означает что порядок элементов в кортеже сохраняется
# # Индексируемый - что позволяет получить доступ к его элементам по индексу
# # Итерируемый - это означает, что мы можем перебрать все его элементы в цикле
# # '''
# # tuple_ = (1,2,3) # Кортеж
# # tuple_1 = () # Кортеж
# # tuple_2 = (1) #int
# # tuple_3 = (1,) #Кортеж
# # tuple_4 = 1, # Кортеж
# # print(type(tuple_4))
# # tuple_5 = tuple('helloworld')
# # print(tuple_5)
# # print(dir(tuple))


# # list1 = [(), (), (), (), ()]
# # for i in list1:
# #     print(type(i))


# # tuple_ = (1,2,3)
# # for i in range(3):
# #     print(tuple_[i])

spisok_name = ['Alina', 'Ainazik', 'Alena', 'Alex', 'Max']
print(' '.join(spisok_name))
spisok_surname = ['Ivanov', 'Maratov', 'Bekturov']
spisok_name.extend(spisok_surname)
print(spisok_name)
# # spisok3 = spisok_name + spisok_surname
# # print(spisok3)
# # print(spisok_name)
# # l = ['integer', 'float', 'string', 'list', 'loop', 'tuple', 'while', 'for']
# # index_ = l.index('loop')
# # print(l.pop(index_))
# # print(l)
# # count = 1
# # l = [1, 2, 5, 3]
# # for num in l:
# #     count *= num

# # print(count)
numbers = []
letters = []
s = 'Integers 1,2,3 Floats 44 Strings 5 Lists 10Tuples'
for elm in s:
    if elm.isalpha():
        letters.append(elm)
    elif elm.isdigit():
        numbers.append(elm)
print(numbers)
# words = ''.join(letters)
# print(words)
# #IntegersFloatsStringsListsTuples
# # c = []
# # for i in words:
# #     if i.isupper():
# #         c.append(words.index(i))

# # print(c)
# # new_words = []
# # next_ = 0
# # prev_ = 0
# # for index in c:
# #     next_ = index
# #     new_words.append(words[prev_:next_])
# #     prev_ = index
# # print(new_words)

# # print(' '.join(new_words))

# '''
# Дополните приведенный код так, чтобы элемент списка имеющий значение Green заменился на значение Зеленый, а элемент Violet на Фиолетовый. Далее необходимо вывести полученный список.
# '''
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[rainbow.index('Green')] = 'Зеленый'
# rainbow[rainbow.index('Violet')] = 'Фиолетовый'
# print(rainbow)
# '''
# Дополните приведенный код так, чтобы он вывел "перевёрнутый" список languages (т.е. элементы будут идти в обратном порядке).
# '''
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# languages.reverse()
# print(languages)
# print(dir(tuple))
my_list = [1, 2, 3, 4, 5]
deleted_element = my_list.pop(2)
print(deleted_element)  # Вывод: 3