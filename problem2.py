import numpy as np
import math as m

def twoDimTransform(deg, coord):
    rads = m.radians(deg)
    M = [[round(m.cos(rads), 4), round(-m.sin(rads), 4), coord[0]],
     [round(m.sin(rads), 4), round(m.cos(rads), 4), coord[1]], 
     [0, 0, 1]]
    return M

def solve():
    for row in twoDimTransform(30, (3, -3)):
        print(row)