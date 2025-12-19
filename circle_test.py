from circle import *
import unittest

class CirceTestCase(unittest.TestCase):
  '''
    Overview of the test cases:
    test_zero_multiplication
    test_negative_number_stability_area
    test_negative_number_stability_perimeter
    test_small_multiplication - small float number multiplication
    test_big_multiplication - tests big number handling
    test_perimeter
    test_big_perimeter

    Big numbers are checked up to 3 places
    Small numbers are checked up to 7 places
  '''

  def test_zero_multiplication(self):
    result = area(0)
    self.assertAlmostEqual(result, 0)
       
  def test_small_multiplication(self):
    result = area(1.1)
    self.assertAlmostEqual(result, 1.21*math.pi, places=7)

  def test_negative_number_stability_area(self):
    result = area(-1.1)
    self.assertAlmostEqual(result, 1.21*math.pi, places=7)

  def test_negative_number_stability_perimeter(self):
    result = perimeter(-1.1)
    self.assertAlmostEqual(result, -1.1*2*math.pi, places=7)

  def test_big_multiplication(self):
    big_a = 823293.89339910
    area_expected = big_a * big_a * math.pi
    result = area(big_a)
    self.assertAlmostEqual(result, area_expected, places=3)

  def test_perimeter(self):
    result = perimeter(4)
    self.assertAlmostEqual(result, 8*math.pi, places=7)

  def test_big_perimeter(self):
    big_a = 1781782.7818727
    perimeter_expected = (big_a) * 2 * math.pi
    result = perimeter(big_a)
    self.assertAlmostEqual(result, perimeter_expected, places=3)
