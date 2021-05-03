from math import factorial
from collections import Counter


def gcd(b, a):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def partitions(n):
    if n == 0:
        yield ()
        return

    for p in partitions(n-1):
        yield (1, ) + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield (p[0] + 1, ) + p[1:]


def coefficient_factor(partition, n):
    output = factorial(n)
    for a, b in Counter(partition).items():
        output //= (a**b) * factorial(b)
    return output


def solution(width, height, states):
    n = 0
    height_partitions = tuple(partitions(height))
    for width_partition in partitions(width):
        for height_partition in height_partitions:
            width_factor = coefficient_factor(width_partition, width)
            height_factor = coefficient_factor(height_partition, height)

            power = 0
            for i in width_partition:
                for j in height_partition:
                    power += gcd(i, j)

            n += width_factor * height_factor * (states ** power)

    return str(n // (factorial(width) * factorial(height)))


s1 = solution(2, 3, 4)
print(s1 == "430", s1)

s2 = solution(2, 2, 2)
print(s2 == "7", s2)

s3 = solution(4, 4, 20)
print(s3 == "1137863754106723400", s3)

s4 = solution(5, 5, 20)
print(s4 == "23301834615661488487765745000", s4)

s5 = solution(6, 6, 20)
print(s5 == "132560781153101038829213988789736592649360", s5)

s6 = solution(7, 7, 20)
print(s6 == "221619886894198821201872678876163305792210161226545392840", s6)

s7 = solution(8, 8, 20)
print(s7 == "113469378614817897312718329989374518983724697432844009920312263602471667640", s7)
