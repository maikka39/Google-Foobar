#!/usr/bin/env python2

def solution(x, y):
    horizontal = (x*(x+1))//2
    vertical = ((y+x-2)*(y+x-1))//2 - ((x-1)*(x))//2

    return str(horizontal + vertical)


s1 = solution(5, 10)
print(s1 == "96", s1)

s2 = solution(3, 2)
print(s2 == "9", s2)

s3 = solution(2, 3)
print(s3 == "8", s3)

s4 = solution(1, 1)
print(s4 == "1", s4)
