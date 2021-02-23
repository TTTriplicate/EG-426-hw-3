import numpy.linalg as lin
import math as m

def ccwRot(deg):
    rads = m.radians(deg)
    M = [[m.cos(rads), -m.sin(rads), 0],
     [m.sin(rads), m.cos(rads), 0], 
     [0, 0, 1]]
    return M

def cwRot(deg):
    M = ccwRot(deg)
    M = lin.inv(M)
    return M

def solve():
    print("Problem 1, using a rotation of 45 degrees:")
    
    angle = 45
    for row in ccwRot(angle):
        print(row)
    print()
    for row in cwRot(angle):
        print(row)