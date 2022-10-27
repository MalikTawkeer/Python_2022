#list overview
list = [1,2,3,"malik"]
print(list)

#accessing list using indexes
print(list[1])
print(list[:-1]) #means print from 0 to end exclude last(-1)
print(list[:3]) #print from index 0 to 3 excluded(index-3)
print(list[2:3]) #print from index 2 to 3 (included index 2 and excluded 3)

print(list)
#Creating a list with multiple distinct or duplicate elements
#list with duplicate elements
list1 = [1,2,3,3,4,4,5,5]
print(list1)

#list with distinct elements
list2 = [1,"one",2,"two",3,"three"]
print(list2)

#Accessing elements from a multi-dimensional list using indexes
muld_list = [['malik','tawkeer'],['ul','islam']]
print(muld_list[0][0]) #print malik
print(muld_list[0][1]) #print tawkeer
print(muld_list[1][0])#print ul 
print(muld_list[1][1]) #print islam

#accessing list items using for loop
for i in range(len(list1)):
    print(int(list1[i]))
    
#Getting the size of Python list
list_length = len(muld_list)
print(list_length)
print(len(list1))

#Taking Input of a Python List
listn = []
listn.append(input())
print(listn)

#M2  
string = input("Enter a string to be stored ")
lst = string.split()
print(lst)

#insert tuple into list
lst1 = [1,2,3]
print("Before adding tuple into a list: ",lst1)
tuple = (10,20)
lst1.append(tuple)
#OR lst1.append((100,200))
print("After adding tuple into a list: ",lst1)

#insert list into list
list2 = ['w','x','y','z']
print("list2 before inserting elemensts into it")
listz = [100,200,300,400]
list2.append(listz)
#OR
#list2.append(['a','b','c','d'])
print("list2 After inserting elements into it ",list2)

#inserting elements using insert(index,element) method
lst5 = [1,2,3]
print(lst5)
lst5.insert(5,10029)
print(lst5)

#inserting elements using extend(list) method
list5 = []
list5.extend([200])
print(list5)

#revering a list
list6 = ["x","y","z"]
list6.reverse()
print("list6 is reversed to ",list6)

#removing elements from the list using remove() func.
list7 = [1,2,3,4,5,6,7,8,9,10,11,12]
print("inital list: ",list7)
list7.remove(12)
list7.remove(11)
print("After removal: ",list7)

#removing sequence of numbers using iterator
print("Before removal of numbers:- ",list7)

for i in range(1, 8): #excludes 8
    list7.remove(i)
print(list7)

#remove using pop() func.
list11 = ['a','b','c','d','e']
list11.pop() #removed last elemnt of list11
print(list11)
print(list11.pop(1))#removed element at position 

#list slicing
slist = [100,200,300,400,500,600,700]
#print element from beginning to spacified range [:index]
print(slist[:4])
#print elamnt from end-use [:-index]
print(slist[:-4])
#print elemnts from specific index till end use [index:]
print(slist[5:])
#print whole list in reverse order [::-1]
print(slist[::-1])
#print elemtnts of list from rear-end use negative indexes
print(slist[:-4])
print(slist[-6:-1])


#list comprehension

odd_square = [x ** 2 for x in range(1,11) if x % 2 == 1]
print(odd_square)
#another method for above code
odd_square1 = []
for x in range (1,11):
    if(x % 2 == 1):
        odd_square1.append(x ** 2)
print(odd_square1)