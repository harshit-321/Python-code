#prime number in interval
lower=int(input("Enter a lower number : "))
upper=int(input("Enter a upper number : "))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
              break
        else:
            print(num)
            
        
    