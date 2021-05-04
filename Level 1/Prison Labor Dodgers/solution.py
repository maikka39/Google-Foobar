def solution(x, y):
    setx = set(x)
    sety = set(y)

    return list(setx-sety) + list(sety-setx)


s1 = solution([13, 5, 6, 2, 5], [5, 2, 5, 13])
print(s1 == [6], s1)

s2 = solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
print(s2 == [-4], s2)
