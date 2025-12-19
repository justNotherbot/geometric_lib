import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
  '''
    Overview of the test cases:
    test_zero_multiplication
    test_negative_number_stability_area
    test_negative_number_stability_perimeter
    test_square_multiplication - same side test
    test_big_multiplication - tests big number handling
    test_perimeter
    test_big_perimeter
  '''

  def test_zero_multiplication(self):
    result = area(10, 0)
    self.assertEqual(result, 0)

  def test_negative_number_stability_area(self):
    result = area(-10, 3)
    self.assertEqual(result, -15)

  def test_negative_number_stability_perimeter(self):
    result = perimeter(-10, -3, -8)
    self.assertEqual(result, -21)
       
  def test_square_multiplication(self):
    result = area(10.5, 10.5)
    self.assertAlmostEqual(result, 55.125, places=7)

  def test_big_multiplication(self):
    big_a = 82329389339910
    big_b = 91092019029019
    area_expected = big_a * big_b / 2
    result = area(big_a, big_b)
    self.assertEqual(result, area_expected)

  def test_perimeter(self):
    result = perimeter(4, 6, 10)
    self.assertEqual(result, 20)

  def test_big_perimeter(self):
    big_a = 17817827818727
    big_b = 28832389293892
    big_c = 89198291892900
    perimeter_expected = (big_a + big_b + big_c)
    result = perimeter(big_a, big_b, big_c)
    self.assertEqual(result, perimeter_expected)