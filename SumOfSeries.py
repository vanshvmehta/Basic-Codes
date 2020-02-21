"""
To find sum of the following series where x is a float point and n is an integer

1. 1 + x/1! + x^2/2! ...... + x^n/n!
2. 1 - x/1! + x^2/2! ...... + (-1)^(n)*x^n/n!
3. 1 - x^2/2! + x^4/4! ...... + (-1)^(n)*x^2n/2n!
4. x/1! - x^3/3! + x^5/5! ...... + (-1)^(n)*x^(2n-1)/(2n-1)!
5. Exit the menu
"""

def a(x, n):
    sum = 1
    prod = 1
    for i in range(1, n + 1):
        prod *= i
        sum += x ** i / prod
    print(sum)


def b(x, n):
    sum = 1
    prod = 1
    for i in range(1, n + 1):
        prod *= (-1) * i
        sum += x ** i / prod
    print(sum)


def c(x, n):
    sum = 1
    prod = 1
    for i in range(2, 2 * n + 1, 2):
        prod *= (-1) * i * (i - 1)
        sum += x ** i / prod
    print(sum)


def d(x, n):
    sum = x
    prod = 1
    for i in range(3, 2 * n, 2):
        prod *= (-1) * i * (i - 1)
        sum += x ** i / prod
    print(sum)


print('''
1. 1 + x/1! + x^2/2! ...... + x^n/n!
2. 1 - x/1! + x^2/2! ...... + (-1)^(n)*x^n/n!
3. 1 - x^2/2! + x^4/4! ...... + (-1)^(n)*x^2n/2n!
4. x/1! - x^3/3! + x^5/5! ...... + (-1)^(n)*x^(2n-1)/(2n-1)!
5. Exit the menu
''')
opt = 0
while opt != 5:
    opt = int(input('Enter your option: '))
    if opt != 5:
        x = float(input('Enter value of x: '))
        n = int(input('Enter value of n: '))
    if opt == 1:
        a(x, n)
    elif opt == 2:
        b(x, n)
    elif opt == 3:
        c(x, n)
    elif opt == 4:
        d(x, n)
