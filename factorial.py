'''
num=int(input("Enter the number : "))
fact=1
if num==0:
    print ("The factorial of ",num,"is: 1")
if num<0: 
    print ("The factorial of ",num,"is not exist")
if num>0:
    for i in range (1,num+1):
        fact=fact*i
print("The factorial of the given number is ",fact)

'''

#solution 2 using recursion
