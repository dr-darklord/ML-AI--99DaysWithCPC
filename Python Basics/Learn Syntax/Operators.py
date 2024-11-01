'''Python Operators
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:

Example'''
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)


'''Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''
# ADDITION
x = 5
y = 3
print(x + y)

# Subtraction
x = 5
y = 3
print(x - y)

# Multiplication
x = 5
y = 3
print(x * y)

# Division
x = 12
y = 3
print(x / y)

# Modulus
x = 5
y = 2
print(x % y)

# Exponentiation
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2

# Floor division
x = 15
y = 2
print(x // y)
#the floor division // rounds the result down to the nearest whole number


# IN "Assignment Operators" mean all operators use (+=,-=,*=,/=)to assign values to variables:

'''Python Comparison Operators
Comparison operators are used to compare two values:'''
# Equal
x = 5
y = 3
print(x == y)
# returns False because 5 is not equal to 3

# NOT EQUAL
x = 5
y = 3
print(x != y)
# returns True because 5 is not equal to 3

# Greater than
x = 5
y = 3
print(x > y)
# returns True because 5 is greater than 3

# Less than
x = 5
y = 3
print(x < y)
# returns False because 5 is not less than 3

# Greater than or equal to
x = 5
y = 3
print(x >= y)
# returns True because five is greater, or equal, to 3

# Less than equal to
x = 5
y = 3
print(x <= y)
# returns False because 5 is neither less than or equal to 3

'''Python Logical Operators
Logical operators are used to combine conditional statements:'''

# AND(and) =  Returns True if both statements are true
x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

# OR(or) = Returns True if one of the statements is true
x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

# NOT(not) = Reverse the result, returns False if the result is true
x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result


