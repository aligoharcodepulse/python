# # Print Function
# print("Hello","World",sep='-', end=' ')
# print("Ali", "Gohar")
# print(5)
# print(5-3)




# # Data Types
# # Dynamic Typing
# name = "Ali"
# fname = "Gohar"
# age = 20
# print("My name is", name , fname, ", and I'm", age, "years old.")

# # Dynamic Binding
# age = "Twenty"
# print(age)

# age = 20.0
# print(age)





# # Variables
# office = "Marketing"
# price = 20.3
# year = 2006

# list = [1,2,3,4,5]
# tuple = (1,2,3,4,5)
# sets = {(1,2,3,4,5),(6,7,8,9,10)}
# print(office, price, year, list, tuple, sets)




# # Keywords
# # python has 33 keywords (Can't be used as variable name)
# import keyword
# print(keyword.kwlist)




# # Input and type conversion
# #name = input("Enter Name: ")

# x = int(input("Enter Num 1: "))
# y = int(input("Enter Num 2: "))
# result = x + y
# print(result)



# # Literals
# # Numeric
# a = 0b1010 #binary
# b = 0o200 #octal
# c = 100 #decimal
# d = 0x100 #hexadecimal

# float_1 = 10.5
# float_2 = 1e2

# e = 5j

# print(a, b, c, d)
# print(float_1, float_2)
# print(e, e.real, e.imag)

# # String
# string = 'This is String'
# char = 'A'
# multiline_str = """hellllooooooooooooooooooooooooooooooooooooo""" 
# unicode = u"\U0001f600"
# raw_str = r"raw \n string"
# print(string, char, multiline_str, unicode, raw_str, sep='\n')

# # Boolean
# f = True + 4
# g = False + 10
# print(f, g)

# # Special
# h = None
# print(h)




# # Operators
# # Arithmetic Operators
# print(5+5)
# print(5-5)
# print(10/2)
# print(5*2)
# print(10%3)
# print(10 // 6)

# # Comparison Operators
# i = 5
# j = 3
# print(i>j, i<j, i>=j, i<=j, i==j, i!=j)

# # Logical Operators
# k = True
# l = False
# print(k and l, k or l, not l)

# # Bitwise Operators
# m = 0b1010
# n = 0b1011
# print(m & n, m | n)

# # Assignment Operators
# m = n
# print(m)

# # Identity Operators
# o = "Hello"
# p = "Hello"
# print(o is p)

# o = [1,2,3,4,5]
# p = [1,2,3,4,5]
# print(o is p)

# # Membership Operators
# q = "Ali Gohar"
# print('l' in q)





# # Conditional Statements
# email = input("Enter Email")
# password = input("Password")
# if '@' in email:
#     if email == "ali@gmail.com" and password == '1234':
#         print('Welcome')
#     elif email == "ali@gmail.com" and password != '1234':
#         print('Incorrect Password')
#         password = input("Enter password again:") 
#         if password == '1234':
#             print("Welcome")
#     else:
#         print('Invalid')
# else:
#     print("Invalid Email missing @")
    



# # While Loop
# number = int(input("Enter Number "))
# i=1
# while i<=10:
#     print(number, "*", i, "=", number*i)
#     i+=1

# # Guessing Game
# import random
# target = random.randint(1,100)
# guess = int(input("Guess kro "))
# countGuess = 1
# while(guess!=target):
#     if(guess>target):
#         print("Guess Lower ")
#     else:
#         print("Guess Higher ")
#     guess = int(input("Ek or Try kr "))
#     countGuess+=1

# print("Sahi Jawab")
# print("Total guesses:", countGuess)




# # For Loop
# for i in range(1,10,3):
#     print(i, end=" ")

# for i in [1,2,3,4]:
#     print(i, end=" ")

# for i in (6,7,8,9):
#     print(i, end=" ")

# for i in "Ali Gohar":
#     print(i, end=" ")

# print(end='\n')
# for i in range(1,5):
#     for j in range(0,i):
#         print('*', end=' ')
#     print(end='\n')




