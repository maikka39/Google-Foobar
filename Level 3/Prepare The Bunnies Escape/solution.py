#!/usr/bin/env python2

def cost_from_start(matrix, height, width, start_x, start_y):
    cost = [[None for _ in range(width)] for _ in range(height)]

    cost[start_x][start_y] = 1

    current = [(start_x, start_y)]

    while current:
        x, y = current.pop(0)

        for neighbor in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            neighbor_x = x + neighbor[0]
            neighbor_y = y + neighbor[1]

            if 0 <= neighbor_x < height and 0 <= neighbor_y < width and cost[neighbor_x][neighbor_y] is None:
                cost[neighbor_x][neighbor_y] = cost[x][y] + 1

                if matrix[neighbor_x][neighbor_y] == 1:
                    continue

                current.append((neighbor_x, neighbor_y))

    return cost


def solution(matrix):
    height = len(matrix)
    width = len(matrix[0])

    start_to_goal = cost_from_start(matrix, height, width, 0, 0)
    goal_to_start = cost_from_start(matrix, height, width, height-1, width-1)

    answer = float("inf")

    for x in range(height):
        for y in range(width):
            if start_to_goal[x][y] and goal_to_start[x][y]:
                answer = min(start_to_goal[x][y] +
                             goal_to_start[x][y] - 1, answer)

    return answer


s1 = solution([
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0]
])
print(s1 == 7, s1)

s2 = solution([
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
])
print(s2 == 11, s2)

s3 = solution([
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0]
])
print(s3 == 11, s3)
