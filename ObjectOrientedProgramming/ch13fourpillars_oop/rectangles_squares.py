
class Rectangle():
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def calculate_perimeter(self):
		return (self.length * 2) + (self.width * 2)

class Square(Rectangle):
	def __init__(self, sidelength):
		super().__init__(sidelength, sidelength) # in our square, the subclass of Rectangle, it inherits the __init__ and method from Rectangle except the Square's sidelength argument is passed in as both the length and width arguments found in Rectangle. i.e. all sides are the same size now, when creating a square object.

	def change_size(self, increment):
		'''
		method that allows you to change a squares side incrementally by the [increment], positive or negative, that is given.
		''' # belongs only to subclass Square, not Rectangle.
		self.length += increment; self.width += increment
		print(self.length, self.width)
		print(self.calculate_perimeter())





rect_obj = Rectangle(6, 10)
print(rect_obj.calculate_perimeter())
# 6 * 2 + 10 * 2 = 32
square_obj = Square(20)
print(square_obj.calculate_perimeter())
# 2 * 20 + 2 * 20 [or 4*20] = 80

square_obj.change_size(6)
square_obj.change_size(3)
square_obj.change_size(-4)

#rect_obj.change_size(40)
# ^ returns AttributeError: "Rectangle has no attribute 'change_size'"
