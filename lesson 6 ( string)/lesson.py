# '''# '==================================String=================================='
# # строки - это неизменяемый тип данных, который предназначен для хранения текста
# # (последовательности символов), заключенного в одинарные или двойные кавычки

# # string1 = 'строка с одинарными кавычками'
# # string2 = " строка с двойными кавычками"

# # # string3 = "Don't" #одинарные кавычки внутри двойныз являются символом
# # print(string3)
# # string4 = 'Petter is "strong" man'
# # print(string4)
# # string5 = 'Petter isn\'t "Strong" man' # обратный слеш подсказывает 
# # python что после него идет символ кавычки
# # print(string5)
# # #Литералами строк являются как одинарные кавычки так и двойные.
# # "===============================Экранизация строк=========================="
# # '\n' # переносит на новую строку
# # stirng = 'Ada courses\nThe better courses'
# # '\t' # табуляция
# # print('hello\tworld')
# #  '\' #отображение кавычки
# # "\" #отбражение двойных кавычек
# # "\\" #отображение одного слеша
# # print('https:\\www.google.com', '\\desktop\\ada')
# # '\v' # перенос строки на новую со смещение вправо на длину предыдущей
# # "\r"
# # string7 = 
# # Многострочный текст 
# # в одинарных кавычках тут
# # можно ставить любые кавычки'''

# # '=================================форматирование строк==================================='
# '''title = 'Iphone 13'
# price = 900
# format1 = f'Название: {title}\nЦена: {price}'
# # print(format1)
# format2 = 'Название: {}\n Цена: {}'
# print(format2.format('хлеб', 15))
# print(format2.format(title, price))
# format3 = 'название: %s\nЦена:%s'
# print(format3 % (title, price))

# '========================================Конкатенация======================================='
# # Конкатенация - это операция сложения двух строк
# string8 = 'hello' + 'world'
# print(string8)
# string9 = 'hello' + 'world' * 2
# print(string9)
# '======================================индексы============================================='
# #индексы = порядковый номер элемента в последовательности (символ строке) и начинается индекс с  нуля:
# 0, 1, 2, 3 . . . 
# индексы указывают в квдратных скобках string[0] - доступ к первому элементу
# '''
# # h e l l o  w o r l d
# # 1 2 3 4 5  6 7 8 9 10
# #               -3  -2 -1
# '''
                     
# string = 'hello world'
# срезы строк - это опреленная часть строки
# string[start:end:step]
# print(string[0:5]) показывается первый 5 символов
# print(string[0:5:2]) пропустит каджый 2 символ
# print(stirng[::-1]) # переворачивает всю строку
# print(string[-2:]) выведит  только последние 2 символа
# print(string[:]) vyvedit vse symvoly


# '=================================методы строк =================================='
# #Методы - это функции которым относятся к определенному классу(типу данных)
# к ним обращаемся через точку
# # функция type - подскажет какой тип данных у нас хранится 
# print(type('123'))
# # функции dir - подскажет все методы нащего типа данных
# print(dir(str)) посмотрит все методы string
# string = 'Hello world'
# upper_string = string.upper()#все большие буквы
# # print(upper_string)
# print(string.lower()) # все буквы маленькми буквами 
# print(string.swapcase())# menyaet registry vseh bukv
# print(string.title()) # каждое новое слово булет с большой буквы а остальные с маленькими
# print(string.capitalize()) # делает  первую букву с большой  а остальные слова с маленькими
# print(string.count(L)) # считает символы
# print(string.startswith('he')) #проверка начинается ли строка с заданных символов
# print(string.endswith('he')) #проверка заканчивается ли строка с заданных символов
# print(string.isupper()) # proveryaet vseh simvolov na verhnem registre
# print(string.islower()) # proveryaet vseh simvolov v nijnem registre
# print(string.isdigit()) # proverk yavlyaetsya li storka chislovoi
# print(string.isalpha()) # proverk yavlyaetsya li storka bukvami
# print(string.isalnum()) # proverk yavlyaetsya li storka bukvami chislami ili vse vmeste
# print(string.split()) # razdelitel' 
# print('*'.join(string.split)) # skleivat
# print(string.replace('L', '')) # MENYAET VSE SIMVOLY UKAZANYM VTORYM '''
# ''''''
print(dir(str))