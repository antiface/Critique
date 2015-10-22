# (Ref. https://greentreesnakes.readthedocs.org/en/latest/tofrom.html)
# Getting to and from ASTs
# To build an ast from code stored as a string, use ast.parse().
# To turn the ast into executable code, pass it to compile() (which can also compile a string directly).

"""
>>> tree = ast.parse("print('hello world')")
>>> tree
<_ast.Module object at 0x9e3df6c>
>>> exec(compile(tree, filename="<ast>", mode="exec"))
hello world

"""
