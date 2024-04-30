# zadanie1
# hello = (1, 2, 3, 4, 5)
# hello_list = list(hello)
# print(hello_list)
# zadanie2
# tuple_1 = (1, 2, 3)
# list1 = list(tuple_1)
# print(list1[0])
# print(list1[1])
# print(list1[2])
# zadanie3
# list1 = [1, 'privet', 1.2, (1,), [1,2,3]]
# print(list1)
# zadanie4
# list1 = ['arstan', 'tilek', 'bektru', 'chyngyz', 'omar']
# list2 = ' '.join(list1)
# print(list2)
# zadanie5
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# # list3 = list1 + list2
# # print(list3)
# list2.extend(list1)

# print(list2)
# zadanie6
# l = ['Sanjar', 'Tilek', 'Kalys', 'Eldar', 'Elina', 'Beka', 'Elzar', 'Bael', 'Atajan', 'Emir', 'Mamed', 'Beka']
# name = l.count('Beka')
# print(name)

# zadanie7
# l.remove('Elina')
# print(l)
# zadanie8
# my_list3 = real_info.copy()
# print(my_list3)

# aidana = []
# tilek = ['ya tebya lyublyu']
# aidana = tilek.copy()
# aidana2 = [1,2,2,2,2,2]
# tilek2 = [:]
# print(tilek2)
# print(aidana)
# print(aidana)
# zadanie9
# l = ['integer', 'float', 'string', 'list', 'loop', 'tuple', 'while', 'for']
# index_loop = l.index('loop')
# delete_loop = l.pop(index_loop)
# print(l)
# zadanie10
# i = 1
# l = [1, 2, 5, 3]
# for num in l:
#     i *= num  
# print(i)
# 11) Взять строку №1 создать два списка numbers и letters, пройтись по каждому 
# элементу строки No1 и в numbers добавлять только числа, а в letters буквы.
# list1 = []
# num = []
# s = 'Integers 1,2,3 Floats 44 Strings 5 Lists 10Tuples'
# for elm in s:
#     if elm.isalpha():   
#         list1.append(elm)
#     elif elm.isdigit():
#         num.append(elm)
# print(num, list1)
# print(''.join(list1))
# print(''.join(num))
# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# summa = (sum(evens))
# dlinna = len(evens)
# print(f'{summa} / {dlinna} = {summa /dlinna}')
# green = 'зеленый'
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# index_green = rainbow.index('Green')
# delete1 = rainbow.pop(index_green)
# print(index_green)
# print(rainbow)
integer = [1, 2, 3, 4, 5, 6 ,7, 8, 9]
int_ = int(integer)
for i in range(int_):
    i % 2 == 0
print(int_)




