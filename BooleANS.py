# BOOLEANS


"""
 booleans with
"""

#Booleans with data types

"""
hi = " Hello world"

# booleans methods

print(hi.isalpha()) # false (is the content alphabetical characters only and it has a space so false)
print(hi.islower()) # false
print(hi.endswith("d")) # true
print(hi.startswith("w")) # false
"""

# the value of 0

"""
x = 0
y = 10

print(bool(x)) #False, 0 is always false, every other number is true including minus and int/floats
print(bool(y)) #True
"""


# Value of None
#Not 0, not nothing-----> it is a PLACEHOLDER

x = None # Capital N

print(bool(None)) # False
print(x == False) #Flase
print(x == True) # False

# None is neither true or false is it simply none

# these are not best practice
print(type(x))
print(x == None)

# best practice for checking if somehting is None

print(x is None)
# mathematically x cannot equal to zero, this way you not bringing in any booleans so not true or false
