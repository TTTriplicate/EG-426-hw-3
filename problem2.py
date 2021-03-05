import numpy as np
import numpy.linalg as lin
import math as m

def twoDimTransform(deg, coord):
    rads = m.radians(deg)
    M = [[m.cos(rads), -m.sin(rads), coord[0]],
     [m.sin(rads), m.cos(rads), coord[1]], 
     [0, 0, 1]]
    return M

def pointInBaseFrame(trans, point):
    rebasedPoint = np.matmul(trans, [[point[0]], [point[1]], [1]])
    for coord in rebasedPoint:
        print(coord)

def pointInRobotFrame(trans, point):
    rev = lin.inv(trans)
    print(rev)
    rebasedPoint = pointInBaseFrame(rev, point)
    
def solve():
    print("Problem 2:")
    M = twoDimTransform(270, (-3, 1))
    for row in M:
        print(row)
    print()

    pointInBaseFrame(M, (-4, -5))
    print()

    pointInRobotFrame(M, (-2, 2))