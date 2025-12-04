# Project description
This is a python library for calculation of perimiter and area of primitive shapes.

At the moment the following shapes are supported:
- circle
- square
# Project structure
## circle.py
Functions for circle
### Function area
Returns area of a circle
#### Parameters
  r (float): length of the radius of the circle
#### Return value
  area (float): area of the circle
#### Usage
    from geometric_lib import circle
    c_area = circle.area(radius)
### Function perimeter
Returns perimeter of a circle
#### Parameters
  r (float): length of the radius of the circle
#### Return value
  perimeter (float): perimeter of the circle
#### Usage
    from geometric_lib import circle
    c_perimeter = circle.perimeter(radius)
## square.py
Functions for square
### Function area
Returns area of a square
#### Parameters
  a (float): length of the side of the square
#### Return value
  area (float): area of the square
#### Usage
    from geometric_lib import square
    s_area = square.area(side)
### Function perimeter
Returns perimeter of a square
#### Parameters
  a (float): length of the side of the square
#### Return value
  perimeter (float): perimeter of the square
#### Usage
    from geometric_lib import square
    s_perimeter = square.perimeter(side)

# Project history
[8ba9aeb](https://github.com/smartiqaorg/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460) L-03: Circle and square added