# # Break Statement
# for i in range(1,11):
#     if i == 5:
#         break
#     print(i, end=' ')

# # Continue Statement
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i, end=' ')

# # Pass
# for i in range(1,11):
#     pass




# # Buiilt-in Functions
# # 1. Input
# name = input("Enter Name: ")

# # 2. Print
# print("Your Name is", name)
# # 3. Type
# age = input("Enter Age: ")

# # 4. Int
# int(age)
# print("Your age is", age)

# # 5. Absolute (abs)
# print(abs(4))
# print(abs(-4))

# # 6. Power (pow)
# print(pow(2,10))

# # 7. Min/Max (Pass Iterable)
# print(max([100,200,300,400]))

# # 8. Round (22/7, 3)
# c = 22/7
# print(round(c,2))

# # 9. DivMod (5,2)
# print(divmod(10,3))

# # 10. bin/oct/hex
# print(bin(10))
# print(hex(10))
# print(oct(10))

# # 11. id (address)
# print(id(c))

# # 12. ord ('C') return ASCII
# print(ord('A'))

# # 13. len (iterable)
# print(len({4,5,6,7,8}))

# # 14. sum (iterable)
# print(sum({1,2,3,4,5}))

# # 15. help (pass function name for details)
# help('input')



# # Modules
# # help('modules')
# import math
# print(math.pi)
# print(math.e)
# print(math.factorial(5))
# print(math.ceil(5.4))
# print(math.floor(5.8))
# print(math.sqrt(25))
# print(math.pow(2,2))


# import random
# print(random.randint(1,100))
# list1 = [1,2,3,4]
# print(random.shuffle(list1))


# import time
# print(time.time())
# print(time.ctime())
# print("Hello")
# time.sleep(5)
# print("Ali")


# import os
# print(os.getcwd())
# print(os.listdir())




# # Strings
# # Creating a String

# a = 'Hello'
# print(a)
# a = "Ali"
# print(a)
# a = "It's raining outside"
# print(a)
# a = """Hi, How are you?"""
# print(a)


# # Concept of Indexing
# # Types of Indexing
# # Positive Indexing
# a = "Ali Gohar"
# print(a[4])

# # Negative Indexing
# print(a[-9])


# # Slicing
# print(a[0:3])
# print(a[3:])
# print(a[:6])
# print(a[:])
# print(a[0:7:2])
# print(a[-5:-1])
# print(a[-5:-1:2])
# # reverse
# print(a[::-1])


# # Editing and Deleting Strings
# # Strings are Immutable (Can not be changed)
# c = "Hello" 
# print(c)
# del c # deleted
# # print(c) c not defined


# # String Operations
# a = "hello"
# b = "world"

# #  Concatenation
# print(a + " " + b)

# # Multiply
# print(a * 3)

# # relational operators
# print("Ali" == "Gohar")
# print("Ali" != "Gohar")
# print("Ali" < "Gohar") #lexiographically (as alphabet go higher it becomes greater)
# print("Ali" > "Gohar")
# print("Ali" > "ali")

# # logical
# print("" and "world")
# print("" or "world")
# print("hello" and "world")
# print("hello" or "world")
# print(not "hello")
# print(not '')


# # loops
# c = "Hello World"
# for i in c[0:5]:
#     print(i, end='')
# print(end='\n')

# # Membership operator
# print('o' in c)




# # String Functions
# c = "hello world"
# print(len(c))
# print(max(c))
# print(min(c))
# print(sorted(c))
# print(sorted(c, reverse=True))

# print(c.capitalize())
# print(c.title())
# print(c.upper())
# print(c.lower())
# print(c.swapcase()) # Convert lower to upper and so on.

# print(c.count('o'))

# print(c.find('o')) # if not found return -1
# print(c.index('ello')) # if not found throw error

# print(c.endswith("ld"))
# print(c.startswith("el"))

# # format
# print("Hello I'm {} and I'm {} years old".format("Ali", 30))
# print("Hello I'm {1} and I'm {0} years old".format("Ali", 30))
# print("Hello I'm {name} and I'm {age} years old".format(name = "Ali", age = 30))


