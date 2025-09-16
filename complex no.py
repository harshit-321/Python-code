import cmath
a=int(input("enter 1 number(a!=0) : "))
b=int(input("enter 2nd number : " ))
c=int(input("enter 3rd number : "))
d=(b**2)-4*a*c
root1=(-b+cmath.sqrt(d))/2*a
root2=(-b-cmath.sqrt(d))/2*a
print("roots are : ",root1,root2)
