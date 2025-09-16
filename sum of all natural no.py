num=int(input("enter a nmuber here : "))
if num<0:
    print("Please enter positive number ")
else:
    sum=0
    for i in range (1,num+1):
        sum+=i    
    print(sum)