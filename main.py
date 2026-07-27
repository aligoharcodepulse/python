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

