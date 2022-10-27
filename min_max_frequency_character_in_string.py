
str = input("enter your string here")
mycount = []
length = len(str)
for i in range(length):
    x = str[i]
    mycount.append(str.count(x))
maxi = max(mycount)
index = mycount.index(maxi)
print(f"Maximum frequency  character is ' {str[index]} ' with frequency  : {maxi}")
mini = min(mycount)
index1 = mycount.index(mini)
print(
    f"Least frequency  character is ' {str[index1]} ' with frequency  : {mini}")
