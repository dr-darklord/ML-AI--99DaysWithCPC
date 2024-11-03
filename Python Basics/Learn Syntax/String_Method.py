"""String are immutable so,string are not be changed.

n_ame = "My name is Durjoy Bormon !!!!!!"
print(len(n_ame))

''' n_ame = "My name is Durjoy Bormon" '''
print(n_ame.upper())

''' n_ame = "My name is Durjoy Bormon" '''
print(n_ame.lower())

print(n_ame)
print(n_ame.rstrip("!"))
print(n_ame.replace("Durjoy","John"))
print(n_ame.split(" ")) #"split" convert a string in list.

blog_Heading = 'welcome tO mY channel'
print(blog_Heading.capitalize())

str1 = 'Welcome to my Heart'
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))

# a = '''MY NAME IS DURJOY BORMON !!!!!!
# my name is durjoy bormon !!!!!!
# My name is Durjoy Bormon !!!!!!
# My name is Durjoy Bormon.'''
print(a.count("is")) 
print(a.endswith("Bormon"))
print(a.endswith("."))"""

'''srr1 =("He\'s name is Sakib.He is a honest man.")
print(srr1)
print(srr1.find("Sakib"))
# print(srr1.index('OF'))
print(srr1.isalnum())
joll_y = 'WelcomeHome'
print(joll_y.isalnum())'''

'''radha = "Welcome"
print(radha.isalpha())

radha = "Welcome00"
print(radha.isalpha())'''

radha = "Welcome"
print(radha.islower())

rak_ib = "he is very nice guy."
print(rak_ib.isprintable())

rak_ib = "he is very nice guy.\n"
print(rak_ib.isprintable())

s = "      "
print(s.isspace())

titl_e = 'He Kiss His Friend Girlfriend'
print(titl_e.istitle())