"""
To check is a number is fibonacci or not
"""


def fibo(n):
    d1 = d2 = 1
    while d2 <= n:
        d = d1 + d2
        d1, d2 = d2, d
    if d1 == n:
        print('Fibonacci number')
    else:
        print('Not a Finonacci number')


while True:
    n = int(input('Enter a number: '))
    fibo(n)
