# (Ref. http://eli.thegreenplace.net/2009/11/28/python-internals-working-with-python-asts/)
# (Not exactly "runnable" code, more of a Reference, if you will.)
# Manually building ASTs

import ast

node = ast.Expression(ast.BinOp(
                ast.Str('xy'),
                ast.Mult(),
                ast.Num(3)))

fixed = ast.fix_missing_locations(node)

codeobj = compile(fixed, '<string>', 'eval')
print eval(codeobj)

# Breaking compilation into pieces
# Given some source code, we first parse it into an AST, and then compile this AST into a code object that can be evaluated:

import ast

source = '6 + 8'
node = ast.parse(source, mode='eval')

print eval(compile(node, '<string>', mode='eval'))

# Simple visiting and transformation of ASTs

import ast

class MyVisitor(ast.NodeVisitor):
    def visit_Str(self, node):
        print 'Found string "%s"' % node.s


class MyTransformer(ast.NodeTransformer):
    def visit_Str(self, node):
        return ast.Str('str: ' + node.s)


node = ast.parse('''
favs = ['berry', 'apple']
name = 'peter'

for item in favs:
    print '%s likes %s' % (name, item)
''')

MyTransformer().visit(node)
MyVisitor().visit(node)

# This prints:

Found string "str: berry"
Found string "str: apple"
Found string "str: peter"
Found string "str: %s likes %s"

# The visitor class implements methods that are called for relevant AST nodes
# (for example visit_Str is called for Str nodes).
# The transformer is a bit more complex.
# It calls relevant methods for AST nodes and then replaces them with the returned value of the methods.
# To prove that the transformed code is perfectly valid, we can just compile and execute it:

node = ast.fix_missing_locations(node)
exec compile(node, '<string>', 'exec')
As expected [4], this prints:

str: str: peter likes str: berry
str: str: peter likes str: apple
