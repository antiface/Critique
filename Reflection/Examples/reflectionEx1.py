# (Ref. https://en.wikibooks.org/wiki/Python_Programming/Reflection)
# Python Programming/Reflection

# A Python script can find out about the type, class, attributes and methods of an object.
# This is referred to as reflection or introspection. See also Metaclasses.

# Reflection-enabling functions include type(), isinstance(), callable(), dir() and getattr().

# Type
# The type method enables to find out about the type of an object. The following tests return True:

type(3) is int
type('Hello') is str
type([1, 2]) is list
type([1, [2, 'Hello']]) is list
type({'city': 'Paris'}) is dict

# Isinstance
# Determines whether an object is an instance of a class.

# The following returns True:

isinstance(3, int)
isinstance([1, 2], list)

# Note that isinstance provides a weaker condition than a comparison using #Type.

# Duck typing
# Duck typing provides an indirect means of reflection.
# It is a technique consisting in using an object as if it was of the requested type,
# while catching exceptions resulting from the object not supporting some of the features of the class or type.

# Callable
# For an object, determines whether it can be called. A class can be made callable by providing a __call__() method.

# Examples:

callable(2)
# Returns False. Ditto for callable("Hello") and callable([1, 2]).

callable([1,2].pop)
# Returns True, as pop without "()" returns a function object.

callable([1,2].pop())
# Returns False, as [1,2].pop() returns 2 rather than a function object.

# Dir
# Returns the list of attributes of an object, which includes methods.

# Examples:

dir(3)
dir("Hello")
dir([1, 2])

# Getattr
# Returns the value of an attribute of an object, given the attribute name passed as a string.

# An example:

getattr(3, "imag")

# The list of attributes of an object can be obtained using #Dir.
