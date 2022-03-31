# Bunny Prisoner Locating

Time to solve: `48 hours`.

## Description

Keeping track of Commander Lambda's many bunny prisoners is starting to get tricky. You've been tasked with writing a program to match bunny prisoner IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:

```dat
| 7
| 4 8
| 2 5 9
| 1 3 6 10
```

Each cell can be represented as points `(x, y)`, with x being the distance from the vertical wall, and y being the height from the ground.

For example, the bunny prisoner at `(1, 1)` has ID `1`, the bunny prisoner at `(3, 2)` has ID `9`, and the bunny prisoner at `(2,3)` has ID `8`. This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners).

Write a function `solution(x, y)` which returns the prisoner ID of the bunny at location `(x, y)`. Each value of x and y will be at least 1 and no greater than 100,000. Since the prisoner ID can be very large, return your solution as a string representation of the number.

## Languages

To provide a Python solution, edit `solution.py`

To provide a Java solution, edit `Solution.java`

## Test Cases

### Test Case 1

Inputs:

```python
x = 5
y = 10
```

Output:

```python
"96"
```

### Test Case 2

Inputs:

```python
x = 3
y = 2
```

Output:

```python
"9"
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
