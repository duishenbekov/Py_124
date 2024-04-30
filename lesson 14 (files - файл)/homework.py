# data = input('napiwi') 
# file = open('lesson 14 (files - файл)/test.txt', 'a') # функция аппенд добавляет уже к существующему тексту и не удаляет
# file.write(data + '\n')
# file.close()

# file = open('lesson 14 (files - файл)/test2.txt', 'r')
# # print(file.read(1)) #сколько символов нужно вывести
# for line in file:
#     print(line, end= '')

# file.close()
'zadanie1'
# file = open('lesson 14 (files - файл)/test4.txt', 'w')
# file.write('salam aleikum')
# file.close()
# file = open('lesson 14 (files - файл)/test4.txt')
# print(file.read())
# file.close()

'zadanie 2'
# login_password = input("напишите логин и пароль: ")
# file = open('lesson 14 (files - файл)/users.txt', 'w')
# file.close()
# file = open('lesson 14 (files - файл)/users.txt', 'a')
# file.write(login_password)
# print(file)
# file.close()

'zadanie 3'
# def main():
#     with open('lesson 14 (files - файл)/users.txt', 'r') as file:
#         content = file.read() #sporsit' pochemu nujno sozdavat' novuyu per.
#         if 'w' in content:
#             print('bukwa w')
#         else:
#             print("netu")
# main() 
'zadanie 4'
# text = 'fhufoooooojalewkfhkajefk'
# with open('lesson 14 (files - файл)/users.txt', 'w') as file:
#     file.write(text)

# with open('lesson 14 (files - файл)/users.txt') as file:
#     text = file.read()
#     words = text.split()
#     print(words)
#     o_words = [word.count('o') for word in words if 'o' in word]
#     print(o_words)
#     print(sum(o_words))

'zadanie 5'
# text = """
# .detacilpmoc naht retteb si xelpmoC
# .xelpmoc naht retteb si elpmiS
# .ticilpmi naht retteb si ticilpxE
# .ylgu naht retteb si lufituaeB
# """

# with open ('lesson 14 (files - файл)/users.txt', 'w') as file:
#     file.write(text)
# with open('lesson 14 (files - файл)/users.txt', 'w') as file:
#     lines = file.readlines()
#     print(lines)
#     reverse_list = []
#     for i in lines:
#         reverse_list.append


'zadanie 6'

text = """
123
aaa456
fxdya 5 0 0
"""
# with open ('/Users/IT/Desktop/ada3/lesson 14 (files - файл)/test3.txt', 'w') as file:
#     file.write(text)
with open ('/Users/IT/Desktop/ada3/lesson 14 (files - файл)/test3.txt', 'r') as file:
    lines = file.readlines()
    spisok = []
    for line in lines:
        stroka = ''
        for number in line:
            if number.isdigit():
                stroka += number
        print(stroka)
        if stroka.isdigit():
            spisok.append(int(stroka))
            print(spisok)
    print(sum(spisok))  
    # spisok = [int(''.join([simvol for simvol in line if simvol.isdigit()])) for line in lines]
    # print(sum(spisok))