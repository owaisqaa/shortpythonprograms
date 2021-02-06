import random

print('I am thinking in a number between 1 and 20')
machinenum = random.randint(1, 20)

#ask player to guess 5 times
for num in range(1, 6):
    print('Take a guess')
    number = int(input())

    if number < machinenum:
        print('Your guess is low')

    elif number > machinenum:
        print('Your guess is high')

    else:
        break

if number == machinenum:
    print('Good Job! You guessed my number in ' + str(num) + ' Times')
else:
    print('Nope the number i was thinking of is ' + str(machinenum))