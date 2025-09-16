# write a programe to find sum of first 10 odd numbers using while loop 
sum=0
n=0
while n <=20 :
    if n%2!=0:
        sum+=n
    n+=1
print(sum)
#if we use for loop 
'''for i in range(1,21):
    if i % 2 != 0 :
        sum+=i
print("sum of first 10 odd number is : ",sum)'''
