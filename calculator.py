num1=eval(input("Enter the first number : "))      # 'eval' means both data types used (flaot and int )values.
num2=eval(input("Enter the  second number : "))
opr=input("Enter the operator : ")
if opr=="+" :
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="/":
    print(num1/num2)
elif opr=="*":
    print(num1*num2)
else:
    print("Only use (+,-,*,/) operators ")                