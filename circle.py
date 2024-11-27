import math


def area_circle(r):

    return math.pi * r * r


def perimeter_circle(r):

    return 2 * math.pi * r


def correct_circle(r):
    if r < 0:
        return False
    return True