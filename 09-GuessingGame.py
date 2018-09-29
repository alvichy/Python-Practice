# Guessing Game
# Program a random number, allow user input until correct number
# Have number of tries
import random

print('Guessing Game\n')


def guessing_game():
    num = random.randint(0, 20)
    count = 0
    guess = None

    while guess != num:
        guess = int(input('Guess a number between 0 and 100: '))
        if guess > num:
            print('Too High')
            count += 1
        elif guess < num:
            print('Too Low')
            count += 1
        else:
            count += 1
            print(f'\nYou got the right number. it only took you {count} goes.\n')
            play()


def play():
    game = input('Play Again? E[X]IT ').strip().lower()
    if game != 'x':
        guessing_game()
    elif game == 'n':
        print('GAME OVER!')


guessing_game()
