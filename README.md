
# Introduction to Python

## Variables
Variables are used to store data in Python. You can assign a value to a variable using the assignment operator (`=`). Python is a dynamically typed language, which means you don't need to explicitly declare the variable's type.

```python
# Example:
name = "John"
age = 25`
```
## User Input
You can prompt the user for input using the input() function. The entered value is stored as a string by default, so you might need to convert it to the appropriate data type.
```Python
# Example:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```
## Data Types
Python has several built-in data types:

- Numeric types (int, float)
- Strings (str)
- Booleans (bool)

## Arithmetic Operations
Python supports basic arithmetic operations like addition (+), subtraction (-), multiplication (*), division (/), and Modulo (%).
```python
# Arithmetic Operations
a = 24
b = 16

print(a + b)
print(a - b)
print(a / b)
print(a < b)

FloatNum= 1.35
IntNum= 4

print(FloatNum + IntNum)
print(type(FloatNum + IntNum))

one_third= 1 / 3

print(one_third)
print(one_third * 3) # rounds up
print(type(one_third * 3)) # still will come as a float even if it rounds up
print(one_third + 3) # rounds up
```
## Comparison Operators
You can compare values using comparison operators such as <, >, <=, >=, == (equality), and != (not equal). These operators return a boolean value (True or False).
## Strings
Strings are used to represent text in Python. You can use single quotes (') or double quotes (") to define a string.
```python
# Example:
message = "Hello, world!"
single_quotes = 'look'
double_quotes = "look"
#No difference

#select a specific character
hi = "Hello World"


# H   E   L  L  O     W  O  R  L   D
# 0   1   2  3  4  5  6  7  8  9  10
#-11 -10 -9 -8 -7 -6 -5 -4 -3  -2 -1


print(hi[0:5]) 
#all characters from 0 to 5, dont have to type 0 if starting from the start

print(hi[-5:])
# this will give you the fifth last character
```
## String Methods
Strings have built-in methods for various operations. Here are a few examples:

- `len()`: Returns the length of a string.
- `strip()`: Removes leading and trailing whitespace.
- `upper()`: Converts the string to uppercase.
- `lower()`: Converts the string to lowercase.
- `replace()`: Replaces a substring with another substring.
- `count()`: Returns the number of occurrences of a substring within the string.

```Python
#Example
hi = "Hello"
print(len(hi)) # lenght of character

# strip()
white_space = " lots of white space           "
print(len(white_space)) # 31 characters
print(len(white_space.strip())) # will remove white space at the end of a strip, 19 characters

# .lower()
example_text = " Hello text"
print( example_text.lower())

# .upper()
print(example_text.upper())

# .count
print(example_text.count("text")) 

#.replace
print(example_text.replace("text", "there")) # replaces characters in the string
```
## String Concatenation and Casting
You can concatenate strings using the + operator. If you want to concatenate a string with a non-string value, you need to convert the non-string value to a string using the str() function.

```Python
# concatenation and casting

x = 2
y = 5.4
z = "this is a string"
zz = " this is also a string"

# Concatenation, adding two string together
print(z +" "+ zz)


# casting
print(str(x) + " " + str(y) + z)

# string to numeric casting
int_string = "6"

print(int(int_string))


print(float(int_string))
```
## F-Strings and Percentages
F-strings provide a convenient way to embed expressions inside string literals. You can use curly braces {} inside an f-string to include variables or expressions.
```Python
# F - Strings

name = "Dog"
years = 7
height = 70.5

print(f"{name.upper()} is {years * 7} yeras old in dog yeras") # do stuff to your variables when in a string

pi = 3.14159265359

print(f" pi to 3 decimal place: { pi:.5f}") #shows up to a specific decimal place

# percentages
score = 16
max_score = 26

print(f" You scored {score/max_score}")
print(f" You scored {score/max_score:%}")
print(f" You scored {score/max_score:.0%}")
```
## Booleans
Booleans are a data type in Python that represent either True or False. They are often used in conditional statements and logical operations.
```Python
hi = " Hello world"

# booleans methods

print(hi.isalpha()) # false (in the content alphabetical characters only and it has a space so false)
print(hi.islower()) # false
print(hi.endswith("d")) # true
print(hi.startswith("w")) # false
```
Value of Zero: In Python, the integer value 0 is considered as False when evaluated as a boolean.
```Python
x = 0
y = 10

print(bool(x)) #False, 0 is always false, every other number is true including minus and int/floats
print(bool(y)) #True
```
Value of None: None is a special object in Python that represents the absence of a value or a null value. It is commonly used to indicate the absence of a meaningful value.

```Python
# Value of None
#Not 0, not nothing-----> it is a PLACEHOLDER

x = None # Capital N

print(bool(None)) # False
print(x == False) #Flase
print(x == True) # False

# None is neither true or false is it simply none

# these are not best practice when trying to figure of the type
print(type(x))
print(x == None)

# best practice for checking if somehting is None

print(x is None)
# mathematically x cannot equal to zero, this way you not bringing in any booleans so true or false are not into play.
```