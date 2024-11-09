import math


def area_circle(r):
    '''
    Возвращает площадь окружности по заданному радиусу.

         Параметры:
                 r (int) или (float) - радиус окружности.

         Возвращает значение:
                 area(r) - площадь окружности радиусом r.
    '''
    return math.pi * r * r


def perimeter_circle(r):
    '''
    Возвращает периметр окружности по заданному радиусу.

         Параметры:
                 r (int) или (float) - радиус окружности.

         Возвращает значение:
                 perimeter(r) - периметр окружности радиусом r.
    '''
    return 2 * math.pi * r


def correct_circle(r):
    if r < 0:
        return False
    return True