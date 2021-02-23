#!/usr/bin/python
import problem1 as p1
import problem2 as p2

problems = [p1.solve, p2.solve]

for p in problems:
    p()
    print()