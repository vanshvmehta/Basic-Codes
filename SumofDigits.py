"""
To find sum and product of digits of a number
"""


def digit(n):
    sum, prod, count = 0, 1, 0
    while n:
        d = n % 10
        sum += d
        prod *= d
        count += 1
        n //= 10
    print('Number of digits = ', count)
    print('Sum and product of digits = ', sum, ',', prod, ' repectively')


while True:
    n = int(input('Enter a number: '))
    digit(n)
