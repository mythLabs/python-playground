import random

print('Hello, whats your name ?')
name = input()

secretNumber = random.randint(1,20)

print('Well, '+ name + ', guess number between 1 and 20')

for count in range(1,7):
    print('make a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is low')
    elif guess > secretNumber:
        print('Your guess is high')
    else:
        break

if guess == secretNumber:
    print('good job')
else:
    print('Better luck next time')