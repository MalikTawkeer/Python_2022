#check_wheather_an_element_exists_in_an_array_or_not
mixed_list = [1,2,3,4,'a','b','c','d','@','#','!']
print("the list is:-  ",mixed_list)
key = input("Enter a key to search:- ")
if( key in mixed_list):
    print("Yes exists")
else:
    print("Not Exists")


# check using loop
list1 = [12,13,14,15]
flag = False
key = input("Enter a key ")
for i in list1:
    if(i == int(key)):
        flag = True
        break
    else:
        flag = False
if(flag):
    print("EXISTS:")
else:
    print("NOT EXISTS:")
    

#check using count() func.
list2 = [50,60,70,80,90,100]
key = input("Enter a key: ")

if list2.count(int(key)) > 0:
    print("key found.")
else:
    print("key not found!!")

    
     
