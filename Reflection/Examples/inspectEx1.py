# (Ref. https://pymotw.com/2/inspect/)
# inspect – Inspect live objects
# Purpose:	The inspect module provides functions for introspecting on live objects and their source code.
# Available In:	added in 2.1, with updates in 2.3 and 2.5
# The inspect module provides functions for learning about live objects, including modules, classes, instances,
# functions, and methods. You can use functions in this module to retrieve the original source code for a function,
# look at the arguments to a method on the stack, and extract the sort of information useful for producing
# library documentation for your source code. My own CommandLineApp module uses inspect to determine the
# valid options to a command line program, as well as any arguments and their names so command line programs are
# self-documenting and the help text is generated automatically.

# Module Information

# The first kind of introspection supported lets you probe live objects to learn about them.
# For example, it is possible to discover the classes and functions in a module, the methods of a class, etc.
# Let’s start with the module-level details and work our way down to the function level.

# To determine how the interpreter will treat and load a file as a module, use getmoduleinfo().
# Pass a filename as the only argument, and the return value is a tuple including the module base name,
# the suffix of the file, the mode that will be used for reading the file, and the module type as defined
# in the imp module. It is important to note that the function looks only at the file’s name, and does not
# actually check if the file exists or try to read the file.

import imp
import inspect
import sys

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = 'example.py'

try:
    (name, suffix, mode, mtype)  = inspect.getmoduleinfo(filename)
except TypeError:
    print 'Could not determine module type of %s' % filename
else:
    mtype_name = { imp.PY_SOURCE:'source',
                   imp.PY_COMPILED:'compiled',
                   }.get(mtype, mtype)

    mode_description = { 'rb':'(read-binary)',
                         'U':'(universal newline)',
                         }.get(mode, '')

    print 'NAME   :', name
    print 'SUFFIX :', suffix
    print 'MODE   :', mode, mode_description
    print 'MTYPE  :', mtype_name

# Here are a few sample runs:
"""
$ python inspect_getmoduleinfo.py example.py

NAME   : example
SUFFIX : .py
MODE   : U (universal newline)
MTYPE  : source

$ python inspect_getmoduleinfo.py readme.txt

Could not determine module type of readme.txt

$ python inspect_getmoduleinfo.py notthere.pyc

NAME   : notthere
SUFFIX : .pyc
MODE   : rb (read-binary)
MTYPE  : compiled
"""

# Example Module

# The rest of the examples for this tutorial use a single example file source file, found in PyMOTW/inspect/example.py
# and which is included below. The file is also available as part of the source distribution associated with
# this series of articles.

"""Sample file to serve as the basis for inspect examples.
"""

def module_level_function(arg1, arg2='default', *args, **kwargs):
    """This function is declared in the module."""
    local_variable = arg1
    return

class A(object):
    """The A class."""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        "Returns the name of the instance."
        return self.name

instance_of_a = A('sample_instance')

class B(A):
    """This is the B class.
    It is derived from A.
    """

    # This method is not part of A.
    def do_something(self):
        """Does some work"""
        pass

    def get_name(self):
        "Overrides version from A"
        return 'B(' + self.name + ')'

# Modules

# It is possible to probe live objects to determine their components using getmembers().
# The arguments to getmembers() are an object to scan (a module, class, or instance) and
# an optional predicate function that is used to filter the objects returned. The return value
# is a list of tuples with 2 values: the name of the member, and the type of the member.
# The inspect module includes several such predicate functions with names like ismodule(), isclass(), etc.
# You can provide your own predicate function as well.

# The types of members that might be returned depend on the type of object scanned. Modules can contain classes
# and functions; classes can contain methods and attributes; and so on.

import inspect

import example

for name, data in inspect.getmembers(example):
    if name == '__builtins__':
        continue
    print '%s :' % name, repr(data)

# This sample prints the members of the example module. Modules have a set of __builtins__, which are ignored in
# the output for this example because they are not actually part of the module and the list is long.

