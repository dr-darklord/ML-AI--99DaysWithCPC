'''List comprehension offers a shorter syntax when you want to create a new list based on 
the values of an existing list.
Example:
Based on a list of fruits, you want a new list, 
containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:''' 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []
for x in fruits:
    if "e" in x:
        new_list.append(x)
print(new_list)

'''With list comprehension you can do all that 
with only one line of code:    
Example'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
