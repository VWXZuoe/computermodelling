"""
Vector operations codified to be imported to other programs
"""
import math


def sqmod(a):
    """
    Square modulus

    :param a: vector (a1, a2, a3)
    :return: square modulus a1**2+a2**2+a3**2
    """
    return a[0]**2 + a[1]**2 + a[2]**2

def mod(a):
    """
    Modulus

    :param a: vector (a1, a2, a3)
    :return: modulus (a1**2+a2**2+a3**2)**(1/2)
    """
    return math.sqrt(sqmod(a))

def mult(a, scalar):
    """
    Multiplication of vector by scalar

    :param a: vector (a1, a2, a3)
    :param scalar: scalar factor
    :return: scaled vector (a1*scalar, a2*scalar, a3*scalar)
    """
    return [a[0]*scalar, a[1]*scalar, a[2]*scalar]

def div(a, scalar):
    """
    Division of vector by a scalar

    :param a: vector (a1, a2, a3)
    :param scalar: scalar factor
    :return: scaled vector (a1/scalar, a2/scalar, a3/scalar)
    """
    return [a[0]/scalar, a[1]/scalar, a[2]/scalar]

def sum(a, b):
    """
    Vector addition

    :param a: first vector (a1, a2, a3)
    :param b: second vector (b1, b2, b3)
    :return: vector sum a+b
    """
    return [a[0]+b[0], a[1]+b[1], a[2]+b[2]]

def sub(a, b):
    """
    Vector subtraction

    :param a: first vector (a1, a2, a3)
    :param b: second vector (b1, b2, b3)
    :return: vector a - vector b
    """
    return [a[0]-b[0], a[1]-b[1], a[2]-b[2]]

def dot(a, b):
    """
    Scalar product of 2 vectors

    :param a: first vector (a1, a2, a3)
    :param b: second vector (b1, b2, b3)
    :return: scalar product
    """
    return [a[0]*b[0] + a[1]*b[1] + a[2]*b[2]]

def cross(a, b):
    """
    Vector product of 2 vectors

    :param a: first vector (a1, a2, a3)
    :param b: second vector (b1, b2, b3)
    calculate 3d cross product term by term
    :return: cross product (c1, c2, c3)
    """
    c[0]=a[1]*b[2]-b[1]*a[2]
    c[1]=a[2]*b[0]-b[2]*a[0]
    c[2]=a[0]*b[1]-b[0]*a[1]
    return c

def dup(a, b):
    """
    Check if 2 vectors are the same

    :param a: first vector (a1, a2, a3)
    :param b: second vector (b1, b2, b3)
    :return: equal or not equal
    """
    if sub (a, b)==[0, 0, 0]
        print ("equal")
        else print ("not equal")
