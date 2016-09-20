a ='ajay'
b =50

'''
print type(a)

print type(b)


isinstance(...)
    isinstance(object, class-or-type-or-tuple) -> bool
    
    Return whether an object is an instance of a class or of a subclass thereof.
    With a type as second argument, return whether that is the object's type.
    The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for
    isinstance(x, A) or isinstance(x, B) or ... (etc.).


'''
print isinstance(a,str)
print isinstance(b,str)
print isinstance(b,int)
'''
datatype = type(a)
print datatype

if datatype =='int':
	print 'datatype is integer'
elif datatype =='str':
	print 'datatype is string'

if type(b)==int:
	print 'datatype is integer'
elif type(b)==str:
	print 'datatype is string'

'''
