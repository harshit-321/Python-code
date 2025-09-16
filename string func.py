a="Why fit in , when you are born to stand out!"


# 1. Write a program to find the length of the following string.
print("-"*10,"  length  ","-"*10)
print(len(a))
print()

# 2. Write a program to check how many time alphabet o is occuring.
print("-"*10,"  count  ","-"*10)
print(a.count("o"))
print()

# 3. Write a program to convert the whole string into lower and upper cases.
print("-"*10,"  lower case  ","-"*10)

print(a.lower())
print()
print("-"*10,"  upper case  ","-"*10)
print(a.upper())
print()

# 4. write a program to convert the following string into a title.
print("-"*10,"  title  ","-"*10)
print(a.title())
print()
# 5. write a program to find the index number of "fit in".
print("-"*10,"  find  ","-"*10)
print(a.find("fit in"))
print()
#6. index
print("-"*10," index ","-"*10)
print(a.index("o"))
print()
#7 capitalize
print("-"*10,"  capitalize  ","-"*10)
print(a.capitalize())
print()
#8 casefold  
print("-"*10,"  casefold  ","-"*10)
print(a.casefold())                     #convert into lower case
print()
#9 format
name="harshit"
age="22"
print("-"*10,"  format  ","-"*10)
b="my name is {} and my age is {}"
print(b.format(name,age))
#10 center
print("-"*10," center ","-"*10)
print(name.center(20,"*"))
print()
###################################################################
A="hello"
B="123Hello"
C="123456"
D="HELLO"
E=" "
F="Hello 123@"
G="1.234"
#######################################################################

# 11. isalnum 
print("-"*10," isalnum ","-"*10)
print(A.isalnum())
print(B.isalnum())
print(F.isalnum())
print()
  
#12. isalpha centre
print("-"*10," isalpha ","-"*10)
print(D.isalpha())
print(B.isalpha())
print(A.isalpha())
print()
#13. isdecimal
print("-"*10,"isdecimal ","-"*10)
print(C.isdecimal())
print(G.isdecimal())
print()
#14. isdigit
print("-"*10," isdigit ","-"*10)
print(C.isdigit())
print(G.isdigit())
print(F.isdigit())
print()
#15. isnumeric
print("-"*10," isnumeric ","-"*10)
print(B.isnumeric())
print(C.isnumeric())
print()
#16. islower
print("-"*10,"islower ","-"*10)
print(A.islower())
print(B.islower())
#17. isupper
print("-"*10," issuper ","-"*10)
print(A.isupper())
print(B.isupper())
print(D.isupper())
#18. isspace
print("-"*10," isspace ","-"*10)
print(D.isspace())
print(E.isspace())
print(F.isspace())
#19. istitle
print("-"*10," istitle ","-"*10)
print(F.istitle())
print(A.istitle())

###########################################################################

