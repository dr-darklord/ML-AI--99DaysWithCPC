'''
Unpaking a tuples....

step 1 :Create a tuples
step 2 :Assign variable for all tuple elements/value
step 3 : print
'''
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)


'''Using Asterisk*
If the number of variables is less than the number of values,
you can add an " * " to the variable name and the values will be assigned to the variable as a list:

Example
Assign the rest of the values as a list called "red":
'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


'''If the asterisk is added to another variable name than the last, 
Python will assign values to the variable until the number of values left matches the number of variables left.

Example
Add a list of values the "tropic" variable:
'''
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)