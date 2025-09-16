# Armstromg number
'''153 = (1*1*1) + (5*5*5) + (3*3*3) 
       = 1 + 125 + 27   
       = 153         '''

num=int(input("enter the three digit number : "))
sum=0 
temp=num
while temp > 0:
       digit= temp%10
       cube=digit**3
       sum=sum+cube
       temp//=10
       
if sum ==num :
       print("it is an armstrong number ")
else :
       print("it is not amstrong number")



       