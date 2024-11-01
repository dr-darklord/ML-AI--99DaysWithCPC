def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def multi(a,b):
    return (a*b)

def division(a,b):
    return (a/b)

a = float(input("Enter Your 1st Number : "))
b = float(input("Enter Your 2nd Number : "))

print("Addition",add(a,b))
print("Subtracsion",sub(a,b))
print("Multiplication",multi(a,b))
print("Division",division(a,b))