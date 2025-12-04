import unittest

def area(a: float):
	'''
		Returns area of a square
		Parameters:
		  a (float): length of the side of the square
		Return value:
		  area (float): area of the square
		Usage:
		  s_area = area(side)
	'''
	return a * a


def perimeter(a: float):
	'''
		Returns perimeter of a square
		Parameters:
		  a (float): length of the side of the square
		Return value:
		  perimeter (float): perimeter of the square
		Usage:
		  s_perimeter = perimeter(side)
	'''
	return 4 * a

class SquareTestCase(unittest.TestCase):
  def test_zero_multiplication(self):
    result = area(0)
    self.assertEqual(result, 0)
       
  def test_square_multiplication(self):
    result = area(1.1)
    self.assertAlmostEqual(result, 1.21, places=7)

  def test_big_multiplication(self):
    big_a = 82329389339910
    area_expected = big_a * big_a
    result = area(big_a)
    self.assertEqual(result, area_expected)

  def test_perimeter(self):
    result = perimeter(4)
    self.assertEqual(result, 16)

  def test_big_perimeter(self):
    big_a = 17817827818727
    perimeter_expected = (big_a) * 4
    result = perimeter(big_a)
    self.assertEqual(result, perimeter_expected)
