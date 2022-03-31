#!/usr/bin/env python2
from decimal import Decimal, getcontext

getcontext().prec = 102

sqrt_2_minus_1 = Decimal(2).sqrt()-1


def solution(str_n):
    n = int(str_n)

    return str(rec(n))


def rec(n):
    if n == 0:
        return 0

    m = int(n*sqrt_2_minus_1)

    return n * m + ((n * (n + 1)) // 2) - ((m * (m + 1)) // 2) - rec(m)


s1 = solution("77")
print(s1 == "4208", s1)

s2 = solution("5")
print(s2 == "19", s2)
