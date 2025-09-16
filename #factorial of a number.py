#factorial of a number
num=int(input("Enter a Factorial : "))
fact=1
if num<0:
    print("This is not exist")
if num==0:
    print("This factorial's solution is ",1)
if num>0:
    for i in range(1,num+1):
        fact=fact*i
print("This factorial is",fact)
    