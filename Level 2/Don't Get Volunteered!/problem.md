# Don't Get Volunteered!

Time to solve: `168 hours`.

## Description

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called `answer(src, dest)` which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between `0` and `63`, inclusive, and are numbered like the example chessboard below:

| - | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| **0** | 0| 1| 2| 3| 4| 5| 6| 7|
| **1** | 8| 9|10|11|12|13|14|15|
| **2** |16|17|18|19|20|21|22|23|
| **3** |24|25|26|27|28|29|30|31|
| **4** |32|33|34|35|36|37|38|39|
| **5** |40|41|42|43|44|45|46|47|
| **6** |48|49|50|51|52|53|54|55|
| **7** |56|57|58|59|60|61|62|63|

## Languages

To provide a Python solution, edit `solution.py`

To provide a Java solution, edit `Solution.java`

## Test Cases

### Test Case 1

Inputs:

```python
src = 19
dest = 36
```

Output:

```python
1
```

### Test Case 2

Inputs:

```python
src = 0
dest = 1
```

Output:

```python
3
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