"""
$ python inspect_getmembers_module.py
A : <class 'example.A'>
B : <class 'example.B'>
__doc__ : 'Sample file to serve as the basis for inspect examples.\n'
__file__ : '/Users/dhellmann/Documents/PyMOTW/branches/inspect/example.pyc'
__name__ : 'example'
instance_of_a : <example.A object at 0xbb810>
module_level_function : <function module_level_function at 0xc8230>
"""

# The predicate argument can be used to filter the types of objects returned.

import inspect

import example

for name, data in inspect.getmembers(example, inspect.isclass):
    print '%s :' % name, repr(data)

# Notice that only classes are included in the output, now:
"""
$ python inspect_getmembers_module_class.py

A : <class 'example.A'>
B : <class 'example.B'>
"""

# Classes

# Classes are scanned using getmembers() in the same way as modules, though the types of members are different.

import inspect
from pprint import pprint

import example

pprint(inspect.getmembers(example.A))

# Since no filtering is applied, the output shows the attributes, methods, slots, and other members of the class:
"""
$ python inspect_getmembers_class.py
[('__class__', <type 'type'>),
 ('__delattr__', <slot wrapper '__delattr__' of 'object' objects>),
 ('__dict__', <dictproxy object at 0xca090>),
 ('__doc__', 'The A class.'),
 ('__getattribute__', <slot wrapper '__getattribute__' of 'object' objects>),
 ('__hash__', <slot wrapper '__hash__' of 'object' objects>),
 ('__init__', <unbound method A.__init__>),
 ('__module__', 'example'),
 ('__new__', <built-in method __new__ of type object at 0x32ff38>),
 ('__reduce__', <method '__reduce__' of 'object' objects>),
 ('__reduce_ex__', <method '__reduce_ex__' of 'object' objects>),
 ('__repr__', <slot wrapper '__repr__' of 'object' objects>),
 ('__setattr__', <slot wrapper '__setattr__' of 'object' objects>),
 ('__str__', <slot wrapper '__str__' of 'object' objects>),
 ('__weakref__', <attribute '__weakref__' of 'A' objects>),
 ('get_name', <unbound method A.get_name>)]
"""
# To find the methods of a class, use the ismethod() predicate:

import inspect
from pprint import pprint

import example

pprint(inspect.getmembers(example.A, inspect.ismethod))
"""
$ python inspect_getmembers_class_methods.py

[('__init__', <unbound method A.__init__>),
 ('get_name', <unbound method A.get_name>)]
"""
# If we look at class B, we see the over-ride for get_name() as well as the new method, and the inherited __init__()
# method implented in A.

import inspect
from pprint import pprint

import example

pprint(inspect.getmembers(example.B, inspect.ismethod))

# Notice that even though __init__() is inherited from A, it is identified as a method of B.

"""
$ python inspect_getmembers_class_methods_b.py

[('__init__', <unbound method B.__init__>),
 ('do_something', <unbound method B.do_something>),
 ('get_name', <unbound method B.get_name>)]
"""

# Documentation Strings

# The docstring for an object can be retrieved with getdoc(). The return value is the __doc__ attribute with tabs
# expanded to spaces and with indentation made uniform.

import inspect
import example

print 'B.__doc__:'
print example.B.__doc__
print
print 'getdoc(B):'
print inspect.getdoc(example.B)

# Notice the difference in indentation on the second line of the doctring:
"""
$ python inspect_getdoc.py

B.__doc__:
This is the B class.
    It is derived from A.


getdoc(B):
This is the B class.
It is derived from A.
"""

# In addition to the actual docstring, it is possible to retrieve the comments from the source file where
# an object is implemented, if the source is available. The getcomments() function looks at the source of
# the object and finds comments on lines preceding the implementation.

import inspect
import example

print inspect.getcomments(example.B.do_something)

# The lines returned include the comment prefix, but any whitespace prefix is stripped off.
"""
$ python inspect_getcomments_method.py

# This method is not part of A.
"""

# When a module is passed to getcomments(), the return value is always the first comment in the module.

import inspect
import example

print inspect.getcomments(example)
# Notice that contiguous lines from the example file are included as a single comment, but as soon as a
# blank line appears the comment is stopped.
"""
$ python inspect_getcomments_module.py

# This comment appears first
# and spans 2 lines.
"""

