print '\n1.feladat : gomb terfogat\n'
import math


def vol(rad):
    return 4 / 3 * math.pi * rad ** 3


print vol(3)

print '\n2.feladat : benne van-e a szam az intervallumban\n'


def ran_check(num, low, high):
    if low <= num <= high:
        return True
    else:
        return False


print ran_check(2, 1, 10)

print '\n3.feladat : kis es nagybetu szamolas\n'


def up_low(st):
    u = 0
    l = 0
    for i in st:
        if i.islower():
            l += 1
        if i.isupper():
            u += 1
    print 'upper case letters: ', u, '\nlower case letters: ', l


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

print '\n4.feladat : duplikatumok eltavolitasa\n'

lst = [1, 2, 2, 2, 3, 3, 4, 7, 7, 7, 8, 5, 5, 5]


def unique_list(l):
    return set(l)


print unique_list(lst)

print '\n5.feladat : listaelemek osszeszorzasa\n'


def multiply(num):
    y = 1
    for i in num:
        y *= i
    return y


print multiply(lst)

print '\n6.feladat : palindrom\n'


def palindrome(szo):
    if szo == szo[::-1]:
        return True
    else:
        return False


print palindrome('indulagorogaludni')
