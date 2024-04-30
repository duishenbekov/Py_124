# zadanie1
# string1 = input('napiwite chto nibud: ')
# string2 = input('napiwite chto nibud: ')
# print(string1.lower(), string2.upper())
#zadanie2
# privet = True
# hi = str(privet)
# print(type(hi))
# print(str(privet))
# zadanie 3
# name = input("kak vas zovut? ")
# age = input("skolko vam let? ")
# movie = input('vaw lyubimiy film?')
# finish = f"Привет! {name}\nОтличный вкус фильма {movie} !"
# print(finish)
#zadanie 4 ne dodelal
# simvol = input("napiwite simvol: ")
# tekst = """Этот документ описывает соглашение о том, как писать код для языка python, включая стандартную библиотеку, входящую в состав python.
#           PEP 8 создан на основе рекомендаций Гуидо ван Россума с добавлениями от Барри. Если где-то возникал конфликт, мы выбирали стиль Гуидо.
#           И, конечно, этот PEP может быть неполным (фактически, он, наверное, никогда не будет закончен)."""
# new_teks = tekst.split(simvol)
# print(new_teks)
# #zadanie 5
# text = """Ключевая идея Гуидо такова: код читается намного больше раз, чем пишется. 
# Собственно, рекомендации о стиле написания кода направлены на то, чтобы улучшить читаемость кода и сделать его согласованным
# между большим числом проектов. В идеале, весь код будет написан в едином стиле, и любой сможет легко его прочесть."""
# text2 = text.replace('е', '5')
# print(text2)
#zadanie6
# text = """Пробелы - самый предпочтительный метод отступов.
# Табуляция должна использоваться только для поддержки кода, написанного с отступами с помощью табуляции.
# Python 3 запрещает смешивание табуляции и пробелов в отступах.
# Python 2 пытается преобразовать табуляцию в пробелы."""
# new_text2 = text.split()
# word = len(new_text2)
# print(word)
# zadanie7
# text = "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design."
# text2 = '|'.join(list(text))
# print(text2)
# zadanie8
# text = "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design."
# text2 = text.title()
# print(text2)
# zadanie 9
# text = input("kk dela?")
# text2 = text.upper()
# print(text2)
# zadanie 10
# text = "Dj(.=(.(,,,,,ango i,,s a hi,,,,gh-,.,.,.,.level Python( web framewor(.....k"
# text2 = text.replace('.', '')
# text3 = text2.replace(',', '')
# text4 = text3.replace('(', '')
# print(text4)
# # zadanie11
# text = input("vvesti tolko bukvy")
# text2 = text.isalpha()
# if text2:
#     print(text.lower())
#     print('vse verno')
# else:
#     print("")
# zadanie12
# text = input("vvesti tolko celoe chislo")
# if text.isdigit():
#     print((int(text) * 2) ** 3)
# else:   
#     print("vvediete chislo")
# zadanie13
# slovo = input('Vvedite vawe slovo: ')
# palindrom = slovo[::-1]
# print(palindrom)
# if slovo == palindrom:
#     print("chetko")
# name = input("name")
# last_name = input("lastname")
# fio = f'Hello {name} {last_name}! You have just delved into Python'
# print(fio)

# a = 'Bishksfafek'
# b = 'Osh'
# c = 'Nafdasfasffsryn'
# a2 = len(a)
# b2 = len(b)
# c2 = len(c)
# if b2 < a2 > c2:
#     print(a2)
# elif a2< b2 >c2:
#     print(b2)
# else:
#     print(c2)

# number = int(input("napiwite chisla: "))
# number2 = int(input("napiwite chisla: "))
# number3 = int(input("napiwite chisla: "))
# number1 = len(number)
# number22 = len(number2)
# number33 = len(number3)
# summary = (number2 + number3) / 2 *