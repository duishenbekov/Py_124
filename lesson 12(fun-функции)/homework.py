# 'zadanie1'
# def numebrs():
# num = {input('napiwite 5 chisel')}
    
# print(min(set(num)))
# set1 = min({int(value) for value in input().split()})

'zadanie 2'
# zaim = int(input('min 100_000:'))
# kredit = zaim * (7.89 / 100)
# print(round(kredit, 2))

'zadanie 3'
# tekst = input("napiwite tekst s cifrarami")
# numbers = [ i for i in tekst if i.isdigit()]
# if numbers:
#     print(int(numbers))
# else:
#     print("cifr ne bylo")

# for i in tekst:
#     if i.isdigit():
#         print(i)
'zadanie4'

# def count_days():
#     years = int(input('let: '))
#     month = int(input('mesyac: '))
#     print(f'{years}let i {month} mesyacy preobrazuem v dni {(years * 12 + month)* 30 } stolko dnei')
# count_days()
'zadanie5'
# def build_dict():
#     keys_ = {i: i**3 for i in range(1, 10+1)}
    
#     # for i in range(1, 10+1):
#     #     keys_[i] = i ** 3
#     print(keys_)
# build_dict()

'zadanie6'
# def counting():
#     number = []
#     for i in range (1, 51):
#         number.append(i)
#     print(sum(number))
# counting()
# total_sum = sum(range(1, 51))
# return total_sum


'ZADANIE 1'
# def ask_number():
#     num2 = set()
#     for i in range(1,5):
#         number = int(input("chislo napiwite"))
#         num2.add(number)
#         min_number = min(num2)
#     return num2, min_number
# print(ask_number())
# def ask_number():
#     num = {int(input("napiwite chislo")) for i in range(4)}
#     min_number = min(num)
#     return min_number, num
# print(ask_number())

'zadanie2'
# def find_procent(kolichestvo):
#     kredit = kolichestvo * (7.89 / 100)
#     print(round(kredit, 2))


# find_procent(100000)

'zadanie3'
# def find_numbers(tekst):
#     number = []
#     for i in tekst:
#         if i.isdigit():
#             number += i
#     print(number)


# find_numbers('sklenf;slnef1e21321')

'zadanie 4'
# def count_days(years, month):
#     print(f'{years}let i {month} mesyacy preobrazuem v dni {(years * 12 + month)* 30 } stolko dnei')


# count_days(month = 23, years = 4)

'zadanie new 1'

# def new_func(firth):
#     middle_index = len(firth) // 2
#     list1 = firth[:middle_index]
#     list2 = firth[middle_index:]
#     list1_reversed = list1[::-1]
#     list2_reversed = list2[::-1]
#     list3 = list1_reversed + list2_reversed
#     return list3


# list_1 = ['python', 'Django', '3.11', '4']
# change_list = new_func(list_1)
# print(change_list)

'zadanie2'
# def new_func(list_):
#     middle_index = len(list_) // 2
#     list1 = list_[:middle_index]
#     list2 = list_[middle_index:]
#     list1_reversed = list1[::-1]
#     list2_reversed = list2[::-1]
#     list_finish = list1_reversed + list2_reversed
#     return list_finish

# list_1 = ['python', 'Django', '3.11', '4']
# change_ = new_func(list_1)
# print(change_)

'zadanie3'
# def gen_number(kod):
#     import random
#     string_ = ''
#     numbers2 = 5, 6, 8, 0, 3, 4
#     for i in range(6):
#         gen_number = str(random.choice(numbers2))
#         string_ += gen_number
#         finish = kod + string_
#     return finish


# numbers = ('0888')
# full_numbers = (gen_number(numbers))
# print(full_numbers)

'zadanie 4'
# def add(a, b):
#     return a + b
# def substract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     if b == 0:
#         print("na nol' delit' nel'zya")
#     else:
#          return a / b


# numbers = 2, 3
# rewenie = add(*numbers)
# rewenie2 = substract(4, 6)
# rewenie3 = multiply(*numbers)
# print(rewenie)
# print(rewenie2)
# print(rewenie3)
# print(divide(*rewenie4))

'zadanie 5'
# def count_letter(text):
#     counter = 0
#     for i in text:
#         counter += 1
#     return counter


# text = "234iu2o3jrksjnlfei798124!"
# counter1 = count_letter(text)
# print(counter1)

database = [
    {'name': 'user1', 'password': 12345},
    {'name': 'user2', 'password': 12345},
    {'name': 'user3', 'password': 12345},
]

def in_database(name):
    for user in database:
        if user['name'] == name:
            return True
    return False


def register_database(name, password1, password2):
    if in_database(name):
        return 'Пользователь с таким именем уже существует'
    if password1 != password2:
        return "Пароли не совпадают"
    user = {'name': name, 'password': password1}
    database.append(user)
    return 'Вы успешно зарегистрированы!'


def login_database(name, password):
    if not in_database(name):
        return 'Пользователь не найден'
    for user in database:
        if user['name'] == name:
            if user['password'] != password:
                return "Неверный пароль"
            return 'Вы успешно вошли'
        

