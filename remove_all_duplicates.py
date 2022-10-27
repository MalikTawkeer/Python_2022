def swapElement(list1,pos1,pos2):

    list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
    return list1
List=[1,2,34,4,5,43,5,3,5]
pos1=int(input("plese enter ist  the position"))
pos2=int(input("Plese enter 2nd position"))
print("Before Swap ",List)

print("After swap ",swapElement(List,pos1,pos2))