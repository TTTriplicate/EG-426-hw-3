#!/usr/bin/python
import problem1 as p1
import problem2 as p2
import problem4 as p4

problems = [p1.solve, p2.solve, p4.solve]

for p in problems:
    p()
    print()