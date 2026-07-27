# Print Function
print("Hello","World",sep='-', end=' ')
print("Ali", "Gohar")
print(5)
print(5-3)




# Data Types
# Dynamic Typing
name = "Ali"
fname = "Gohar"
age = 20
print("My name is", name , fname, ", and I'm", age, "years old.")

# Dynamic Binding
age = "Twenty"
print(age)

age = 20.0
print(age)





# Variables
office = "Marketing"
price = 20.3
year = 2006

list = [1,2,3,4,5]
tuple = (1,2,3,4,5)
sets = {(1,2,3,4,5),(6,7,8,9,10)}
print(office, price, year, list, tuple, sets)




# Keywords
# python has 33 keywords (Can't be used as variable name)
import keyword
print(keyword.kwlist)




# Input and type conversion
#name = input("Enter Name: ")

x = int(input("Enter Num 1: "))
y = int(input("Enter Num 2: "))
result = x + y
print(result)



# Literals
# Numeric
a = 0b1010 #binary
b = 0o200 #octal
c = 100 #decimal
d = 0x100 #hexadecimal

float_1 = 10.5
float_2 = 1e2

e = 5j

print(a, b, c, d)
print(float_1, float_2)
print(e, e.real, e.imag)

# String
string = 'This is String'
char = 'A'
multiline_str = """hellllooooooooooooooooooooooooooooooooooooo""" 
unicode = u"\U0001f600"
raw_str = r"raw \n string"
print(string, char, multiline_str, unicode, raw_str, sep='\n')

# Boolean
f = True + 4
g = False + 10
print(f, g)

# Special
h = None
print(h)




# Operators
# Arithmetic Operators
print(5+5)
print(5-5)
print(10/2)
print(5*2)
print(10%3)
print(10 // 6)

# Comparison Operators
i = 5
j = 3
print(i>j, i<j, i>=j, i<=j, i==j, i!=j)

# Logical Operators
k = True
l = False
print(k and l, k or l, not l)

# Bitwise Operators
m = 0b1010
n = 0b1011
print(m & n, m | n)

# Assignment Operators
m = n
print(m)

# Identity Operators
o = "Hello"
p = "Hello"
print(o is p)

o = [1,2,3,4,5]
p = [1,2,3,4,5]
print(o is p)

# Membership Operators
q = "Ali Gohar"
print('l' in q)





# Conditional Statements
email = input("Enter Email")
password = input("Password")
if '@' in email:
    if email == "ali@gmail.com" and password == '1234':
        print('Welcome')
    elif email == "ali@gmail.com" and password != '1234':
        print('Incorrect Password')
        password = input("Enter password again:") 
        if password == '1234':
            print("Welcome")
    else:
        print('Invalid')
else:
    print("Invalid Email missing @")
    

