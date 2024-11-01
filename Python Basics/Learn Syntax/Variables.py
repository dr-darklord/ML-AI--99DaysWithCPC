'''Variables
Variables are containers for storing data values.

Creating Variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.'''

#Example
x = 5  #Here "x" and "y" is a variable who stote value/elements.
y = "John"
print(x)
print(y)


x = 4       
x = "Sally" 
print(x) # If you declare same "variable"name it doen't print both.Its count last one.


'''Casting
If you want to specify the data type of a variable, this can be done with casting.

Example'''
x = str(3)    # x will be 3
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0'

print(x)
print(y)
print(z)

'''Get the Type
You can get the data type of a variable with the type() function.

Example'''
x = 5
y = "John"
print(type(x))#Here "x" is a <class 'int'>
print(type(y))#Here "y" is a <class 'str'>


# String variables can be declared either by using single or double quotes:
# Example
x = "John"
print(x)
#double quotes are the same as single quotes.
x = 'John'
print(x)


'''Case-Sensitive
Variable names are case-sensitive.

Example
This will create two variables:'''

a = 4
A = "Sally"
print(a)#here "a" and "A" is not same
print(A)