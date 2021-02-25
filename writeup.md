Chris Sousa
EG-426

# Homework 3 - Kinematics

I wrote some Python scripts to do much of the math, particularly in problems 2 and 4.  I will include that code with my submission.

## Problem 1
Assume two coordinate systems that are co-located in the same origin, but rotated around the z-axis by the angle $\alpha$ . Give the rotation matrix from one coordinate system into the other, and the inverse rotation matrix.

The counter clockwise rotation around the z-axis is described by the matrix:
$$
\begin{bmatrix}
\cos\alpha &-\sin\alpha & 0\\
\sin\alpha & \cos\alpha & 0\\
0 & 0 & 1
\end{bmatrix}
$$

This matrix is orthogonal; this can be demonstrated by the fact that any single vector of the matrix multiplied by the transpose of another is 0.  This is easily demonstrated for vector 3; it has zeros corresponding to the contents on the other vectors, and vice versa.
$$
\begin{bmatrix}\cos\alpha & \sin \alpha & 0\end{bmatrix} \cdot\begin{bmatrix}-\sin\alpha \\ \cos \alpha \\0\end{bmatrix} = ((\cos\alpha * -\sin\alpha) + (\sin\alpha * \cos\alpha) + 0) \sim 0\\
$$
Since the matrix is orthogonal, its inverse is simply its transpose:
$$
\begin{bmatrix}
\cos\alpha &\sin\alpha & 0\\
-\sin\alpha & \cos\alpha & 0\\
0 & 0 & 1
\end{bmatrix}
$$

## Problem 2

A mobile robot is located at x=3, y=-3, with an orientation of $30^o$.

### a. See drawing

###   b. Offer a 3x3, 2-D homogeneous transform matrix that describes the location and orientation of the robot relative to the base frame.  

Since we are looking at a 2-D plane, transforming the orientation is a z-axis rotation of $30^o$ with an offset of (3, -3):
$$
\begin{bmatrix}
\cos30^o &-\sin30^o & 3\\
\sin30^o & \cos30^o & -3\\
0 & 0 & 1
\end{bmatrix}
$$

### c. The robot detects an object at x=3, y=-2, relative to its internal reference frame. Where is the object located in the base frame?  

We can find this by multiplying this transform matrix by the point vector in the robot's reference space:
$$
\begin{bmatrix}
\cos30^o &-\sin30^o & 3\\
\sin30^o & \cos30^o & -3\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}3 \\ -2 \\ 1\end{bmatrix} = 
\begin{bmatrix}6.598 \\ -3.232 \\ 1\end{bmatrix}
$$
Which tells us that our identified object is at coordinates (6.598, -3.232) in the base frame.

### d. Compute the inverse of the 3x3 matrix in part (b).  

I used the linear algebra submodule of NumPy for this instead of doing it by hand.
$$
\begin{bmatrix}
\cos30^o & \sin30^o & -1.098\\
-\sin30^o & \cos30^o & 4.098\\
0 & 0 & 1
\end{bmatrix}
$$



### e. Use the results from (d) to determine the location of an object in robot coordinates given that its location in the global frame is x=7, y=-1.  

$$
\begin{bmatrix}
\cos30^o & \sin30^o & -1.098\\
-\sin30^o & \cos30^o & 4.098\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}7 \\ -1 \\ 1 \end{bmatrix}
 = 
 \begin{bmatrix}4.464 \\ -0.268 \\ 1 \end{bmatrix}
$$

## Problem 3

A mobile robot follows a circular trajectory of radius 2 with a center at coordinates (3, 3). If the robot is moving in the clockwise direction, determine a matrix to represent the robot’s position and orientation when the robot's x coordinate is:  

$(x-3)^2 + (y - 3)^2 = 4$

(a) and (b) are on cardinal directions, so y will just be on line with the center with a clockwise rotation in increments of $90^o$, which makes the rotation portion of the matrix all 1s and 0s.  (c) is not as clean.

For clarity, anytime there are numbers split as $x|y$ inside the matrices, this is a simplification of two matrices.  Either all of the left options inside that matrix are chosen, or all of the right.

a. x = 3

y=5 OR y=1
$$
\begin{bmatrix}
0|-1 &1 | 0 & 0\\
-1|0 & 0|-1 & 2|-2\\
0 & 0 & 1
\end{bmatrix}
$$


b. x =1

y = 3
$$
\begin{bmatrix}
0 & 1 & -2\\
-1 & 0 & 0\\
0 & 0 & 1
\end{bmatrix}
$$


c. x = 2

$$
(1) + (y - 3)^2 = 4\\
y^2 - 6y + 10 = 4 \\
y^2 - 6y + 6 = 0\\
y = \frac{6\pm\sqrt{(-6)^2 - 4(1)(6)}}{2}\\
y = 4.732 | 1.268
$$

