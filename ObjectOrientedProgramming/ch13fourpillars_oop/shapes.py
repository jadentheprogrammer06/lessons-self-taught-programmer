
class Shape():
    def __init__(self, shape_name):
        print("Object created.")
        self.name = shape_name

    def what_am_i(self):
        print("I am a shape:")
        return self.name

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
        print(self.length, 'length of two sides')
        print(self.width, 'length of other two sides')
        if self.length == self.width:
            print("I am a Rectangle who happens to be a square.") # maybe this is overengineering, I still think this is useful to have.
            self.name = "Square"
        else:
            print("I am a Rectangle.")
# interestingly, after we added in the [check for square functionality] to the parent Rectangle class, we don't have to actually assign the name in the subclass Square. Its parent class will automatically change the name to "Square" if it detects the object is a square.
# this doesn't make our subclass Square pointless. It still functions with the purpose of creating a square with equal side lengths and only one argument given.
    def calculate_perimeter(self):
        print('total of all sides')
        return (self.length * 2) + (self.width * 2)

class Square(Rectangle):
    def __init__(self, sidelength):
        # in our square, the subclass of Rectangle, it inherits the __init__ and method from Rectangle except the Square's sidelength argument is passed >
        super().__init__(sidelength, sidelength)
        self.name = "Square" # we inherit from Rectangle, but change the name for Square.

    def change_size(self, increment):
        '''
        method that allows you to change a squares side incrementally by the [increment], positive or negative, that is given.
        '''  # belongs only to subclass Square, not Rectangle.
        self.length += increment
        self.width += increment
        print(self.length, self.width)
        print(self.calculate_perimeter())


triangle = Shape("Triangle")
print(triangle.what_am_i())
print('\n')
rect_obj = Rectangle(20, 40)
print(rect_obj.calculate_perimeter())
print(rect_obj.what_am_i())
print('\n')
square_obj = Square(20)
print(square_obj.calculate_perimeter())
print(square_obj.what_am_i())
print('\n')
rect_is_square = Rectangle(30,30)
print(rect_is_square.what_am_i())

square_obj.change_size(20)