# # isalnum/ isalpha/ isdecimal/ isdigit/ isidentifier
# c = "Ali20"
# print(c.isalnum())
# c = "Ali20@"
# print(c.isalnum())
# print(c.isalpha())
# c = "20"
# print(c.isdecimal())
# print(c.isdigit())
# c="_hello"
# print(c.isidentifier())

# # Split
# c="hello ahmad, you are welcome"
# print(c.split())
# print(c.split("a"))
# print(c.split("x"))

# # Join
# print(" ".join(['who', 'is', 'the', 'PM', 'of', 'Pakistan?']))

# # Replace
# print(c.replace("ahmad","ali"))

# # Strip
# name = "                ali             "
# print("hi", name)
# print("Hi", name.strip())





# # Lists
# # Homogeneous
# l = [1,2,3,4,5]
# print(l)

# # Heterogeneous
# l = [1,"Hello",20.5, True]
# print(l)

# # Multi-dimensional
# # 2D
# l = [1,2,[3,4],[5,6,7]]
# print(l)
# # 3D
# l = [[[1,2],[3,4]],[5,6]]
# print(l)

# l = list("Ali Gohar")
# print(l)

# l = [1,2,3,4,5]
# print(l[0])
# print(l[2:])
# print(l[-1])
# print(l[:3])
# print(l[0:4])

# l = [1,2,[3,4],[5,6,7]]
# print(l[3][0])
# print(l[-2][0])

# l = [[[1,2],[3,4]],[5,6]]
# print(l[0][1][1])

# # Lists are Mutable
# l = [1,2,3,4,5]
# l[0] = 100
# print(l)
# l[-1] = 500
# print(l)
# l[-4:-1] = [200,300,400]
# print(l)

# # Add new element (append, extend, insert)
# l.append(600)
# l.append("hello")
# print(l)

# l.extend([1000,1100,1200])
# print(l)

# l.append([1,2])
# print(l)

# l.extend("Ali")
# print(l)

# l.insert(1,"Gohar")
# print(l)


# # Delete (del, remove, pop, clear)
# del l[-3:]
# print(l)

# l.remove("hello")
# print(l)

# l.pop()
# print(l)

# l.clear() # empty the list
# print(l)


# # List Operations
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# print(l1 + l2)
# print(l1 * 2)
# for i in l1:
#     print(i)

# l3 = [1,2,3,[4,5]]
# for i in l3:
#     print(i)

# print(4 in l3)
# print([4,5] in l3)



# # Functions on lists
# print(len(l1))
# print(max(l1))
# print(min(l1))
# print(sorted(l1, reverse=True))
# print(l1)
# l1.sort(reverse=True)
# print(l1)

# l = "how are you?"
# print(l.title())
# print(l)
# sample = []
# for i in l.split():
#     sample.append(i.capitalize())
# print(sample)
# print(" ".join(sample))

# l = "aligohar@gmail.com" 
# print(l.index('@'))
# print(l[0:8])

# print(l[:l.find('@')])

# l = [1,1,2,2,3,3,4,4]
# l1 = []
# for i in l:
#     if i not in l1:
#         l1.append(i)

# print(l1)



# Tuples (read-only)
# Create
t = ()
print(t)
t = (1,2,3,4,5)
print(t)
t = (1,"Hello", True, 20.5)
print(t)

# 2D
t = (1,2,3,(4,5))
print(t)

t = 5
print(type(t))
t = ("hello")
print(type(t))

t = ("hello",)
print(type(t))

t = tuple("Hello")
print(t)

t = tuple([1,2,3,4,5])
print(t)


# Access Items
print(t[0])
print(t[-1])

# Edit (Tuples are immutable)

# Delete (can delete whole tuple)
# del t

t1 = (6,7,8,9,10)
print(t + t1)
print(t * 2)

for i in t:
    print(i)
print(6 in t1)

# Functions
print(len(t))
print(min(t))
print(max(t))
print(sorted(t, reverse=True))

