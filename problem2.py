import numpy as np
import math as m

def twoDimTransform(deg, coord):
    rads = m.radians(deg)
    M = [[m.cos(rads), -m.sin(rads), coord[0]],
     [m.sin(rads), m.cos(rads), coord[1]], 
     [0, 0, 1]]
    return M

def solve():
    print(twoDimTransform(30, (3, -3)))