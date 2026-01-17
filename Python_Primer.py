
# Everything in Python is an object
name = "Vijay"
age = 17
print("Name:", name)
print("Age:", age)

x = 10
y = x
print(id(x), id(y))  # same memory address

# Creating and using objects
a = 5
b = 2.5
c = "Python"
print(type(a))
print(type(b))
print(type(c))

# Built-in classes
lst = [1, 2, 3]
tpl = (1, 2, 3)
st = {1, 2, 3}
dct = {"a": 1, "b": 2}
print(lst, tpl, st, dct)

# Expressions and operator precedence
result = 10 + 5 * 2
print(result)

print(10 > 5)
print(10 == 5)
print(True and False)
print(True or False)

x = 5
y = 10
z = 15
print(x < y and y < z)

# Conditional statements
num = 10
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# For loop
for i in range(1, 6):
    print(i)

# While loop
count = 3
while count > 0:
    print("Count:", count)
    count -= 1

# Functions
def add(a, b):
    return a + b

print(add(3, 4))

# Function arguments
def greet(name, msg="Hello"):
    print(msg, name)

greet("Vijay")
greet("Vijay", "Welcome")

# Built-in functions
print(len("Python"))
print(max(3, 7, 2))
print(sum([1, 2, 3]))

# File handling
file = open("sample.txt", "w")
file.write("Learning Python File Handling")
file.close()

file = open("sample.txt", "r")
print(file.read())
file.close()

# Exception handling
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero not allowed")
    return a / b

try:
    print(divide(10, 0))
except ValueError as e:
    print("Error:", e)

# Iterators
nums = [1, 2, 3]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))

# Generators
def square_gen(n):
    for i in range(n):
        yield i * i

for val in square_gen(5):
    print(val)

# Conditional expression
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)

# List comprehension
squares = [i * i for i in range(5)]
print(squares)

# Packing and unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

# Scope example
x = 100
def demo():
    x = 50
    print("Local x:", x)

demo()
print("Global x:", x)

# Importing modules
import math
print(math.sqrt(16))
print(math.pi)
