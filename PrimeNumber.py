"""
To check whether a number is a prime number or not
"""


def prime(n):
    sum = 0
    for i in range(2, n):
        if n % i == 0:
            sum += i
    if sum == 0:
        print('Prime number')
    else:
        print('Not a Prime number')


while True:
    n = int(input('Input the number: '))
    prime(n)
