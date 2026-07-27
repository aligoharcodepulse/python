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







