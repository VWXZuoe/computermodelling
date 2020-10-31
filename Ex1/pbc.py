"""
Jude Ferrier - s1808200 - 31/10/20
Ex 1.
Program to find the image of a position r within
a cube of length l repeated over space and the closest
image to the origin.
"""

import numpy as np

def main():
    # Inputs are asked for the coordinates of the vector and the length of the cubes that space is divided into
    rx = float(input("Input rx:"))
    ry = float(input("Input ry:"))
    rz = float(input("Input rz:"))

    r = np.array([rx, ry, rz])
    l = float(input("Input l:"))

    # The image of the vector in the first cube with sides in positive x, y, z is created by taking the remainder of division r/l
    imager = np.mod(r, l)
    print ("Image of r in cube 0 <= x, y, z <= l:", imager)

    # Individual components are created to check which side of the axis planes the closes image will be on
    imagerx = np.mod(rx, l)
    imagery = np.mod(ry, l)
    imagerz = np.mod(rz, l)

    # Each component is checked individually against its image across each plane to see which is closer to the origin
    if np.abs(imagerx)>np.abs(imagerx-l):
        closestx = imagerx-l
    else:
        closestx = imagerx

    if np.abs(imagery)>np.abs(imagery-l):
        closesty = imagery-l
    else:
        closesty = imagery

    if np.abs(imagerz)>np.abs(imagerz-l):
        closestz = imagerz-l
    else:
        closestz = imagerz

    # Final set of closest componets are presented in an array
    print("The nearest image to the origin is at:", np.array([closestx, closesty, closestz]))

main()
