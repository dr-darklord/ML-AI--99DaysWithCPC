# You can change list item with his "index"number
thislist = ["apple", "banana", "cherry"]
thislist[1] = ("Berry") 
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ("blackcurrant","watermelon")
print(thislist)   # print(thislist[0])

# Change the second value by replacing it with two new values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second and third value by replacing it with one value
thislist = ["apple", "banana", "cherry", "orange", "kiwi"]
thislist[1:3] = ["mango"]
print(thislist)

# Insert "watermelon" as the third item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)