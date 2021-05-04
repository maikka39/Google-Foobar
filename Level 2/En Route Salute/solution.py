def solution(s):
    to_salute = 0
    counter = 0

    for i, ch in enumerate(s):
        if ch == "-":
            continue
        if ch == ">":
            counter += 1
        else:
            to_salute += counter

    return to_salute*2


s1 = solution(">----<")
print (s1 == 2, s1)

s2 = solution("<<>><")
print(s2 == 4, s2)

s3 = solution("--->->-<><-->-")
print(s3 == 10, s3)
