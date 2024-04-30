import random

def welcome():
    name = input('Привет! Как тебя зовут? ')
    play = input(f'{name} хочешь сыграть в игру Угадай число? (да\нет) ')
    if play.lower() == 'да':
        return (True, name)
    else:
        return (False, name)

def gameplay():
    number_guess = random.randint(1,100)
    attempts = 0
    while True:
        guess = int(input('Угадай число от 1 до 100: '))
        attempts += 1
        if guess < number_guess:
            print('Больше!')
        elif guess > number_guess:
            print('Меньше!')
        else:
            print(f'Поздравляю! Ты угадал число {number_guess} за {attempts} попыток')
            return attempts

def play_again():
    again = input("Хочешь сыграть еще раз (да\нет) ")
    if again.lower() == 'да':
        return True
    else:
        return False

def main():
    while True:
        play_game, name = welcome() # true or false, name
        if not play_game:
            print(f'До свидания {name}!')
            break
        attempts = gameplay()
        play_more = play_again()
        if not play_more:
            print(f'До свидания {name}!')
            break

main()
