# fabonacci series
from socket import ntohl


n1 = 0
n2 = 1
n = int(input("Enter how many terms will be in series : "))
if n <= 0:
    print("please enter a positive number")
elif n == 1:
    print("fabonacci series is ")
    print(n)
else:
    print("fabonacci series is ")
    for i in range(0, n):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
