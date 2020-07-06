
class Rider():
	def __init__(self, name):
		self.name = name
		print(self.name)
class Horse():
	def __init__(self, name, breed, owner):
		self.name = name; self.breed = breed; self.owner = owner
		print(self.name); print(self.breed); print(self.owner.name)

joemama = Rider("Joe Mama")

billy = Horse("Billy Horse", "Brown", joemama)
