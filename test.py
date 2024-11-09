from circle import *
from square import *
from triangle import *
from rectangle import *
import unittest

class Test_Circle(unittest.TestCase):
    def test_is_corret_circle(self):
        res = correct_circle(4)
        self.assertEqual(res, True)


    def test_circle_area(self):
        res = area_circle(4)
        self.assertEqual(res, 50.26548245743669)


    def test_circle_perimeter(self):
        res = perimeter_circle(4)
        self.assertEqual(res, 25.132741228718345)


class Test_Square(unittest.TestCase):
    def test_is_corret_square(self):
        res = correct_square(4)
        self.assertEqual(res, True)


    def test_square_area(self):
        res = area_square(4)
        self.assertEqual(res, 16)


    def test_square_perimeter(self):
        res = perimeter_square(4)
        self.assertEqual(res, 16)



class Test_Triangle(unittest.TestCase):
    def test_is_corret_triangle(self):
        res = correct_triangle(4, 5, 4)
        self.assertEqual(res, True)


    def test_triangle_area(self):
        res = area_triangle(6, 4)
        self.assertEqual(res, 12)


    def test_triangle_perimeter(self):
        res = perimeter_triangle(4, 5, 4)
        self.assertEqual(res, 13)


class Test_Rectangle(unittest.TestCase):
    def test_is_corret_rectangle(self):
        res = correct_rectangle(5, 10)
        self.assertEqual(res, True)


    def test_rectangle_area(self):
        res = area_rectangle(5, 10)
        self.assertEqual(res, 50)


    def test_rectangle_perimeter(self):
        res = perimeter_rectangle(5, 10)
        self.assertEqual(res, 30)


if __name__ == '__main__':
    unittest.main()