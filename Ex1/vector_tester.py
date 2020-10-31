"""
Jude Ferrier - s1808200 - 31/10/20
Ex 1.
Program to test vector.py
Creates 3 vectors in 3 dimensions and runs the functions from vector.py
to check against known vector identities
"""

import math
import random
import vector as vr


def main():
    """
    First generates 3 vectors with integer components ranging from -10 to 10 as lists, and prints them.
    Modulus of each is printed and then the required vector identities are tested with vectors a and b.
    The three more complex vector identities are tested at the end by taking the left and right sides of the equality to be
    seperate variables and composing them from imported component functions.
    """

#random module used to generate vectors
    a = [random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)]
    b = [random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)]
    c = [random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)]

    print("a = ", a)
    print("b = ", b)
    print("c = ", c)

#imported functions calculates magnitudes of each and then the sum, scalar product and vector product
    print("|a| = ", vr.mod(a))
    print("|b| = ", vr.mod(b))
    print("|c| = ", vr.mod(c))

    print ("a + b = ", vr.sum(a, b))
    print ("a . b = ", vr.dot(a, b))
    print ("a x b = ", vr.cross(a, b))
#each more complex identity is constructed from the imported functions and "equal" is printed if the identity holds, while "not equal" is printed if the idenity appears false
    print("Test 1:")
    test1L = vr.cross(a, b)
    test1R = vr.cross(vr.mult(b, -1.0), a)
    vr.dup(test1L, test1R)

    print("Test 2:")
    test2L = vr.cross(a, vr.sum(b, c))
    test2R = vr.sum (vr.cross(a, b), vr.cross(a, c))
    vr.dup(test2L, test2R)

    print("Test 3:")
    test3L = vr.cross(a, vr.cross(b, c))
    test3R = vr.sub(vr.mult(b, vr.dot(a, c)), vr.mult(c, vr.dot(a,b)))
    vr.dup(test3L, test3R)

main()
