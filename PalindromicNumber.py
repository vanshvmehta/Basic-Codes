"""
To check if a number is palindromic number or not
"""


def palindrome(n):
    t, s = 0, n
    while s:
        d = s % 10
        t = t * 10 + d
        s //= 10
    if t == n:
        print('Palindrome number')
    else:
        print('Not a palindrome number')


while True:
    n = int(input('Enter a number: '))
    palindrome(n)
