import math

class Circle():
	def __init__(self, r):
		self.radius = r

	def area(self):
		print('finding area...')
		return (math.pi) * (self.radius ** 2)


circle = Circle(5)
print(circle.area())
