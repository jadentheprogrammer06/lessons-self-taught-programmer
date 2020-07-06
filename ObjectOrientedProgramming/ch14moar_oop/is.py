# keyword is returns True if two objects are the same object, and False if not:
# if both belong to the same class but not the same object, it is False.

class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob) #should return True

another_bob = Person()
print(bob is another_bob) #should return False

# use "is" to check if the variable is None.

def is_x_none(x):
    if x is None:
        print(f"X ({x}) is None :(")
    else:
        print(f"X ({x}) is not None :)")

x = 10
is_x_none(x)
x = None
is_x_none(x)
x = 0
is_x_none(x)
