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



# Garbage Collector (When we delete any name/ variable, it actually delete the reference
# of that variable pointing towards any memory address)
# In order to free up the actual space in memory Garbage collector is used
# GC checks the address to which no variable or name points and that memory address is free
# It just free up that space for other processes


# Weird Stuff
# Weird Behaviour 1
a = 2
b = a
c = b
print(sys.getrefcount(a)) # just because 2 is very common and is referenced by alot of names

# WB
a = []
b = a
c = b
print(sys.getrefcount(a))

d = []
print(sys.getrefcount(a))
d = c
print(sys.getrefcount(a))

a = [1,2,3]
print(id(1))
print(id(a[0]))

a[2]=1
print(id(a[0]))
print(id(a[2]))

