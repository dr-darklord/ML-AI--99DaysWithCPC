'''
Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:
'''
# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

'''You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new tuple with the specified items.
Example
Return the third, fourth, and fifth item: '''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

'''To determine if a specified item is present in a tuple use the in keyword:
Example
Check if "apple" is present in the tuple: '''
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes,'apple' is in the fruits list")
