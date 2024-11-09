
def area_triangle(a, h):
    return a * h / 2


def perimeter_triangle(a, b, c):
    return a + b + c


def correct_triangle(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return False
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True