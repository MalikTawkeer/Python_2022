#reversing the list
# method-1 by using [::-1]
list = ['a','b','c','d'] #list of some letters
print("list Before reversing: ",list)
reversed_list = list[::-1] #reversing list by slicing [::-1]
print("list After reversing: ")
print(reversed_list)

#method-2 by using reverse() func.

list = [100,200,'a','b','$',500]
print("Before rev: ",list)
list.reverse()
print("After rev: ",list)