With those y values, we can use that for our third column in the matrices.  However, we still need to calculate our rotation angle.  Drawing a triangle from (3, 5) or (3, 1) to (2, 4.732) or (2, 1.268) respectively, allows us to trigonometrically calculate the angle sitting at the second point.
$$
\theta = \tan(\frac{1.268 - 1}{1}) = \tan(.268) = .275 rad\\
\theta = \tan(\frac{5-4.732}{1}) = \tan(.268) = .275 rad
$$

That will be the clockwise rotation in radians beyond the total inversion when y = 1.268, and counter-clockwise from base when y = 4.732, giving us matrices of:
$$
\begin{bmatrix}
\cos(\pi + .275) & \sin(\pi + .275) & -1\\
-\sin(\pi + .275) & \cos(\pi + .275) & 3-(3 - 1.268)\\
0 & 0 & 1
\end{bmatrix}
\text{OR}
\begin{bmatrix}
\cos(.275) & -\sin(.275) & -1\\
\sin(.275) & \cos(.275) & 3+(5-4.732)\\
0 & 0 & 1
\end{bmatrix}
$$

## Problem 4

Professor Carlstrom desires to drive a robot in a circular arc, with a radius of 30 inches. On his first
attempt, he will use a two-wheel robot with a wheel diameter of 2.5 inches and a base length of 6
inches. He desires to traverse a $60^o$ arc in 4 seconds. Show all necessary work.

### a) What must the forward and angular velocities of the robot be to achieve his goal?  

Arc length to traverse = $\frac{\pi}{3}30 = 10\pi$ inches at center of robot.
Outside(right) arc = $\frac{\pi}{3}33 = 11\pi$ inches.
Inside(left) arc = $\frac{\pi}{3}27 = 9\pi$ inches.
$$
\phi = \frac{A_r - A_l}{6} \\
\phi = \frac{11\pi - 9\pi}{6} \to \frac{2\pi}{6}\\
\phi = \frac{\pi}{3}
$$
This tracks with our intended arc of 60 degrees, or $\frac{\pi}{3}$ radians.

Angular velocity of the robot is .2618 rad/s:
$$
\frac{\frac{\pi}{3}}{4} \to \frac{1.047}{4} = \frac{.2618}{s}
$$
The forward velocity will be the distance travelled on that arc, calculated as either the arc length travelled over time or as $V = \omega r$:
$$
V = \frac{10\pi}{4} = \frac{2.5\pi}{s} = \frac{7.854}{s}\\
V = (.2618)(30) = \frac{7.854}{s}
$$

### b) What are the wheel speeds?  

To get the wheel speeds, we start by getting the wheel circumference, which is $2.5 * \pi = 7.854$ inches.  The we calculate the arc length of each wheel based on the circumference driven by the robot offset by the wheelbase:
$$
\text{Outer Arc} = \frac{\pi}{3}33 = 11\pi\\
\text{Inner Arc} = \frac{\pi}{3}27 = 9\pi
$$
Now we have the distance travelled per revolution, and the total distance each wheel needs to travel, letting us calculate the total revolutions of each wheel:
$$
\text{Outer Revs} = \frac{11\pi}{7.854} = 4.4 rev\\
\text{Inner Revs} = \frac{9\pi}{7.854} = 3.6rev
$$
And since this travel is happening over 4 seconds, we can get the revolutions per second by simply dividing by 4:
$$
\text{Outer Speed} = \frac{4.4}{4} = 1.1 rev/s\\
\text{Inner Speed} = \frac{3.6}{4} = 0.9rev/s
$$

## Problem 5

Having enjoyed problem #4, Professor Carlstrom desires to try again with an Ackerman steering
robot. This robot has a wheel diameter of 2.5 inches and a base length of 8 inches. Show all necessary
work.  

### a) What must the forward and angular velocities of the robot be to achieve his goal?  

The basic mechanics of the velocities do not change.  Since the robot is still traversing a 30" circle at a rate of $\frac{\pi}{3}$ radians every 4 seconds, the forward and angular velocities are still 7.854 in/s and .2618 rad/s respectively. 

### b) What are the rear wheel speeds?  

Now that the wheel speeds are separated from the turning mechanics, the two tires can have the same drive speed.  Taking the math from problem 4 part b, we can simply strip out the wheelbase adjustments.  So we have an arc length of $10\pi$ inches to drive in 4 seconds, and a distance per revolution of 2.5$\pi$ inches.  The math is simple: 1 rev/s.

### c) What is the steering angle?  

The ideal angle is simple:
$$
\tan(\delta) = (\frac{L}{r})\to \tan(\delta) = \frac{8}{30}\\
\delta = \arctan(\frac{8}{30}) = .2606\text{ rad}
$$
However this doesn't take the wheelbase into account.  In order to do that, we need to offset the actual radius of each steering tire by half the distance of the wheelbase to represent the slightly different paths the actual tires will travel:
$$
\tan(\delta_i) = \frac{L}{r-\frac{w}{2}} \to \frac{8}{27}\\
\delta_i = \arctan(\frac{8}{27}) = .2880\\
\tan(\delta_o) = \frac{L}{r+\frac{w}{2}} \to \frac{8}{33}\\
\delta_o = \arctan({8}{33}) = .2378
$$