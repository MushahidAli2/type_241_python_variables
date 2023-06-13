"""variables in python

a way to store data within a program -> it becomes a refrence to that data
variable can change

How to set a variable in Python

a = 4 -> variable_name = variable_data"""

a = 1
b = 2
c = 3.5
hi = "Hello Mushahid!"

print(a + b)

# Dynamically type language - Python
# strong typed language - Java

#type() method

print(type(a))

# d = 5
# print(d)
# d = 7
# print(d)

# User input

# print("What is our name?")
# name = input("What is our name? ")
# print("hi")
# print(name)

# get user name, age, dob, address. Print it back to them

Name = input("Hello,What is your name? ")
print("hi " + Name)
Age = input("How old are you? ")
print("that's cool")
DOB = input("and when were you born? ")
print("that's pretty old :p ")
ADD = input("and lastly what is your address? ")
print("Well, Nice to meet you " + Name + " ,I know you are " + Age + " Years Old, your date of Birth is " + DOB + " and, finally you live in " + ADD)
Hobbies = input("What do you like to do in your free time? ")
print( "thats amazing! " + Name.upper())
