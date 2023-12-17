# isinstance() function
# isinstance(object, classinfo)
# Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof.
# If object is not an object of the given type, the function always returns False.

# Example 1: How isinstance() works in Python?
class Person:
    name = "John"
    age = 36


person = Person()

print(isinstance(person, Person))
print(isinstance(person, object))
