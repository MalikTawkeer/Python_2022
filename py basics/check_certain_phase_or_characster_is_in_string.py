#check if a certain phase is present in string

# in
str = "malik tawkeer ul islam"
subString = input("ENTER A sub-string: ")

if(subString in str):
    print("yes")
else:
    print("NO")

#not in

s2 = "malik"

if s2 not in str:
    print("Not present!!!!")
else:
    print("YES in else")