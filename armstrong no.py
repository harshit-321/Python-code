num=int(input("Enter the first digit of your number : "))
n=len(str(num))
total= sum(int(digit)**n for digit in str(num) )
if num == total :
    print(num, "is armstrong number")
else:
    print(num,"is not armstrong number ")
    


