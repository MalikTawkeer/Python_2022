# program to copy list onto another list
list = ["malik", "xyz", 11, 28, 'x', 'y', 'z']
print(list)
#m-1
list1 = []  # empty list
print(list1)
list1 = list #copying list into list1 
print(list1)

#OR BY USING copy() func.
lst = [1,2,3]
list1 = lst.copy()
print(list1)

#OR BY USING LOOP
lst2 = [] #declaring empty list
for i in lst: #iterating elements of lst to copy them one by one into lst2
    lst2.append(i)
print(lst2)