# Retrieving Source

# If the .py file is available for a module, the original source code for the class or method can be retrieved
# using getsource() and getsourcelines().

import inspect
import example

print inspect.getsource(example.A.get_name)

# The original indent level is retained in this case.
"""
$ python inspect_getsource_method.py

    def get_name(self):
        "Returns the name of the instance."
        return self.name
"""

# When a class is passed in, all of the methods for the class are included in the output.

import inspect
import example

print inspect.getsource(example.A)
"""
$ python inspect_getsource_class.py
"""

class A(object):
    """The A class."""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        "Returns the name of the instance."
        return self.name

# If you need the lines of source split up, it can be easier to use getsourcelines() instead of getsource().
# The return value from getsourcelines() is a tuple containing a list of strings (the lines from the source file),
# and a starting line number in the file where the source appears.

import inspect
import pprint
import example

pprint.pprint(inspect.getsourcelines(example.A.get_name))
"""
$ python inspect_getsourcelines_method.py

(['    def get_name(self):\n',
  '        "Returns the name of the instance."\n',
  '        return self.name\n'],
 48)
"""

# If the source file is not available, getsource() and getsourcelines() raise an IOError.

# Method and Function Arguments

# In addition to the documentation for a function or method, it is possible to ask for a complete specification of
# the arguments the callable takes, including default values. The getargspec() function returns a tuple containing
# the list of positional argument names, the name of any variable positional arguments (e.g., *args),
# the names of any variable named arguments (e.g., **kwds), and default values for the arguments.
# If there are default values, they match up with the end of the positional argument list.

import inspect
import example

arg_spec = inspect.getargspec(example.module_level_function)
print 'NAMES   :', arg_spec[0]
print '*       :', arg_spec[1]
print '**      :', arg_spec[2]
print 'defaults:', arg_spec[3]

args_with_defaults = arg_spec[0][-len(arg_spec[3]):]
print 'args & defaults:', zip(args_with_defaults, arg_spec[3])

# Note that the first argument, arg1, does not have a default value. The single default therefore is matched up with arg2.
"""
$ python inspect_getargspec_function.py

NAMES   : ['arg1', 'arg2']
*       : args
**      : kwargs
defaults: ('default',)
args & defaults: [('arg2', 'default')]
"""

# Class Hierarchies

# inspect includes two methods for working directly with class hierarchies.
# The first, getclasstree(), creates a tree-like data structure using nested lists and tuples
# based on the classes it is given and their base classes. Each element in the list returned is either
# a tuple with a class and its base classes, or another list containing tuples for subclasses.

import inspect
import example

class C(example.B):
    pass

class D(C, example.A):
    pass

def print_class_tree(tree, indent=-1):
    if isinstance(tree, list):
        for node in tree:
            print_class_tree(node, indent+1)
    else:
        print '  ' * indent, tree[0].__name__
    return

if __name__ == '__main__':
    print 'A, B, C, D:'
    print_class_tree(inspect.getclasstree([example.A, example.B, C, D]))

# The output from this example is the “tree” of inheritance for the A, B, C, and D classes. Note that D appears twice,
# since it inherits from both C and A.

"""
$ python inspect_getclasstree.py

A, B, C, D:
 object
   A
     D
     B
       C
         D
"""

# If we call getclasstree() with unique=True, the output is different.

import inspect
import example
from inspect_getclasstree import *

print_class_tree(inspect.getclasstree([example.A, example.B, C, D],
                                      unique=True,
                                      ))
# This time, D only appears in the output once:
"""
$ python inspect_getclasstree_unique.py

 object
   A
     B
       C
         D
"""
# Method Resolution Order

# The other function for working with class hierarchies is getmro(), which returns a tuple of classes
# in the order they should be scanned when resolving an attribute that might be inherited from a base class.
# Each class in the sequence appears only once.

import inspect
import example

class C(object):
    pass

class C_First(C, example.B):
    pass

class B_First(example.B, C):
    pass

print 'B_First:'
for c in inspect.getmro(B_First):
    print '\t', c.__name__
