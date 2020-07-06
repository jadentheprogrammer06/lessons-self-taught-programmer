class Triangle():
	def __init__(self, length, width):
		self.length = length
		self.width = width
		
	def area(self): #we use self because when we create a shape object we can find its area through the object itself. The function (is actually a method since it belongs to one type of object created by a class) will only be used with data provided by the object itself. If we want to find another circle's area we would create a separate shape object of the class with different parameters.
		return .5 * (self.length * self.width)
# thanks to using a class, it will automatically call the class method for each class object. No need to enter values that were already provided when making an object instance.

triangle1 = Triangle(5,10) # area should be 25.
print(triangle1.area())
triangle2 = Triangle(2, 50) #area should be 50.
print(triangle2.area()) # make sure when calling methods of an object, 
