#!/usr/bin/env python2

def solution(input_str):
    to_salute = 0
    counter = 0

    for char in input_str:
        if char == "-":
            continue
        if char == ">":
            counter += 1
        else:
            to_salute += counter

    return to_salute*2


s1 = solution(">----<")
print(s1 == 2, s1)

s2 = solution("<<>><")
print(s2 == 4, s2)

s3 = solution("--->->-<><-->-")
print(s3 == 10, s3)
