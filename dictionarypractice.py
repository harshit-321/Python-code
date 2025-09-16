dict={"name" : "john",
      "age":23,
      "gender":"male"}

print(dict["age"]) 

# iteration of dict.......

# fuction

 #1.  get
print(dict.get("gender"))
 #2.  keys
print(dict.keys())
 #3.  values
print(dict.values())


 #4.  copy 
d=dict.copy()
print(d)
'''#5.  item 
print(dict.item())
 #6.  setdefault 
print(dict.setdefault("age",21))
 #7.  update 
print(dict.update(  ))
 #8.  pop 
print(dict.pop())
 #9.  popitem
print(dict.popitem())
 #10. clear
print(dict.clear())

'''

#sort the values of dictionary
dict1={"a":13,"b":34,"c":23,"d":11}
'''dict1=sorted(dict1.values())          #sorted functions
print(dict1)
'''
#write a python script to sort a dictionary.
#where the keys are numbers between 1 and 15
#and the values are square of keys.

a={}
for i in range (1,16):
    a[i]=i**2
print(a)

#write a programe to multiple all the item in a dictionary.
print(dict1["c"])
product=1
for i in dict1:
    product *=dict1[i]
print(product)
  
# write a python programe to sort a dictionary by key.
dict1={"d":11,"b":34,"e":3,"a":13,"c":23}
dict1=sorted(dict1.keys())          #sorted functions
print(dict1)

 
 