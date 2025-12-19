def area(base: float, height: float):
  '''
		Returns area of a triangle
		Parameters:
		  base (float), positive: length of the base of the triangle
      height (float), positive: length of the triangle's height(perpendicular to base)
		Return value:
		  area (float), positive: area of the triangle
		Usage:
		  t_area = area(side)
	'''
  return 0.5 * base * height

def perimeter(a: float, b: float, c: float):
  '''
		Returns perimeter of a triangle
		Parameters:
		  a,b,c (float), positive: length of three distinct sides of the triangle
		Return value:
		  perimeter (float), positive: perimeter of the triangle
		Usage:
		  t_perimeter = perimeter(side)
	'''
  return a+b+c