def main():
    print('Добро пожаловать!')
    while True:
        action = input('Введите: 1 для регистрации, 2 для входа, 3 для выхода: ')
        if action == '3':
            break
        elif action == '1':
            name = input('Введите имя пользователя: ')
            password1 = input('Введите пароль: ')
            password2 = input('Повторите пароль: ')
            print(register_database(name, password1, password2))
        elif action == '2':
            name = input('Введите имя пользователя: ')
            password = input('Введите пароль: ')
            print(login_database(name, password))
        else:
            print('Некорректный выбор')
# main()
        


'''
ТЗ “Угадай число”

Напишите мини-проект “Угадай число”. Для
этого, вам понадобиться стандартный
ввод/вывод данных, тип данных числа и
условные операторы. Также не забудьте
использовать библиотеку random.
Требования:
1. Ваша программа должна запрашивать
имя пользователя. Программа должна
запросить у пользователя хочет ли он
играть или нет. Если ответ будет ‘нет’, то
программа должна завершиться.
2. Далее пользователь должен угадать
число. Также вы должны сделать счетчик
попыток, и показать пользователю сколько
попыток ему потребовалось, чтобы отгадать
число.
3. Если пользователь угадал число,
запросить у него хочет ли он пройти игру
еще раз, если ответ будет “нет”, программа
должна завершиться'''

# def text_count(text):
#     simvol = 0
#     for i in text:
#         # if i == str:
#         simvol +=1
#     return simvol

# print(text_count(text =input('Введите ваш текст:')))
# import random
# number = random.randint(1, 30) 
# name = input('Привет! Как тебя зовут?: ') 
# print ('Отлично', name,  'отгадай число между 1 и 30. Будешь играть? Если да,то продолжим!') 
# otvet = input('Твой ответ?:')
# while otvet == 'да':
#     print('Отлично, продолжим!')
#     guesses = 0  
#     while guesses < 4:
#         guess = int(input('Введи число: ')) 
#         guesses += 1 
#         if guess < number:
#             print ('Твое число меньше моего,', name, ",Еще попытка?")

#         if guess > number:
#            print ('Твое число больше моего,', name, ",Еще попытка?")
#         if guess == number:
#             break
#     if guess == number:
#         print ('Вау! Ты везунчик. Ты угадал с', (guesses), 'попыток!!!')
#         break
#     else:
#         print ('Ты не угадал,', name, ' Я загадал число',( number))
#         idem_dalwe = input('Еще играем?:')
#         if idem_dalwe == 'да':
#             continue
#         else: 
#             break 
# if otvet == 'нет':
#     print("Хорошо", name, "Увидимся")
# else:
#     print('Не понял твой ответ, попробуй еще раз')

# import random
# def welcom():
#     name = input('privet, kak tebya zovut? ')
#     play = input(f'{name} hochew sygrat v igru ugadai chislo? (da/net)')
#     if play.lower()== 'da':
#          return True, name
#     else:
#         return False, name
# def gameplay():
#     number_guess = random.randint(1, 100)
#     attempts = 0
#     while True:
#         guess = int(input('Ugadai chislo ot 1 / 100: '))
#         attempts += 1
#         if guess < number_guess:
#             print('bolwe')
#         elif guess > number_guess:
#             print('menwe')
#         else:
#             print(f'ty ugadal chislo {number_guess} i kolichestvo popytok{attempts}')
#             return attempts


# def play_again():
#     again = input("hochew' sygrat' ewe raz da/net")
#     if again.lower() == 'da':
#         return True
#     else:
#         return False


# def main():
#     while True:
#         play_game,  name = welcom()
#         if not play_game:
#             print(f'dosvidaniya {name}')
#             break
#         attempts = gameplay()
#         play_more = play_again
#         if not play_again:
#             print(f'dosvidaniya {name}!')
#             break
# main()


'kamen nojnicy bumaga'
import random
def start():
    name = input("Привет! Как я могу обрашться к Вам? ")
    choise = input(f"{name}, давайте сыграем в игру? (да или нет) ")
    if choise == 'да':
        return True, name
    elif choise == 'нет':
        return False, name


def gameplay():
    attemps = 0
    while attemps <= 2:
        slova = ['бумага', 'камень', 'ножницы']

        robot_choice = random.choices(slova)
        print(f'Robot choice {robot_choice}')

        chelovek_choice = input(f'{slova}: ')
        
        attemps += 1

        if (chelovek_choice == 'бумага' and robot_choice == 'камень') or (chelovek_choice == 'ножницы' and robot_choice == 'бумага') or (chelovek_choice == 'камень' and robot_choice == 'ножницы'): 
                print(f"vy pobedili {attemps} raund")
        elif (robot_choice == 'бумага' and chelovek_choice == 'камень') or (robot_choice == 'ножницы' and chelovek_choice == 'бумага') or (robot_choice == 'камень' and chelovek_choice == 'ножницы'): 
                print("robot_choice pobedil")
        else:
            print(f"robot_choice vybrl {robot_choice}, chlovr vybral {chelovek_choice} vy vybrali odinakovye")

def again():
    again_ = input('hotite snova sygrat? да/нет')
    if again_ == 'да':
        return True
    else:
        return False

def main():
    while True:

        agreement, name = start() # True, Arstan
        if not agreement:
            print(f'do svidaniya {name}!')
            break
        gameplay()
        play_more = again()
        if not play_more:
            print(f'spasibo za igru {name}')
            break
main()

