"""
To check whether a number is an armstrong number or not
"""


def armstrong(n):
    sum, t = 0, n
    while n:
        sum += (n % 10) * (n % 10) * (n % 10)
        n //= 10
    if t == sum:
        print('Armstrong number')
    else:
        print('Not an armstrong number')


while True:
    n = int(input('Input the number: '))
    armstrong(n)