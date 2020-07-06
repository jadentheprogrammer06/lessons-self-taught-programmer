# we are creating a square_list class variable. An item gets appended to this class variable list every time a Square object gets created.

class Square():
    square_list = []
    def __init__(self, name, sidelength):
        self.name = name
        self.sl = sidelength
        self.slstr = str(self.sl)
        self.square_list.append(self.name)
        print(self.square_list)

# every time we print the object we want it to print the object dimensions
    def __repr__(self):
        return ' by '.join([self.slstr, self.slstr, self.slstr, self.slstr])

square = Square('square', 10)
print(square)
square2 = Square('square2', 20)
print(square2)

