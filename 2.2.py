def solution(s):
    to_salute = 0
    stack = []
    for i, ch in enumerate(s):
        if ch == "-":
            continue
        if ch == ">":
            stack.append(ch)
        else:
            to_salute += len(stack)
    return to_salute*2


print(solution(">----<"), solution(">----<") == 2)
print(solution("<<>><"), solution("<<>><") == 4)
print(solution("--->->-<><-->-"), solution("--->-><-><-->-") == 10)
