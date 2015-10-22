# (Ref. http://glowingpython.blogspot.ca/2011/07/how-to-use-reflection.html)
# How to use reflection
# A simple code snippet that use reflection to print names of attributes, methods and doc strings:

class Obj:
 """ An object that use reflection """

 def __init__(self,name):
  """ the constructor of this object """
  self.name = name

 def print_methods(self):
  """ print all the methods of this object and their doc string"""
  print '\n* Methods *'
  for names in dir(self):
   attr = getattr(self,names)
   if callable(attr):
    print names,':',attr.__doc__

 def print_attributes(self):
  """ print all the attributes of this object and their value """
  print '* Attributes *'
  for names in dir(self):
   attr = getattr(self,names)
   if not callable(attr):
    print names,':',attr

 def print_all(self):
  """ calls all the methods of this object """
  for names in dir(self):
   attr = getattr(self,names)
   if callable(attr) and names != 'print_all' and names != '__init__':
    attr() # calling the method

o = Obj('the my object')
o.print_all()

# Which gives the following output:

"""
* Attributes *
__doc__ :  An object that use reflection 
__module__ : __main__
name : the my object

* Methods *
__init__ :  the constructor of this object 
print_all :  calls all the methods of this object 
print_my_attributes :  print all the attributes of this object 
print_my_methods :  print all the methods of this object 

"""
