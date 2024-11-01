'''Python Syntax
As we learned in the previous page, 
Python syntax can be executed by writing directly in the Command Line:'''

print("Hello World")

'''creating a python file on the server, using the .py file extension, and running it in the Command Line:

LIKE THIS -- "Your File Name".py'''

'''...Python Indentation...
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, 
the indentation in Python is very important.

Python uses indentation to indicate a block of code.'''

# Example
if 5 > 2:
  print("Five is greater than two!")
  
# Python will give you an error if you skip the indentation:
#Example

'''
if 5 > 2:
print("Five is greater than two!")#look properly Here i don't use indentation'''


'''The number of spaces is up to you as a programmer, 
the most common use is four, but it has to be at least one.

Example '''
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

'''You have to use the same number of spaces in the same block of code, 
otherwise Python will give you an error:

Example
Syntax Error:

if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")Look here properly'''
        

'''...Python Variables...
In Python, variables are created when you assign a value to it:

Example'''
x = 5
y = "Hello, World!"

'''...Comments...
Comments start with a " # "--its use for single line comment
Example'''

#"print is a built in function"---its a comment.
print("Hello, World!")
# If you want multiple line comment you use  (triple quotes) in your code. 