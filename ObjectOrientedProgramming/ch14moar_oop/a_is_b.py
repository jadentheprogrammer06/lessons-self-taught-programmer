# we write a function which takes two objects as parameters. returns True if both objects are the same object. returns False if both object aren't the same object.

def a_is_b(a, b):
    if a is b:
        return True
    else:
        return False


class ThisIsAClass():
    def __init__(self):
        pass

class AnotherClass():
    def __init__(self, name):
        pass

a = 10
b = 10

bill = 'bill'
joe = 'joe'
joey = 'joe'

this_is_an_object = ThisIsAClass
this_is_same_object = this_is_an_object
this_is_another_object = ThisIsAClass

other_object = AnotherClass('other object')
same_other_object = other_object
other_other_object = AnotherClass('other other other object')

print(a_is_b(a, b)) # should return True
print(a_is_b(bill, joe)) # should return False
print(a_is_b(joe, joey)) # should return True
print(a_is_b(this_is_an_object, this_is_same_object)) # should return True
print(a_is_b(this_is_an_object, this_is_another_object)) # this ended up returning True, since all objects of our sample class lack any unique, individual qualities.

print(a_is_b(other_object, same_other_object)) # should return True
print(a_is_b(other_object, other_other_object)) # should return False
