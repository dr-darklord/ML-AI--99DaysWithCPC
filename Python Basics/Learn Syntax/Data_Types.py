'''...Built-in Data Types...
      READ CAREFULLY
      

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType'''


'''Getting the Data Type
You can get the data type of any object by using the "type():" function:

Example :
Print the data type of the variable x:'''
x = 5
print(type(x))

'''Setting the Data Type
In Python, the data type is set when you assign a value to a variable:'''
#STRING 
x = "Hello World"
#display x:
print(x)
#display the data type of x:
print(type(x)) 

#INTEGER
x = 20
#display x:
print(x)
#display the data type of x:
print(type(x)) 

#FLOAT
x = 20.5
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# COMPLEX
x = 1j
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# LIST
x = ["apple", "banana", "cherry"]
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# TUPLES
x = ("apple", "banana", "cherry")
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# RANGE
x = range(6)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# DICTIONARY
x = {"name" : "John", "age" : 36}
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# SET
x = {"apple", "banana", "cherry"}
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# FROZENSET
x = frozenset({"apple", "banana", "cherry"})
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# BOOLEAN
x = True
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# BYTES
x = b"Hello"
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# BYTESARRY
x = bytearray(5)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# MEMORY VIEW
x = memoryview(bytes(5))
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# NONE
x = None
#display x:
print(x)
#display the data type of x:
print(type(x)) 

'''Setting the Specific Data Type
If you want to specify the data type, 
EXAMPLE :
'''
x = str("Hello World")
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = int(20)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = float(20.5)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = complex(1j)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = list(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = tuple(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = range(6)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = dict(name="John", age=36)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = set(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = frozenset(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = bool(5)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = bytes(5)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = bytearray(5)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = memoryview(bytes(5))
#display x:
print(x)
#display the data type of x:
print(type(x)) 

