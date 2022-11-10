
a = 1
b = 1

if a > b:
    print(f"{a} is grater than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else:
    print(F"{b} is grater than {a}")


# SHORT HAND IF
#if u have only one statement to execute , one for if and one for else then we put
#all that in one statement
# SYNTAX =  statement if condition else statement
x = 100
y = 200

print("x is big") if a > b else print("b is big")
c = 0
# use multiple if else in single line
print("A") if a > b else print("B") if a < b else print("c")

#and operator
if a > b and c > b:
    print("b is smaller then a and c")