print
print 'C_First:'
for c in inspect.getmro(C_First):
    print '\t', c.__name__

# This output demonstrates the “depth-first” nature of the MRO search. For B_First, A also comes before C
# in the search order, because B is derived from A.

"""
$ python inspect_getmro.py

B_First:
        B_First
        B
        A
        C
        object

C_First:
        C_First
        C
        B
        A
        object
"""
# The Stack and Frames

# In addition to introspection of code objects, inspect includes functions for inspecting the runtime environment
# while a program is running. Most of these functions work with the call stack, and operate on “call frames”.
# Each frame record in the stack is a 6 element tuple containing the frame object, the filename where the code exists,
# the line number in that file for the current line being run, the function name being called, a list of
# lines of context from the source file, and the index into that list of the current line. Typically
# such information is used to build tracebacks when exceptions are raised. It can also be useful when debugging programs,
# since the stack frames can be interrogated to discover the argument values passed into the functions.

# currentframe() returns the frame at the top of the stack (for the current function).
# getargvalues() returns a tuple with argument names, the names of the variable arguments,
# and a dictionary with local values from the frame. By combining them, we can see the arguments
# to functions and local variables at different points in the call stack.

import inspect

def recurse(limit):
    local_variable = '.' * limit
    print limit, inspect.getargvalues(inspect.currentframe())
    if limit <= 0:
        return
    recurse(limit - 1)
    return

if __name__ == '__main__':
    recurse(3)

# The value for local_variable is included in the frame’s local variables even though it is not an argument to the function.
"""
$ python inspect_getargvalues.py

3 ArgInfo(args=['limit'], varargs=None, keywords=None, locals={'local_variable': '...', 'limit': 3})
2 ArgInfo(args=['limit'], varargs=None, keywords=None, locals={'local_variable': '..', 'limit': 2})
1 ArgInfo(args=['limit'], varargs=None, keywords=None, locals={'local_variable': '.', 'limit': 1})
0 ArgInfo(args=['limit'], varargs=None, keywords=None, locals={'local_variable': '', 'limit': 0})
"""
# Using stack(), it is also possible to access all of the stack frames from the current frame to the first caller.
# This example is similar to the one above, except it waits until reaching the end of the recursion to print
# the stack information.

import inspect

def recurse(limit):
    local_variable = '.' * limit
    if limit <= 0:
        for frame, filename, line_num, func, source_code, source_index in inspect.stack():
            print '%s[%d]\n  -> %s' % (filename, line_num, source_code[source_index].strip())
            print inspect.getargvalues(frame)
            print
        return
    recurse(limit - 1)
    return

if __name__ == '__main__':
    recurse(3)

# The last part of the output represents the main program, outside of the recurse function.
"""
$ python inspect_stack.py
inspect_stack.py[37]
  -> for frame, filename, line_num, func, source_code, source_index in inspect.stack():
(['limit'], None, None, {'local_variable': '', 'line_num': 37, 'frame': <frame object at 0x61ba30>,
'filename': 'inspect_stack.py', 'limit': 0, 'func': 'recurse', 'source_index': 0,
'source_code': ['        for frame, filename, line_num, func, source_code, source_index in inspect.stack():\n']})

inspect_stack.py[42]
  -> recurse(limit - 1)
(['limit'], None, None, {'local_variable': '.', 'limit': 1})

inspect_stack.py[42]
  -> recurse(limit - 1)
(['limit'], None, None, {'local_variable': '..', 'limit': 2})

inspect_stack.py[42]
  -> recurse(limit - 1)
(['limit'], None, None, {'local_variable': '...', 'limit': 3})

inspect_stack.py[46]
  -> recurse(3)
([], None, None, {'__builtins__': <module '__builtin__' (built-in)>,
'__file__': 'inspect_stack.py',
'inspect': <module 'inspect' from '/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/inspect.pyc'>,
'recurse': <function recurse at 0xc81b0>, '__name__': '__main__',
'__doc__': 'Inspecting the call stack.\n\n'})
"""

# There are other functions for building lists of frames in different contexts, such as when an exception
# is being processed. See the documentation for trace(), getouterframes(), and getinnerframes() for more details.
