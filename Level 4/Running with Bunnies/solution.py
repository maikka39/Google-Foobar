#!/usr/bin/env python2
from itertools import permutations, product


def solution(time, time_limit):
    bunnies = len(time) - 2

    for i in range(len(time)):
        for x, y in product(range(len(time)), range(len(time))):
            if time[x][y] > time[x][i] + time[i][y]:
                time[x][y] = time[x][i] + time[i][y]

    for x in range(len(time)):
        if time[x][x] < 0:
            return list(range(bunnies))

    for n in range(bunnies, -1, -1):
        for perm in permutations(range(1, bunnies + 1), n):
            locs = [0] + list(perm) + [-1]
            total_time = sum(time[locs[i - 1]][locs[i]]
                             for i in range(1, len(locs)))
            if total_time <= time_limit:
                return [i - 1 for i in sorted(perm)]


s1 = solution([
    [0, 2, 2, 2, -1],
    [9, 0, 2, 2, -1],
    [9, 3, 0, 2, -1],
    [9, 3, 2, 0, -1],
    [9, 3, 2, 2, 0]
], 1)
print(s1 == [1, 2], s1)

s2 = solution([
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
], 3)
print(s2 == [0, 1], s2)

s3 = solution([
    [0, 2, 2, 2, -1],
    [9, 0, 2, 2, -1],
    [9, 3, 0, 2, -1],
    [9, -3, 2, 0, -1],
    [9, 3, 2, 2, 0]
], 1)
print(s3 == [0, 1, 2], s3)
