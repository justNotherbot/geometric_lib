import unittest
from square import *

class SquareTestCase(unittest.TestCase):
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
		result = area(0)
		self.assertEqual(result, 0)

	def test_negative_number_stability_area(self):
		result = area(-10)
		self.assertEqual(result, 100)

	def test_negative_number_stability_perimeter(self):
		result = perimeter(-4)
		self.assertEqual(result, -16)
       
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
