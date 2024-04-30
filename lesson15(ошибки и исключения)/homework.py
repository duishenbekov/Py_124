'zadanie 1'
# try:
#     num1 = int(input("napiwite1 "))
#     num2 = input("napiwite2")
#     print(f'{num1}{int(num2)} = {num1 + int(num2)}')
# except TypeError:
#     print('ошибка в типах данных')

'zadanie2'
# try:
#     with open('/Users/IT/Desktop/ada3/lesson15(ошибки и исключения)/zadanie2.txt', 'r') as f:
#         for num in f.read().split():
#             try:
#                 digit = int(num)
#                 print(digit)
#             except ValueError:
#                 print("ne poluchilos' ".format(num))
# except FileNotFoundError:
#     print()

'zadanie 3'
# def func_act():
#     try:
#         with open('/Users/IT/Desktop/ada3/lesson15(ошибки и исключения)/zadanie2.txt', 'r') as f:
#             bukva_w = f.read()
#             if 'w' in bukva_w:
#                 print(f"vse chetko est' bukava w")
#             else:
#                 print('netu')
#     except FileNotFoundError:
#          print("netu takoi faila")
# print(func_act())

'zadanie 4'
# try:
#     with open('/Users/IT/Desktop/ada3/lesson15(ошибки и исключения)/zadanie2.txt') as f:
#         reading = f.read()
#         name = input("введите ваше имя")
#         age = int(input("your age"))
#         country = input("are you from?")
#     with open('/Users/IT/Desktop/ada3/lesson15(ошибки и исключения)/zadanie2.txt', 'w') as f:
#         f.write(reading)
#         f.write(f'name:{name} age:{age}, country:{country}')
#         print(f)
# except Exception as error:
#     print("age napisano nepravilno{error}")

'zadanie 2 rewenie Anton'
# try:
#     with open ('file.txt') as file:
#         content = file.read().replace('\n', '')
#         numbers = [int(i) for i in content]
# except ValueError:
#     print('nevozmojno preobrazovyvat')
# except FileNotFoundError:
#     print('Takogo faila ne suwestvuet')
# else:
#     print(f'summa vseh cifr v fail: {sum(numbers)}')

'zadanie 5'

# def name_age(*args, **kwarks):
#     name = kwarks["name"]
#     age = kwarks['age']
#     print(f'name:{name}, age: {age}')
# try:
#     name_age(name = 'anton', age = 25)
#     name_age(name = 'denis')
# except KeyError as error:
#     print('takogo klyucha netu')

'zadanie 6'
# def add (a,b):
#     return a + b
# def substrct (a,b):
#     return a - b
# def divide (a,b):
#     return a / b
# def multiply (a,b):
#     return a * b
# try:
#     num1 = int(input("vvedite chislo: "))
#     num2 = int(input("vvedite chislo: "))
#     print(add(num1, num2))
#     print(substrct(num1, num2))
#     print(divide(num1, num2))
#     print(multiply(num1, num2))
# except ValueError:
#     print('vvedite chislo')
# except ZeroDivisionError:
#     print("na nol' delit' nel'zya")

'zadanie 7'
# l1 = [2, 3, 0, 1]
# l2 = [10, 20, 30, 40]
# try:
#     result = []
#     for ind in l1:
#         elem = l2[ind]
#         result.append(elem)
# except IndexError as error:
#     print(error)
# else:
#     print(result)


try:
    text = input('vvedite lyuboi text')
    text_index = int(input("vvedite index"))
    print(text[text_index])
except IndexError as error:
    print(error)
    



