from random import sample, choice
import sys
from time import sleep


def pair_verificator(value):
    value = value % 2
    if value == 0:
        return 'The number is a pair!'
    else:
        return 'The number is odd!'


count = 0  # this is for count the attempts

# randomize one number
list = (sample(range(0, 11), 1))

# choosing one number
number_selected = choice(list)


print('-*-' * 15)
print('Thinking about one number between 1 and 10. . .')
print('I GOT IT. Warning: You just have 3 attemps to hit the number.')
print('-*-' * 15)
sleep(1)


while True:
    print()
    tip = str(input('You wanna one tip? ')).upper()
    print()

    sleep(1)

    if tip == 'YES':
        print('Ok, i give you one tip!')
        print()
        print(pair_verificator(number_selected))
        break

    elif tip == 'NO':
        print()
        print('Ok, good luck trying without tip.')
        break

    print('Just YES/NO are gonna be accepted')

print()
print()

try_ = []  # attempts

while True:
    try:
        number_attempt = int(
            input(f'What number you are thinking? [{count + 1}] attempts '))

        count = count + 1

        if number_attempt != number_selected:
            print()
            try_.append(number_attempt)

            print()
            if len(try_) == 3:
                print('You reached the limit of attempts.')
                print(f'YOU LOSE, the number selected is {number_selected}!')
                sleep(5)
                sys.exit()

            if number_attempt < number_selected:
                print('Try a higher number.')
                print('Im with you, dont give up')
                print()
            elif number_attempt > number_selected:
                print('Try a lower number.')
                print('Not today, try again')
                print()

        else:
            print()
            print('YOU WON, you hit the correct number, congratulations!!!')
            print(
                f'After {count} attempts, you got it, the number is {number_selected}.')
            sleep(5)
            sys.exit()

    except ValueError:
        print('Just numbers going to be accepted.')
        print()
