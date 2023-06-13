# Data types

# Nubers -> Float, 1.012 , ints, complex, longs
# Strings -> characters or text
# Booleans -> True or False

#Operators

# arithmetic operations

# =, -, /, *, %

# Comparison operators

# ==, !=, <, >, >=, <=

# Numeric types

"""a = 24
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
print(one_third + 3)
"""

# Strings

"""
single_quotes = 'look'
double_quotes = "look"
No difference
"""

"""
String =  "I said ' WOW' "
print(String)

Escape_exam = 'I said \'WOW!\''
print(Escape_exam)
"""


"""
hi = "Hello World"
"""

# H   E   L  L  O     W  O  R  L   D
# 0   1   2  3  4  5  6  7  8  9  10
#-11 -10 -9 -8 -7 -6 -5 -4 -3  -2 -1

"""
print(hi[0:5]) # all characters from 0 to 5, dont hav eot type 0 if starting from the start

print(hi[-5:])

"""

#String methods
# len ()

"""print(len(hi)) # lenght of character

# strip()
white_space = " lots of white space           "
print(len(white_space)) # 31 characters
print(len(white_space.strip())) # will remove white space at the end of a strip, 19 characters

# .lower()
example_text = " Hello text"
print( example_text.lower()) #makes everything lower case

# .upper()

print(example_text.upper()) # makes everything upper case

# .count
print(example_text.count("text")) # counts how many this charcater is in this order in the string can do this for space and indiviual characcetrs

#.replace
print(example_text.replace("text", "there")) # replaces characters in the string
"""

# concatenation and casting

x = 2
y = 5.4
z = "this is a string"
zz = " this is also a string"

# Concatenation, adding two string together


"""
print(z +" "+ zz)
"""

# casting
print(str(x) + " " + str(y) + z)

# string to numeric casting
int_string = "6"

print(int(int_string))
print(type(int(int_string)))

print(float(int_string))
print(type(float(int_string)))

# F - Strings

name = "Dog"
years = 7
height = 70.5

print(f"{name.upper()} is {years * 7} yeras old in dog yeras") # do stuff to your variables when in a string

pi = 3.14159265359

print(f" pi to 3 decimal place: { pi:.5f}")

# percentages

score = 16
max_score = 26

print(f" You scored {score/max_score}")
print(f" You scored {score/max_score:%}")
print(f" You scored {score/max_score:.0%}")









