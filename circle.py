import math
import unittest


def area(r: float):
  '''
    Returns area of a circle
    Parameters:
      r (float): length of the radius of the circle
    Return value:
      area (float): area of the circle
    Usage:
      c_area = area(radius)
  '''
  return math.pi * r * r


def perimeter(r: float):
  '''
		Returns area of a circle
		Parameters:
		  r (float): length of the radius of the circle
		Return value:
		  perimeter (float): perimeter of the circle
		Usage:
		  c_perimeter = perimeter(radius)
	'''
  return 2 * math.pi * r

class CirceTestCase(unittest.TestCase):
  def test_zero_multiplication(self):
    result = area(0)
    self.assertAlmostEqual(result, 0)
       
  def test_square_multiplication(self):
    result = area(1.1)
    self.assertAlmostEqual(result, 1.21*math.pi, places=7)

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
