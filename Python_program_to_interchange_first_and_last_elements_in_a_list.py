#Python program to interchange first and last elements in a list

list = [1,2,3,4,5,6]
print("Before Interchainging: ",list)
#swapping code.....
l_index = len(list) - 1 # computes last index of list
temp = list[l_index] #store value at last index into temp variable
list[l_index] = list[0] #assigns first element of list at last index
list[0] = temp #assigns temp into at index 0 of list
#swaping code ended...
print("After Interchainging: ")
print(list)