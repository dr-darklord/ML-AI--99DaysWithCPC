# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# To sort descending, use the keyword argument reverse = True:
# Example
# Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = False)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

'''You can also customize your own function by using the keyword argument key = function.
The function will return a number that will be used to sort the list (the lowest number first):
Example
Sort the list based on how close the number is to 50:'''
def myfunc(n):
    return abs(n-50)
thislist = [100,50,44,77,65,82,90,23]
thislist.sort(key = myfunc)
print(thislist)

'''By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
Example
Case sensitive sorting can give an unexpected result:'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

'''Luckily we can use built-in functions as key functions when sorting a list.
So if you want a case-insensitive sort function, use str.lower as a key function:
Example
Perform a case-insensitive sort of the list:'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
# Example
# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
