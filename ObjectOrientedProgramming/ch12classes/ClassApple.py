
class Apple():
	def __init__(self, color, sweetness, sourness, rot):
		self.color = color
		self.sweetness = sweetness
		self.sourness = sourness
		self.rot = rot
		print(self)
		print("object created", 'properties: ', color+','+sweetness+','+sourness+','+rot)

apple1 = Apple('green', 'not sweet', 'more sour', 'fresh')
apple2 = Apple('red', 'sweet: just right', 'sour: just right', 'fresh')
apple3 = Apple('blue', 'unimaginable sweetness', "alien-type sour", "don't know")

apple4 = Apple('green', 'not sweet', 'more sour', 'fresh')
# notice if we print() a specific Apple object through its instance variable it should return the same value. This value is the actual object stored in memory.
print(apple3)
print(apple3)
print(apple1)
print(apple2)


print(apple4)
print(apple1)
