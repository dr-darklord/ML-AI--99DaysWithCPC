'''To join two or more tuples you can use the " + " operator:
Example
Join two tuples: '''
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

'''If you want to multiply the content of a tuple a given number of times, you can use the * operator:
Example
Multiply the fruits tuple by 2:'''

fruits = ("apple", "banana", "cherry")
mytuple = fruits * int(input("how many time you want : "))
print(mytuple)