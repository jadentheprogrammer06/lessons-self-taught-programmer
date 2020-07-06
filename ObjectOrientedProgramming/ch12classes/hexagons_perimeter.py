
class Hexagons():
	def __init__(self, side_length):
		self.length = side_length
		self.sides = 6

	def calculate_perimeter(self):
		return(self.length * self.sides)

hexagon_length_10 = Hexagons(10)
print(hexagon_length_10)
print(hexagon_length_10.calculate_perimeter()) #length is 10, so perimeter (10 * 6_sides) should be 60.
