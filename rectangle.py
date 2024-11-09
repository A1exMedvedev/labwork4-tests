
def area_rectangle(a, b):
    return a * b


def perimeter_rectangle(a, b):
    return a + a + b + b


def correct_rectangle(a, b):
    if a < 0 or b < 0:
        return False
    return True