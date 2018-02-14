import random

number = random.randint (1,10)
print ('Random number is: ', number)

guess = int(input('please enter your guess: '))
print ('you guessed: ', guess)

while number != guess:

    if guess < number:
        print ('Too low')
    elif guess > number:
        print ('Too high')

    guess = int(input('please enter your guess: '))
    print ('you guessed: ', guess)

print ('well done - you guessed it!')

