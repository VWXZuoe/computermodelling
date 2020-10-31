"""
Jude Ferrier - s1808200 - 31/10/20
Ex 1.
Program to test the numpy module
Creates 3 vectors in 3 dimensions and runs
through several numpy functions to demonstrate that
known vector identities hold true
"""

import numpy as np
import random as r

def main():
    # Create 3 random vectors as arrays
    a = np.array([r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)])
    b = np.array([r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)])
    c = np.array([r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)])

    print ("a =",a)
    print ("b =",b)
    print ("c =",c)
    # Prints the magnitudes of each vector
    print ("|a| = ", np.linalg.norm(a))
    print ("|b| = ", np.linalg.norm(b))
    print ("|c| = ", np.linalg.norm(c))
    # Prints the values of each vector operations
    print ("a + b =", a + b)
    print ("a . b =", np.inner(a, b))
    print ("a x b =", np.cross(a, b))

    """
    Vector identity tests

    Prints arrays of true or false based on whether
    the values of each component of the vectors produced
    by each identity are within a small tolerance of each
    other (+/- 0.0000001)

    This tolerance has been chosen to remove the effect of rounding errors
    """

    # First vector identity from Ex1 document tested
    print ("Test 1")
    test1L = np.cross(a, b)
    test1R = np.cross(-b, a)
    print (np.isclose(test1L, test1R, atol=0.0000001))

    # Second vector identity from Ex1 document tested
    print ("Test 2")
    test2L = np.cross(a, b+c)
    test2R = np.cross(a, b) + np.cross(a, c)
    print (np.isclose(test2L, test2R, atol=0.0000001))

    # Third vector identity from Ex1 document tested
    print ("Test 3")
    test3L = np.cross(a, np.cross(b, c))
    test3R = np.inner(a,c)*b - np.inner(a, b)*c
    print (np.isclose(test3L, test3R, atol=0.0000001))

main()
