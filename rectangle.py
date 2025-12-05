import unittest

def area(a: float, b: float):
  '''
		Returns area of a rectangle
		Parameters:
		  a,b (float), positive: length of 2 perpendicular sides of the rectangle
		Return value:
		  area (float), positive: area of the rectangle
		Usage:
		  r_area = area(side)
	'''
  return a*b

def perimeter(a: float, b: float):
  '''
		Returns perimeter of a rectangle
		Parameters:
		  a,b (float), positive: length of 2 perpendicular sides of the rectangle
		Return value:
		  perimeter (float), positive: perimeter of the rectangle
		Usage:
		  r_perimeter = perimeter(side)
	'''
  return 2*(a+b)


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