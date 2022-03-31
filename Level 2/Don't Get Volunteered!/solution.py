#!/usr/bin/env python2
from collections import deque


def solution(src, dest):
    source = (src, 0)

    moves = [6, -6, 10, -10, 15, -15, 17, -17]

    queue = deque([source])
    visited = set()
    while len(queue) > 0:
        node = queue.popleft()

        if node[0] == dest:
            return node[1]

        if node not in visited:
            visited.add(node)
            for move in moves:
                new_node = (node[0] + move, node[1] + 1)
                if 0 <= new_node[0] <= 63:
                    queue.append(new_node)


s1 = solution(19, 36)
print(s1 == 1, s1)

s2 = solution(0, 1)
print(s2 == 3, s2)
