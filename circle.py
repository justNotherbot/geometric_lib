import math

def area(r: float):
  '''
    Returns area of a circle
    Parameters:
      r (float), positive: length of the radius of the circle
    Return value:
      area (float), positive: area of the circle
    Usage:
      c_area = area(radius)
  '''
  return math.pi * r * r


def perimeter(r: float):
  '''
		Returns area of a circle
		Parameters:
		  r (float), positive: length of the radius of the circle
		Return value:
		  perimeter (float), positive: perimeter of the circle
		Usage:
		  c_perimeter = perimeter(radius)
	'''
  return 2 * math.pi * r
