'''step1 : assume/create a taples
   step2 : convert the tuples in list
   step3 : then change the elements with his index number
   step4 : then convert the list to tuples again
   step5 : print the tuples
'''
tuples = ("apple","banana","kiwi","cherry")
frut = list(tuples)
frut[2] = "orange" #This method use for specially change the elements
tuples = tuple(frut)
print(tuples) 
# Another example
h = ("a","b","c","d")
i = list(h)
i[0] = "x"
h = tuple(i)
print(h)

# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# reate a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)
this = ("orange",)
thistuple = (thistuple + this)
print(thistuple)
