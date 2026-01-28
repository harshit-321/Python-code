# # #function
# # its a  block of code which only run when it is called.functions is a 
# # ,reusablitiy of the opperation 
# # it have two types of function 
# # 1.builtin fuction  
# # 2.user defined function
# # which are predefined f

# # nitory functions which are common for each and every elements ex-

# def is keyword used to decleared 

# def _name(age):
#     logic
#     return vol.....
# fname ()
# or
# print(fname())

#f.name : its name of function by the user .
#these are the parameters which are use by creating the function 
#returun is a keywords which is used to keyword is used control the flow of excution by providing final value.
#these are the function which user all while executing 
#we have 4 types of user define function 
#1} without argument without return
#2}without argument with return
#3}with argument without return
#4}with argument with return



#wap to extract all the upper case from a string.
'''
def upper_case():
    a='pyThon'
    out=''
    for i in a:
        if "A"<=i<='Z':
            out+=i
    print(out)
upper_case()

'''

'''def num (a,out=[],i=0):
    if i>=len(a):
        return out
    if type(i) in [int,float]:
        out+=[a[i]]
    return num(a,out,i+1 )
print(num([5,63,'hi']))

#a=[2,3,5,'hello',8,7,[1,2]]
#op= [4,3,5,'hello',64,7,[1,2]]

def get(a,out=[],i=0):

'''
a='11001000111001'
b='00110111000000'
#op=2

sum1=0
sum2=0
i=0
while i<len(a) or i<len(b):
    if a[i] in '1' or b[i] in '0':
        sum1+=1

