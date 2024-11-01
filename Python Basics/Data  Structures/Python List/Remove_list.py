'''The remove() method removes the specified item.
Example
Remove "banana": '''

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

'''If there are more than one item with the specified value, 
the remove() method removes the first occurrence:
Remove the first occurrence of "banana":'''

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

'''The pop() method removes the specified index.
Example
Remove the second item:'''

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

'''The del keyword also removes the specified index:
Example
Remove the first item:'''

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

'''The clear() method empties the list.
The list still remains, but it has no content.
Example
Clear the list content: '''

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

'''the del keyword can also delete the list completely.
Example
Delete the entire list: '''

thislist = ["apple", "banana", "cherry"]
del thislist #its show error because delete all.