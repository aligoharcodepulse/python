# Everything is object in python
# In python we call name not variable
a = 4 # Call by Object Reference
print(id(a))
print(id(4))

b = a # aliasing
print(id(b))

c = b # aliasing
print(id(c))

print(a)
print(b)
print(c)

del a
print(b)
print(c)

a = 5
b = a
a = 6
print(b)

import sys
u = "erherherh"
v = u
w = v
print(sys.getrefcount(u))