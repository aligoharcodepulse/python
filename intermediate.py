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



# Functions (Abstraction and Composition)
def is_even(number):
     """
     This function tells if a given number is even or not
     input - any vali integer
     output - even/odd
     Created By - Ali
     Last Edited - 31st July, 2026
     """
     if type(number) == int:
        if(number % 2 == 0):
            return "Even"
        else:
            return "Odd"
     else:
        return "Not Allowed"

print(is_even("Ali"))
print(is_even.__doc__)


# Default Arguments
def power(a,b):
    return a**b
print(power(2,3))
# print(power(2)) error

# Solution is default values
def power(a = 1, b = 1):
    return a**b
print(power(2,3)) # Positional Arguments
print(power(2))
print(power())

# keyword arguments (has greater priority than positional arguments)
print(power(b=2, a=3))

# Arbitrary Arguments (eg. print function)
def flexi(*number): # create tuple from number
    product = 1
    print(number)
    for i in number:
        product*=i
    print(product)

flexi(5,4,3,2,1)

# Local and Global Variable
def f(y):
    x = 1
    x += 1
    print(x)

x = 5
f(x)
print(x)



def g(y):
    print(x)
    print(x+1)

x = 5
g(x)
print(x)



def h(y):
    global x # solution to update value
    x += 1 # Not allowed to change the value of a global variable

x = 5
h(x)
print(x)


# Nested Function
def f():
    print("Inside f")
    def g():
        print("Inside g")
    g()
f()
# g() # Error (Nested function is abstracted from main program)

# Functions as Objects
def eg(num):
    return num**2
c = eg # functions are objects
print(c(3))

del f
print(c(4))

l = [1,2,3,c]
print(l[-1](2))



def f():
    def x(a,b):
        return a+b
    return x
val = f()(3,4)
print(val)



# Recursion
def multiply(a,b):
    result = 0
    for i in range(b):
        result = result + a
    print(result)

multiply(5,4)

# Now same code through recursion
def multiply(a,b):
    if b == 1:
        return a
    else:
        return a + multiply(a, b-1)

print(multiply(5,6))


# factorial
def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number-1)
print(fact(5))


# Palindrome
def palin(text):
    if len(text) <= 1:
        print("Palindrome")
    else:
        if(text[0] == text[-1]):
            palin(text[1:-1])
        else:
            print("Not a Palindrome")

palin("malayalam")
palin("hello")
palin("abba")


# Fabonacci
def fabonacci(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fabonacci(m-1) + fabonacci(m-2)
print(fabonacci(12))


# Fabonacci through dynamic programming (memorization) for time complexity
import time
def memo(m, d):
    if m in d:
        return d[m]
    else:
        d[m] = memo(m-1, d) + memo(m-2, d)
        return d[m]

start = time.time()
d = {0:1, 1:1}
print(memo(48, d))
print(time.time() - start)





