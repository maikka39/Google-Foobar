def solution(x, y):
    setx = set(x)
    sety = set(y)

    return list(setx-sety) + list(sety-setx)


print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))
print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]))
