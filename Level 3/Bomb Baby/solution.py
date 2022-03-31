#!/usr/bin/env python2

def solution(m_count, f_count):
    m_count = int(m_count)
    f_count = int(f_count)

    if (m_count > 1 or f_count > 1) and m_count == f_count:
        return "impossible"

    steps = 0

    while m_count >= 1 and f_count >= 1 and not m_count == f_count == 1:
        if f_count >= m_count:
            multiplier = (f_count // m_count)
            if m_count == 1:
                multiplier -= 1
            f_count -= m_count * multiplier
        else:
            multiplier = (m_count // f_count)
            if f_count == 1:
                multiplier -= 1
            m_count -= f_count * multiplier

        steps += multiplier

    if m_count != 1 or f_count != 1:
        return "impossible"

    return str(steps)


s1 = solution('4', '7')
print(s1 == "4", s1)

s2 = solution('2', '1')
print(s2 == "1", s2)

s3 = solution('2', '4')
print(s3 == "impossible", s3)

s4 = solution(1, 10**50)
print(s4 == str(10**50 - 1), s4)

s5 = solution(1, 1)
print(s5 == str(0), s5)

s6 = solution(2, 2)
print(s6 == "impossible", s6)

s7 = solution(5000, 15000)
print(s7 == "impossible", s7)
