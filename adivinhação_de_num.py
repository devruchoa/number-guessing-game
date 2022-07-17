import random 
import math

print('Hey! Welcome to my game! In this game you will tell me a range of numbers, and then I will think of one of them... Can you guess which one it is?')

major = int(input('Enter the upper limit: '))
minor = int(input('Enter the lower limit: '))

number = random.randint(minor, major)

attempts = math.log(major - minor + 1, 2)
print(f'Okay... for the time you gave me I can offer you {int(attempts)} attempts!')

counter = 0

while counter < attempts:
    counter += 1

    attempt = int(input('Your attempt: '))

    if number == attempt:
        print(f'Congratulations you did it in {counter} attempts!')

        break
    elif number > attempt:
        print("You guessed too small!")
    elif number < attempt:
        print("You Guessed too high!")    
if counter >= attempts:
    print(f'\n The number is {number}')
    print('\nBetter luck next time!')        

