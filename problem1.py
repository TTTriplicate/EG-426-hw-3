import numpy.linalg as lin
import math as m

def ccwRot(deg):
    rads = m.radians(deg)
    M = [[round(m.cos(rads), 4), round(-m.sin(rads), 4), 0],
     [round(m.sin(rads), 4), round(m.cos(rads), 4), 0], 
     [0, 0, 1]]
    return M

def cwRot(deg):
    M = ccwRot(deg)
    M = lin.inv(M)
    return M

def solve():
    angle = 45
    for row in ccwRot(angle):
        print(row)
    print()
    for row in cwRot(angle):
        print(row)