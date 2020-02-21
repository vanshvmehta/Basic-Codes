"""
To find HCF and LCM of 2 integers
"""


def HCF_LCM(a, b):
    HCF = LCM = 1
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            HCF = i
    for i in range(1, a * b + 1):
        if i % a == 0 and i % b == 0:
            LCM = i
            break
    print('LCM = ', LCM, ' and HCF = ', HCF)


while True:
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))
    HCF_LCM(a, b)
