# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

'''To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index:
Example
Insert an item as the second position:'''

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

'''To append elements from another list to the current list, use the extend() method.
Example
Add the elements of tropical to thislist'''

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
Example
Add elements of a tuple to a list"""

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)