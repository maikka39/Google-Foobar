#!/usr/bin/env python2
from math import ceil, sqrt


def dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def gcd(b, a):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def norm(n):
    return max(-1, min(n, 1))


def simplify_fraction(a, b):
    if a == 0 or b == 0:
        return norm(a), norm(b)
    d = gcd(a, b)
    a //= d
    b //= d
    return a, b


def get_vectors(dimensions, start_pos, target_pos, max_distance):
    max_distance = float(max_distance)
    targets = {}

    x_scale = int(ceil(max_distance / dimensions[0]))+1
    y_scale = int(ceil(max_distance / dimensions[1]))+1
    x_range = dimensions[0] * x_scale
    y_range = dimensions[1] * y_scale
    current_x = -x_range + \
        (target_pos[0] if x_scale % 2 == 0 else dimensions[0] - target_pos[0])
    for current_right_border in range(-x_range + dimensions[0], x_range + 1, dimensions[0]):
        current_y = -y_range + \
            (target_pos[1] if y_scale %
             2 == 0 else dimensions[1] - target_pos[1])
        for current_top_border in range(-y_range + dimensions[1], y_range + 1, dimensions[1]):
            pos = (current_x, current_y)
            distance = dist(start_pos, pos)
            if distance <= max_distance:
                frac = simplify_fraction(
                    current_x - start_pos[0], current_y - start_pos[1])
                if distance < targets.get(frac, float('inf')):
                    targets[frac] = distance
            current_y += (current_top_border - current_y) * 2
        current_x += (current_right_border - current_x) * 2

    return targets


def solution(dimensions, start_pos, target_pos, distance):
    hit_target = get_vectors(dimensions, start_pos, target_pos, distance)
    hit_self = get_vectors(dimensions, start_pos, start_pos, distance)

    bearings = [
        bearing
        for bearing in hit_target
        if bearing in hit_self
        and hit_target[bearing] < hit_self[bearing]
        or bearing not in hit_self
    ]

    return len(bearings)


s1 = solution([3, 2], [1, 1], [2, 1], 4)
print(s1 == 7, s1)

s2 = solution([300, 275], [150, 150], [185, 100], 500)
print(s2 == 9, s2)

s3 = solution([10, 10], [4, 4], [3, 3], 5000)
print(s3 == 739323, s3)

s4 = solution([23, 10], [6, 4], [3, 2], 23)
print(s4 == 8, s4)

s5 = solution([2, 5], [1, 2], [1, 4], 11)
print(s5 == 27, s5)
