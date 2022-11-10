
# used to createe new list form existing iterable objects like arrays, tuples, lists
#SYNTAX: newList =   [expression(element) for element in oldList if condition]

# example
list1 = [1,2,4,5]
newList = [c for c in list1]

print(newList)

# even list comprehension
evenList = [i for i in range(100) if i % 2 == 0]
print(evenList)


# matrix using list comprehension
mat = [[i for i in range(3)] for j in range(4)]
print(mat)

# list comprehension strings
str = [s for s in "malik tawkeer"]
print(str)

# square of numbers from 1 to 10
num = [n**2 for n in range(1, 10+1)]
print(num)

