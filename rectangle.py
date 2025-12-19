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
