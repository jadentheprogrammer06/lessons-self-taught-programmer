class Lion:
    def __init__(self, name): #magic method python uses when object is created. includes instance variables that will be used and are required.
        self.name = name

    def __repr__(self): #magic method python uses which represents what will be returned when object is printed.
        return self.name

lion = Lion("Joe Mama")
print(lion)

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other): #magic method python uses when adding operators. first operand passed into object when operator evaluated with second operand passed in as the other variable.
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x+y)

a = AlwaysPositive(-17)
b = AlwaysPositive(10)

print(a+b)
