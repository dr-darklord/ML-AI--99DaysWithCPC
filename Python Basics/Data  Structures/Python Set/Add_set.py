'''Add Items
Once a set is created, you cannot change its items, but you can add new items.
To add one item to a set use the add() method.
Example
Add an item to a set, using the add() method:
'''
thisset = {"apple", "banana", "cherry"}
thisset.add("kiwi")
print(thisset)

'''Add Sets
To add items from another set into the current set, use the update() method.

Example
Add elements from tropical into thisset:
'''
thisset = {"apple", "banana", "cherry"}
topical = {"pineapple", "mango", "papaya"}
thisset.update(topical)
print(thisset)

'''Add Any Iterable
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
Example
Add elements of a list to at set:
'''
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)