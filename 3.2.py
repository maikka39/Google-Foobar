def solution(m, f):
    m = int(m)
    f = int(f)

    if (m > 1 or f > 1) and m == f:
        return "impossible"

    steps = 0

    while m >= 1 and f >= 1 and not m == f == 1:
        if f >= m:
            multiplier = (f // m)
            if m == 1:
                multiplier -= 1
            f -= m * multiplier
        else:
            multiplier = (m // f)
            if f == 1:
                multiplier -= 1
            m -= f * multiplier

        steps += multiplier

    if m != 1 or f != 1:
        return "impossible"

    return str(steps)


s1 = solution('4', '7')
print(s1, s1 == "4")

s2 = solution('2', '1')
print(s2, s2 == "1")

s3 = solution('2', '4')
print(s3, s3 == "impossible")

s4 = solution(1, 10**50)
print(s4, s4 == str(10**50 - 1))

s5 = solution(1, 1)
print(s5, s5 == str(0))

s6 = solution(2, 2)
print(s6, s6 == "impossible")

s7 = solution(5000, 15000)
print(s7, s7 == "impossible")
