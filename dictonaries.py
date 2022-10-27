# understanding dictonary in py
from ast import Dict



dictonary = {'a':'A','b':'B','c':'C',1:'x'}
print(dictonary)
#access by index
print(dictonary['b'])
print(dictonary['c'])
print(dictonary['a'])
print(dictonary[1])

#duplicatws not allowed 
dict = {1:10,2:20,3:30,1:40}
print(dict)
print(dict[1])

#dictonary length
dict = {1:-1,2:-2,3:-3}
print("Length of dict :",len(dict))

#different types of data in dictonary
mixed_dict = {"brand":"ford",
              "flag":False,
              'switch':'on',
              'float':3.298,
              "int":2,
              "sletters":['a','b','c','....','z'],
              "cletters":['A','B','C','D','..........','Z']}

print(mixed_dict)
print("Capital letters are: ",mixed_dict['cletters'])

# printng the dictonary type
print(type(mixed_dict))

# Accessing dictonary items
#m1
x = mixed_dict['int']
print(x)
#m2 using get() func. ( SYNATX: dict.get("key value)  )
x = mixed_dict.get('flag')
print(x)


#get all keys using keys() func. SYNTAX: dict.keys()
all_keys = mixed_dict.keys()
print(all_keys)
#Add a new item to the original dictionary,
# and see that the keys list gets updated as well:
print("ALL KEYS BEFORE: ",all_keys)
mixed_dict['gadgets'] = ['lighter','airpods','mini speaker','flam'] #updating dictonary
print("ALl KEYS AFTER CHANGE: ",all_keys) #YES NOTICED CHANGES


#get all values using values() func (  SYNTAX: dict.values()   )
all_values = mixed_dict.values()
print("ALL VALUES OF mixed_dict",all_values)
#Add a new item to the original dictionary,
# and see that the values list gets updated as well:
#adding new member into dictonary
mixed_dict[1233] = {'fn':'malik','mn':'tawkeer','ln':'islam'}
print(all_values) #YES NOTICED CHANGES

#update values into dictonary using keys
mixed_dict['flag'] = ['TRUE']
print(mixed_dict)

#get all items of dictonary using items() method
dict = {1:"one",2:"two",3:'three',4:'four'}#declaring a dictonary
x = dict.items() #store all dict items into variable x
print(x) #print whatever is inside the x vaariable

#check if key exists in a dictonary
key = 3
#check for key in dictonary
if key in dict:
    print(f"Yes key found")
else:
    print("Not Found")

#change dictonary items 
dict = {'year':2022,'month':'oct','day':15}
print("Before chages",dict)
#update values
#m1 -using keys directly SYNTAX: dictonary_name[key] = new value
dict['year'] = 1996
dict['month'] = "may"
dict['day'] = 5
print("After changes",dict) 

#m2 -by using update() func.
 #Q. update year to 2000 using update() method
dict = {'year':2022,'month':'oct','day':15}
print("BEFORE",dict)
dict.update({'year':2000,'month':1})
print("AFTER",dict)
    #update by passing another dictonary
dict1 = {'year':1400,'month':11,'day':31}
dict.update(dict1)
print(dict)

#REMOVING ITEMS FROM DICTONARY
dict = {1:'a',2:'b',3:'c',4:'d'}
print("before deletion",dict)

#m1- pop() method
dict.pop(1)
print(dict)
#m2- popitem() removes last item of dictonary
dict.popitem()
print(dict)
#m3- using del keyword
del dict[3]
print(dict)

#DELETING THE DICTONARY
dict = {1:'malik',2:'tawkeer',3:'ul',4:'islam'}
print(dict)
del dict

#EMPITY THE DICTONARY USING clear() method
dict = {1:-1,2:-2,3:-3}
print(dict)
dict.clear() #dict items cleared
print(dict)

#LOOP THROUGH DICTONARY
dict = {1:-1,2:-2,3:-3}
print(dict)
#get all keys of dict one by one
for x in dict: #by default loop returns keys
    print(x)
#m-2 using keys() method
for x in dict.keys():
    print(x)

#get all values through loop
for x in dict:
    print(dict[x])
#m-2 using values() method
for x in dict.values():
    print(x)
    
#get all items using items() method
for item in dict.items():
    print(item)

#COPY DICTONARIES
dict1 = {'kulgam':2,'dhpora':3}
print(dict1)
#copy using copy() method
dict2 = dict1.copy()
print(dict2)
#using dict() method
'''dict3 = dict(dict2)
print(dict3) '''

#NESTED DICTONARIES
#crete dictonary that will contain three dictonaries
    #creating nested dictonary
myFamily = {
    "child1":{
        "name":'malik',
        'year':2014
    },
    "child2":{
        "name":"taw",
        "year":2000
    },
    "child3":{
        "name":"abc",
        'year':1926
    }
}
print(myFamily)

#create three seperate dictonaries then create new dictonary and put existing dics into them
dic1 = {1:'a',2:'b',3:'c'}
dic2 = {1:'a',2:'b',3:'c'}
dic3 = {1:'a',2:'b',3:'c'}
#createing nested dictonary
parentdict = {
    "dictonary-1":dic1,
    "dictonary-2":dic2,
    "dictonary-3":dic3
}
print(parentdict)


                #END OF DICTONARY