import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
  '''
    Overview of the test cases:
    test_zero_multiplication
    test_square_multiplication - same side test
    test_big_multiplication - tests big number handling
    test_perimeter
    test_big_perimeter
  '''

  def test_zero_multiplication(self):
    result = area(10, 0)
    self.assertEqual(result, 0)
       
  def test_square_multiplication(self):
    result = area(10.01, 10)
    self.assertAlmostEqual(result, 100.1, places=7)

  def test_negative_number_stability_area(self):
    result = area(-7, 6)
    self.assertEqual(result, -42)

  def test_negative_number_stability_perimeter(self):
    result = perimeter(-7, -6)
    self.assertEqual(result, -26)

  def test_big_multiplication(self):
    big_a = 82329389339910
    big_b = 91092019029019
    area_expected = big_a * big_b
    result = area(big_a, big_b)
    self.assertEqual(result, area_expected)

  def test_perimeter(self):
    result = perimeter(4, 6)
    self.assertEqual(result, 20)

  def test_big_perimeter(self):
    big_a = 17817827818727
    big_b = 28832389293892
    perimeter_expected = (big_a + big_b) * 2
    result = perimeter(big_a, big_b)
    self.assertEqual(result, perimeter_expected)