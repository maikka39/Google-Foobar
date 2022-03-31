#!/usr/bin/env python2

def solution(x, y):
    set_x = set(x)
    set_y = set(y)

    return list(set_x-set_y) + list(set_y-set_x)


s1 = solution([13, 5, 6, 2, 5], [5, 2, 5, 13])
print(s1 == [6], s1)

s2 = solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
print(s2 == [-4], s2)
