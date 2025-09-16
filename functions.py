# hello world 
def hello():
    print("hello world")
hello()

#add functions
def add(a,b):
    print(a+b)

add(23,45)

#rectangle functions
def rect(length,width):
    print(length*width)
rect(45,35)

#arbitrary arguments 
def hello(*name):
    print("hello ,my name is ",name[2])

hello("harshit","shivam","lisa")    


# return statement 
'''is used to exist the functions and return the vales of  the functions.'''
    #1
def hello():
    return("hello world")

print(hello())
   
     #2
def add(a,b):
    return("The addition of two numbers is ",a+b)

print(add(2,45))

# recursion: fuctions call itself .
'''
def hello():
    print("hello")
    return hello()
print(hello())'''

#lambda functions

a= lambda  b:b*4
print(a(4))

#examples of fuctionsssssssssssssssssssssssssssssssssssssss

# write a function to find maximum of three number.
def maximum_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1,"is maximum number")
    elif num2>num3:
        print(num2,"is maximum number")
    else:
        print(num3,"is maximum number")
    
maximum_num(25,43,12)

#write a python function to create and print a list
#where the vales are square of numers between 1 and 30.

def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l

print(create_list())

#write a python function that takes a number as a 
#parameter and check if the number is prime or not.

def prime(num):
    if num==1:
        print("it is a prime number")
   # if num==2:
   #     print("it is a prime number")
    if num>2 :
        for i in range(2,num):
            if num%i==0 :
                print("it is not a prime number")
                break
        else:
            print("it is prime number")

prime(3)   



        
