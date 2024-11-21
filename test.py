import unittest
import time
import math

import circle
import triangle
import rectangle
import square

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_zero_perimiter(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)
        
    def test_area_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_perimeter_sum(self):
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_negative(self):
        with self.assertRaises(AssertionError):
            rectangle.area(-5, -5)
        with self.assertRaises(AssertionError):
            rectangle.perimeter(-5, -5)
        
    def test_operation_speed(self):
        start = time.process_time()
        times = 100000
        for i in range(1,times):
            res = rectangle.area(20, 20)
            res = rectangle.perimeter(10, 5)
            res = 0
        end = time.process_time()
        print("\nRectangle time:",times,"times in:",end - start,"seconds")
        self.assertLess(end - start, 0.1)
    
class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    
    def test_zero_perimiter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
        
    def test_area_mul(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_perimeter_sum(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

    def test_negative(self):
        with self.assertRaises(AssertionError):
            square.area(-5)
        with self.assertRaises(AssertionError):
            square.perimeter(-5)
        
        
    def test_operation_speed(self):
        start = time.process_time()
        times = 100000
        for i in range(1,100000):
            res = square.area(20)
            res = square.perimeter(5)
            res = 0
        end = time.process_time()
        print("\nSquare time:",times,"times in:",end - start,"seconds")
        self.assertLess(end - start, 0.1)
        
class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_zero_perimiter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
        
    def test_area_mul(self):
        res = triangle.area(10, 10)
        self.assertEqual(res, 50)

    def test_perimeter_sum(self):
        res = triangle.perimeter(10, 11, 12)
        self.assertEqual(res, 33)

    def test_negative(self):
        with self.assertRaises(AssertionError):
            triangle.area(-5, 10)
        with self.assertRaises(AssertionError):
            triangle.perimeter(1, -5, 2)
        
    def test_operation_speed(self):
        start = time.process_time()
        times = 100000
        for i in range(1,times):
            res = triangle.area(20, 10)
            res = triangle.perimeter(5, 6, 7)
            res = 0
        end = time.process_time()
        print("\nTriangle time:",times,"times in:",end - start,"seconds")
        self.assertLess(end - start, 0.1)
    
class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    
    def test_zero_perimiter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
        
    def test_area_sq(self):
        res = circle.area(10)
        self.assertAlmostEqual(res, 100 * math.pi)

    def test_perimeter(self):
        res = circle.perimeter(10)
        self.assertAlmostEqual(res, 20 * math.pi)
    
    def test_negative(self):
        with self.assertRaises(AssertionError):
            circle.area(-5)
        with self.assertRaises(AssertionError):
            circle.perimeter(-5)
        
    def test_operation_speed(self):
        start = time.process_time()
        times = 100000
        for i in range(1,times):
            res = circle.area(10)
            res = circle.perimeter(15)
            res = 0
        end = time.process_time()
        print("\nCircle time:",times,"times in:",end - start,"seconds")
        self.assertLess(end - start, 0.1)
    
