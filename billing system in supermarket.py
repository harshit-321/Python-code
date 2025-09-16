while True :
    name=input('enter your name : ')
    total=0
    while True : 
        print("enter the amount and quantity here ")
        amount=float(input("enter the amount of item : "))
        quantity=float(input("enter the quantity of item : "))
        total += amount*quantity
        repeat= input('do you want to add more items ?  (yes\no) : ')
        if repeat =="no" or repeat=="No" or repeat=="NO":
            break
    print("-"*40)
    print("Name : ",name)
    print("Amount to be paid : ",total)
    print("-"*40)
    print("**************** HAPPY SHOPPING *****************")
    repeat1=input('do you want to go the next customer?  (yes\no) : ')
    if repeat1 =="no" or repeat1=="No" or repeat1=="NO":
        break
    
