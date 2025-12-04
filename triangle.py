import unittest

def area(base: float, height: float):
  '''
		Returns area of a triangle
		Parameters:
		  base (float): length of the base of the triangle
      height (float): length of the triangle's height(perpendicular to base)
		Return value:
		  area (float): area of the triangle
		Usage:
		  t_area = area(side)
	'''
  return 0.5 * base * height

def perimeter(a: float, b: float, c: float):
  '''
		Returns perimeter of a triangle
		Parameters:
		  a,b,c (float): length of three distinct sides of the triangle
		Return value:
		  perimeter (float): perimeter of the triangle
		Usage:
		  t_perimeter = perimeter(side)
	'''
  return a+b+c

class TriangleTestCase(unittest.TestCase):
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