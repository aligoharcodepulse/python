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


# Mutability
a = "Hello" # Immutable
print(id(a))
a = a + "World"
print(id(a))

t = (1,2,3) # Immutable
print(id(t))
t = t + (5,6)
print(id(t))

l = [1,2,3] # Mutable (Memory address same after updation)
print(id(l))
l.append(4)
print(id(l))
# built-in functions work by do not changing address, whereas concat or any other oprations
# change address

# Side Effects of Mutability
l = [1,2,3]
l1 = l
print(id(l))
print(id(l1))
l1.append(4)
print(l)
print(l1)

# Solution is 
l = [1,2,3]
l1 = l[:]
print(id(l))
print(id(l1))
l1.append(4)
print(l)
print(l1)

t = (1,2,3,[4,5])
t[-1][-1] = 500
print(t)

# l = [1,2,3,(4,5)]   does not work
# l[-1][-1] = 500
# print(l)

l1 = [1,2]
l2 = [3,4]
t1  = (l1,l2)
print(id(l1), id(l2), id(t1), sep=" ")
t1[0][0] = 100
print(t1)
print(id(l1), id(l2), id(t1), sep=" ")

