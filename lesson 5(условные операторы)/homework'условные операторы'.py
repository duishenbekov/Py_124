# num1 = 2 ** 3
# num2 = 3 ** 2
# if num1 < num2:
#     print(num2)
# elif num1 > num2:
#     print(num1)
# 2 zadanie
# number = int(input("number: "))
# if number >= 0 and number <= 21 or number >= 57 and number <= 100:
#     print("chislo razreweno")
# else:
#     print("chisle zapreweno")
# zadanie 3 ne dodelal
# number = int(input("nomer"))
# if number % 2 == 0:
#     print("четное число")
# elif number % 2 > 0:
#     print("nechetnoe chislo")
# if number % 3 == 0:
#     print("delitsya na 3 bez ostatka")
# else:
#     print("delitsya na 3 s ostatka")
# if number ** 2 > 1000:
#     print("chislo v kvadrate bol'we 1000")
# else:
#     print("chislo v kvadrate men'we 1000")
# zadanie 4
# number = int(input("napiwite svoi vozsrast: "))
# if number <= 17:
#     print("для вашего возвраста надо учиться и получать знания")
# elif number <= 25:
#     print("вам надо выбрать профессию: ")
# elif number <= 50:
#     print("vam nado rabotat': ")
# else:
#     print("otdyhayte i ne volnutes'")
# number = input()
# if number or not number:    
#     print('asdd')
#zadanie 5
# a = 10//5
# b = 10/5
# if a == b:
#     print(a + b)
# else:
#     print("oni ne ravny")
# zadanie 6
# a=10
# b=5
# if a > 0 and b > 0:
#     print("da")
# zadanie7
# a = 10
# b = 5
# if a > b:
#     print(a + 2, b +2)
# zadanie8
# num = int(input("chislo: "))
# if num > 0:
#     print("polojitel'noe chislo")
# elif num < 0:
#     print("otricatelnoe chislo")
# else:
#     print("0")
# zadanie9
# age = int(input("napiwite svoi age: "))
# if age >= 18 and age <= 119:
#     print('soverwenaltniy')
# elif age <= 4 and age >= 1:
#     print("rebenok")
# elif age <= 0 or age >= 120:
#     print("Недопустимый возраст!")
# else:
#     print("ne soverweletniy")
# zadanie10
# a = 45
# b = 6
# if a / b:
#     print("a delitsya na b tolko s otatkom 7,5")
# zadanie11
# year = int(input("god "))
# if year == 2024:
#     print("tekuwii god")
# elif year == 2023:
#     print("fod prowel")
# else:
#     print("cherez odin god")
# ЗАДАНИЕ 12
# a = 5
# b = 4
# c = 4
# if a > b and a > c:
#     print("a bol'we vseh")
# elif b > a and b > c:
#     print("b bol'we vseh")
# elif c > a and c > b:
#     print('c bolwe vseh')
# min_number = min ((a,b,c))
# max_number = max((a,b,c))
# print('samoe bolwe', max_number)
# print("samoe min", min_number) 
# zadanie 13
# num1 = 17391 % 17 
# num2 = 546 % 17
# num3 = 934 % 17
# min_number = num1 if num1 < num2 and num1 < num3 else num2 if num2<num1 and num2 < num3 else num3
# print(min_number)
# if num1 < num2 and num1 < num3:
#     print("men'we num1")
# elif num2 < num3 and num2 < num1:
#     print("men'we num2")
# elif num3 < num2 and num3 < num1:
#     print("men'we num3")
#  ЗАДАНИЕ 14
# x = 13 ** 2
# x2 = x ** 2
# if x2 < 172:
#     x3 = x2 ** 2    
#     print(x3)
# print(x2)
#     print('oni ravny')
# elif x ** 2 == x2:
#     print("posle vozvedenie vo 2 raz v stepen' oni stali ravny")
# 15 zadanie
# a = int(input("napiwite chislo: "))
# if a % 6 == 0:
#     print("delitsya bez ostatka na 6")
# else:
#     print('ostaetsya ostatok')
# ZADANIE 16
# a = int(input("napiwite chislo"))
# b = int(input("napiwite chislo"))
# c = int(input("napiwite chislo"))
# summary = a + b + c
# if summary > 10:
#     print("yes")
# else:
#     print("no")
#zadanie 17
# login = input("login: ")
# password = input("vvedi parol': ")
# if password == 'Tilek123' and login == "Admin"
#     print("vy uspewno avtorizovalis'")
# else:
#     print("Parol' neverniy")
# zadanie 18
# a = int(input("chislo 1: "))
# b = int(input("chislo 2: "))
# result = int(input("skolko u vas poluchilos': "))
# summary = a * b
# if summary == result:
#     print("otvet pravilniy: ", summaary)
# else:   
#     print( a, '*', b, '=', summary)
# zadanie 19
# month = int(input("napiwite chislo: "))
# if month == 1 or month == 2 or month == 12:
#     print("За окном падал белый снег")
# elif month in (3, 4, 5):
#     print("Птицы пели прекрасные песни")
# elif month in (6, 7, 8):   
#     print("Солнце светило ярче чем когда-либо")
# elif month > 8 and month < 12:
#     print("Урожай был невероятным")
# else:
#     print("Такого месяца не существует")
# zadanie 20
# a = int(input("chislo a: "))
# if a > 0 and a < 5:
#     print("Verno")
# else:
#     print("ne verno")
# zadanie 20 тернартрый оператор
# a = int(input("kjndsf"))
# verno = "verno" if a > 0 and a < 5 else "neverno"
# print(verno)
# zadanie 21
# a = int(input("napiwi chislo dlya a: "))
# b = int(input("napiwi chislo dlya b: "))
# if a <= 1 and b >= 3:
#     print(a + b)
# else:
#     print(a - b)
# zadanie 22
# a = int(input("napiwi chislo dlya a: "))
# b = int(input("napiwi chislo dlya b: "))
# verno = "verno" if a > 2 and a < 11 or b >= 6 and b < 14 else "neverno"
# print(verno)
# zadanie 23
# month = int(input("napiwite chislo: "))
# if month == 1 or month == 2 or month == 12:
#     print("zima")
# elif month > 2 and month < 6:
#     print("vesna")
# elif month > 5 and month < 9:   
#     print("leto")
# elif month > 8 and month < 12:
#     print("osen'")
# else:
#     print("Такого месяца не существует")
# zadanie 24 ne dodelal
# number_apt = int(input("napiwite nomer kv: "))
# if number_apt > 0 and number_apt < 21:
#     print("1 подьезд")
# elif number_apt >= 21 and number_apt < 49:
#     print("2 подьезд")
# elif number_apt >= 49 and number_apt <= 90:
#     print("3 подьезд")
# else:
#     print("такой квартиры нету")
# zadanie 25
# finger = int(input("порядковый номер пальца"))
# if finger == 1:
#     print("bol'woi palce")
# else:
#     if finger == 2:
#         print("ukazatel'niy")
#     else:
#         if finger == 3:
#             print("sredniy palec")
#         else:
#             if finger == 4:
#                 print("bezymyaniy palec")
#             else:
#                 if finger == 5:
#                     print("mizinec")
#                 else:
#                     print("net")
# zadanie 26
# num = int(input("polojitel'noe chislo: "))
# if num % 2 == 0 and num % 4 == 0 and num % 6 == 0:
#     print("delitsya bez ostatka")
# else:
#     print("ne delitsya")
# zadanie 27
# a = int(input("napiwite chislo: "))
# b = int(input("napiwite chislo: "))
# c = int(input("napiwite chislo: "))
# if a + b > c and b + c > a and c + a > b:
#     print("validniy")
# else:
#     print("nevalidniy")
# zadanie 28 ne sdelal

# zadanie 29
# romawka = int(input(" kolichestvo lepestkov"))
# if romawka % 2 > 0:
#     print('lyubit')
# else:
#     print("ne lyubit")
# zadanie 30
# celcius = int(input("напиши градус по фаренгейту: "))
# fahrenheit = int(input("напиши градус по фаренгейту: "))
# fahrenheit = (fahrenheit - 32) * 5 / 9
# celcius = celcius * 9 / 5 + 32
# print("послк конвертация фаренгейта в фаренгейт:  ", celcius)
# print("послк конвертация фаренгейта в цельсию:  " , fahrenheit)
