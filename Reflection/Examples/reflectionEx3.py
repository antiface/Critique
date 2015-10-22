# (Ref. http://www.assembleforce.com/2012-08/reflection-in-python.h)

# Reflection in Python

# Python is an interesting programming language that is flexible and easy to hand on. It is syntax is of a bit freestyle and you can access to the inner system easily from the source code. This article will show you an interesting feature of the modern high-level programming language. It is called reflection.

# What is Reflection

# Reflection of a programming language is the ability to examine, modify and maintain its inner structure by the programming language itself at runtime.

# For example, if I write a class and I want to enumerate all the methods and print them to a file, I will need to know the exact set of methods associated with this class. Not that this structure is associated with the type, but not the instance. For the association with type, I mean the structure is defined by type and is already decided before the program runs. A live example can be C++. When you write a class in C++, you know all the details of this C++ class. However, when the program runs, the program itself is not aware of the structure of the class because it is lack of the ability the examine its inner structure at runtime.

# Of course, you can say you don’t need to examine its structure at runtime because you already knew it when writing this class. But how you can modify the structure remains unsolved.

# For example, if you want to call method A(), and then call it again except that we expect a different behaviour at your second calling to that method. How can C++ achieve this? It can’t. But with Python, you can do this easily.

# Python Reflection in Real-world

# The following source code defines a class with a constructor __init__() and two methods. A function introduce() is also defined to provide an example od reflection for method.

class reflect(object):
    '''
    A demo class for Python reflection
    '''
    def __init__(self):
        '''
        Constructor for reflect class
        '''
        self.name = "Hongbao Chen"
        self.gender = "Male"
        self.hobby = "Computer game"
        
    def message(self):
        print "I am ", self.name, " and my gender is ", self.gender, "I like ", self.hobby
        print "How do you do?"
    
    @classmethod
    def static_message(self):
        print "I can be called without an instance."
    
def introduce():
    print "I just introduce myself."
       
# Every method inside a class receive a ‘self’ parameter because the ‘self’ will be passed into a reference to it corresponding instance of its class. In the inner virtual machine, the ‘binding’ will save you lots of time and keep you from many troubles.

# Function introduce() is defined without self as parameter because it is not a instance method nor class method.

# Reflection in Actions

from Reflect import reflect
from Reflect import introduce
if __name__ == '__main__':
    ref = reflect()
    
    print ref.__class__
    print ref.__dict__
    print ref.__doc__
    print ref.__sizeof__()
    
    print ref.__getattribute__('name')
    
    ref.__setattr__('name', 'Stranger')
    print ref.name
    
    introduce()
    ref.intro = introduce;
    ref.intro()
    
    ref.message()
    ref.message = introduce
    ref.message()
    
    print ref.__hash__()
    
    #ref.__delattr__('name')
    print ref.name
    
    reflect.static_message();

# The first line is used to get an instance of the certain class. There are several built-in functions for the class can you can use it without importing any libraries.

# And then, we assign the introduce function to the Reflction and then call the intro(). we find that the output of the latter is different from the former ones. Note that, the function intro() is a new funciton whose name is just been added to class reflet.

# The modification of message() method is an example of modifying class; inner structure.

# We can use __delattr__(string) to delete any variable. If you uncomment the last third line, you will find that ‘print’ statement following it will cause error because the attribute in class reflection is deleted by ourselves.

# The object.__doc__() will return the printable string describing the attributes and their values currently in the class reflect. The __doc__() will return the comment for the class. The sizeof() is very useful because it make you a chance to have a look the memory consumption when the design of the new products were changed.

# The last line of the second script demonstrate the use of a class method. A class method takes in the first parameter as a class and then can be called in both class and instance.

# Conclusion

# This article, I talked about the reflection in python and also show some interesting aspects of it. If you like this article, please press the retweet buttons.
