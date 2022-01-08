def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


try:

    number = collatz(int(input('Enter Number:\n')))
    print(number)
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError as e:
    print('Error: Enter An Integer')
