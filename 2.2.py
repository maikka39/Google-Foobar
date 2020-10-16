def solution(s):
    to_salute = 0
    counter = 0  # Should have been a counter
    for i, ch in enumerate(s):
        if ch == "-":
            continue
        if ch == ">":
            counter += 1
        else:
            to_salute += counter
    return to_salute*2


print(solution(">----<"), solution(">----<") == 2)
print(solution("<<>><"), solution("<<>><") == 4)
print(solution("--->->-<><-->-"), solution("--->-><-><-->-") == 10)
