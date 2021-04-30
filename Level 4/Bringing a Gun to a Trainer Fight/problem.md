# Bringing a Gun to a Trainer Fight

Time to solve: `360 hours`.

## Description

Uh-oh -- you've been cornered by one of Commander Lambdas elite bunny trainers! Fortunately, you grabbed a beam weapon from an abandoned storeroom while you were running through the station, so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the bunny trainers: its beams reflect off walls, meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam hits either you or the bunny trainer, it will stop immediately (albeit painfully). 

Write a function `solution(dimensions, your_position, trainer_position, distance)` that gives an array of 2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 integers of the trainer's x and y coordinates in the room, and returns an integer of the number of distinct directions that you can fire to hit the elite trainer, given the maximum distance that the beam can travel.

The room has integer dimensions `[1 < x_dim <= 1250, 1 < y_dim <= 1250]`. You and the elite trainer are both positioned on the integer lattice at different distinct positions (x, y) inside the room such that `[0 < x < x_dim, 0 < y < y_dim]`. Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer `1 < distance <= 10000`.

For example, if you and the elite trainer were positioned in a room with dimensions `[3, 2]`, your\_position `[1, 1]`, trainer\_position `[2, 1]`, and a maximum shot distance of `4`, you could shoot in seven different directions to hit the elite trainer (given as vector bearings from your location): ``[1, 0]`, `[1, 2]`, `[1, -2]`, `[3, 2]`, `[3, -2]`, `[-3, 2]`, and `[-3, -2]`. As specific examples, the shot at bearing `[1, 0]` is the straight line horizontal shot of distance `1`, the shot at bearing `[-3, -2]` bounces off the left wall and then the bottom wall before hitting the elite trainer with a total shot distance of `sqrt(13)`, and the shot at bearing `[1, 2]` bounces off just the top wall before hitting the elite trainer with a total shot distance of `sqrt(5)`.

## Languages

To provide a Python solution, edit `solution.py`

To provide a Java solution, edit `Solution.java`

## Test Cases

### Test Case 1

Inputs:

```python
room_dimensions = [3, 2]
your_position = [1, 1]
trainer_position = [2, 1]
max_shot_distance = 4
```

Output:

```python
7
```

### Test Case 2

Inputs:

```python
room_dimensions = [300, 275]
your_position = [150, 150]
trainer_position = [185, 100]
max_shot_distance = 500
```

Output:

```python
9
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
