import numpy as np
import math as m

def wheelSpeeds():
    return

def robotVelocities(radius, arc, time):
    angular = robotAngular(arc, time)
    forward = robotForward(angular, radius)
    print("Robot's angular momentum is", round(angular, 4), "radians per second.")
    print("Forward velocity is", round(forward, 4), "inches per second.")

def robotAngular(arc, time):
    return arc/time

def robotForward(angular, radius):
    return angular * radius

def wheelSpeeds(radius, arc, time, wheelbase):
    dia = 2.5
    circ = m.pi * dia
    outerArc = arcLength(radius + (wheelbase/2), arc)
    innerArc = arcLength(radius - (wheelbase/2), arc)
    outerRev = outerArc/circ
    innerRev = innerArc/circ
    print("Outer wheel speed is", round(outerRev/time, 4), "revolutions per second.")
    print("Inner wheel speed is", round(innerRev/time, 4), "revolutions per second.")

def arcLength(radius, arc):
    return radius*arc

def solve():
    print("Problem 4:")
    robotVelocities(30, (m.pi/3), 4)
    print()

    wheelSpeeds(30, (m.pi/3), 4, 6)