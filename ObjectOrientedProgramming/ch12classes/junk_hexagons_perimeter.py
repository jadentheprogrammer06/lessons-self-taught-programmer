import math

class Polygons():
	def __init__(self, s, l):
		self.side = s
		self.sidelength = l

	def find_parameter(self):
		return (self.side * self.sidelength)
# polygons works fine. Trying to make hexagon a derived class (or subclass) is real confusing. includes junk code. will look at later on.
class Hexagon(Polygons):
	def __init__(self):
		Polygons.__init__(self, 6, *args)

	def calculate_parameter(self, l):
		return (self.side * l)

polygon = Polygons(8, 20)
print(polygon.find_parameter())

hexagon = Hexagon(10)
print(hexagon.find_parameter())
