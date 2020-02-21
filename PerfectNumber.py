"""
To check whether a number is a perfect number or not
"""

def perfect(n):
    sum = 1
    for i in range(2, n):
        if n % i == 0:
            sum += i
    if sum == n:
        print('Perfect number')
    else:
        print('Not a Perfect number')


while True:
    n = int(input('Input the number: '))
    perfect(n)
