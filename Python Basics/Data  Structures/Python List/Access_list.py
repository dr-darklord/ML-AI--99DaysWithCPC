# You can access them by referring to the index number
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] #Cheak position in list 
print(thislist[2:5]) #Identify with "Index Number"

# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if Item Exists in the List
# In this case we use "if" loop and use the "in" keyword
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "orange" in thislist:
   print("Yes,orange present in this list.")
else:
    print("No,Here Orange is not presented.")