from random import randint

number = randint(1, 20)
guess = 0

while guess != number:
    print('I am busy thinking of a number, can you guess it…?')
    guess = int(input('Guess the number between 1 and 20: '))
    if guess > number:
        print('Too high')
    elif guess < number:
        print('Too low')

print('Congratulations, you’ve guessed it')