# loops
# python have two primitive loops
# for and while loops
# i = 0
# while i <= 900*(9*2):
#     print(i)
#     i=i+1
# else:
#     print()

a = 0
b = 1
x = 0
n = int(input("Enter number: "))
while x <= n:
    if n == 0:
        print(a)
        break
    elif n == 1:
        print(a," ",b)
        break
    else:
        print(a)
        print(b)
        x = a + b
        print(x)
        a = x
        b = a