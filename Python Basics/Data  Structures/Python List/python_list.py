# Example of list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Lists allow "duplicate" values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Print the number of items in the list
# its mean lentgh of a list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# list use 3 data types,
# There are "String" "int" and "boolean" data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

# Examle :
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# Type casting process
# Here given "1" example
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# You also use "list()"" constructor creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])

colors = ["green","yellow","black","red","white"]
print(colors)
print(colors[-4])
print(colors[len(colors)-4])
print(colors[5-4])
print(colors[1])

if "reen" in "green" :
    print("Yes")
else:
    print("No")
    