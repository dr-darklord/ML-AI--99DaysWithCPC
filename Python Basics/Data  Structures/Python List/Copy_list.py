# You can use the built-in List method copy() to copy a list.
# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
fruits = thislist.copy()
print(fruits)

# Another way to make a copy is to use the built-in method list().
# Example
# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
FRUITS = list(thislist)
print(FRUITS)

# You can also make a copy of a list by using the : (slice) operator.
# Example
# Make a copy of a list with the : operator:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)