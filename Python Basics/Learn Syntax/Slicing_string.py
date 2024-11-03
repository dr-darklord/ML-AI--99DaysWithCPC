# string slicing for use "[]"
fruit = "Orange"
print(len(fruit))
print("Orange is a ",len(fruit),"charecter")

Name = "Sakib,Durjoy"
print(Name[0:12]) #here it print only sakib

Name = "Sakib,Durjoy"
print(Name[0:5] + " " + Name[6:]) #here "," not printed
print(Name[0:-7])
print(Name[-6:])

n_ame = "Mahamudul,Joy"
print(n_ame[0:9])
print(n_ame[0:9]+" "+n_ame[10:])
print(n_ame[0:-4])
print(n_ame[10:])

n_ame = "Mahamudul,Joy"
print(n_ame[4:-8])

nm = "Harry"
print(nm[-4:-2])