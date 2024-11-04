'''
age = int(input("Enter your age : "))
print("Your age is : ",age)
if (age>=18):
    print("Yes,You can Drive")
else:
    print("NO,You can't Drive")    

conditional Operators
">", "<", ">=", "<=" "==", "!="   
age = int(input("Enter your age : "))
print("Your age is : ",age)
print(age>18)
print(age>=18)
print(age<18)
print(age<=18)
print(age==18)
print(age!=18)

apple_Price = 350
budget = float(input("You have : "))
if(apple_Price<=budget):
    print("Yes,You can buy apple 1 Kg.")
else :
    print("No,You can't buy apple.") 

num = int(input("Enter your number : "))
if(num<0):
    print("It's a Negative Number")
elif(num==0):
    print('Number is 0.')
elif(num == 9999):
    print("Yahoo,Special Number.")
else:
    print("it's Positive Number.")     '''
    
num = int(input("Enter your number : "))
if(num<0):
    print('POSITIVE number')
elif(num>0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <=20):
        print("Number is between 11-20")
    else:
        print("Number is graterthan 20")
else:
    print("Number is 0")                