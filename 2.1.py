def solution(x, y):
    horizontal = (x*(x+1))//2
    vertical = ((y+x-2)*(y+x-1))//2 - ((x-1)*(x))//2

    return str(horizontal + vertical)


print(solution(5, 10), solution(5, 10) == "96")
print(solution(3, 2), solution(3, 2) == "9")
print(solution(2, 3), solution(2, 3) == "8")
print(solution(1, 1), solution(1, 1) == "1")
