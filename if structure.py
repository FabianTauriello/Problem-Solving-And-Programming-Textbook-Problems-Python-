# working on an if statement with a random number

import random

random_no = random.randint (1,10)
print ('random number is: ', random_no)

user_guess = int(input('guess a number between 1 and 10: '))
print ('you guessed: ', user_guess)

if random_no == user_guess:
    print ('well done old chap')
elif user_guess < random_number:
    print ('too low')
elif user_guess > random_number:
    print ('too high')

print ('done')

	

