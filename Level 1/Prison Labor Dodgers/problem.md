# Prison Labor Dodgers

Time to solve: `24 hours`.

## Description

Commander Lambda is all about efficiency, including using her bunny prisoners for manual labor. But no one's been properly monitoring the labor shifts for a while, and they've gotten quite mixed up. You've been given the task of fixing them, but after you wrote up new shifts, you realized that some prisoners had been transferred to a different block and aren't available for their assigned shifts. And manually sorting through each shift list to compare against prisoner block lists will take forever - remember, Commander Lambda loves efficiency!

Given two almost identical lists of prisoner IDs x and y where one of the lists contains an additional ID, write a function `solution(x, y)` that compares the lists and returns the additional ID.

For example, given the lists `x = [13, 5, 6, 2, 5]` and `y = [5, 2, 5, 13]`, the function `solution(x, y)` would return `6` because the list x contains the integer 6 and the list y doesn't. Given the lists `x = [14, 27, 1, 4, 2, 50, 3, 1]` and `y = [2, 4, -4, 3, 1, 1, 14, 27, 50]`, the function answer(x, y) would return `-4` because the list y contains the integer -4 and the list x doesn't.

In each test case, the lists x and y will always contain n non-unique integers where n is at least 1 but never more than 99, and one of the lists will contain an additional unique integer which should be returned by the function. The same n non-unique integers will be present on both lists, but they might appear in a different order, like in the examples above. Commander Lambda likes to keep her numbers short, so every prisoner ID will be between -1000 and 1000.

## Languages

To provide a Python solution, edit `solution.py`

To provide a Java solution, edit `Solution.java`

## Test Cases

### Test Case 1

Inputs:

```python
x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13]
```

Output:

```python
[6]
```

### Test Case 2

Inputs:

```python
x = [14, 27, 1, 4, 2, 50, 3, 1]
y = [2, 4, -4, 3, 1, 1, 14, 27, 50]
```

Output:

```python
[-4]
```

## Constraints

### Java

- Your code will be compiled using standard Java 8. All tests will be run by calling the solution() method inside the Solution class

- Execution time is limited.

- Wildcard imports and some specific classes are restricted (e.g. java.lang.ClassLoader). You will receive an error when you verify your solution if you have used a blacklisted class.

- Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed.

- Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

### Python

- Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

- Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

- Input/output operations are not allowed.

- Your solution must be under 32000 characters in length including new lines and and other non-printing characters.
