# factorial of number using iteration

def factorial(n):
    mul = 1
    for i in range(1,n+1):
        mul = mul*i
    return mul

number = int(input("Enter a Number:- "))
print(factorial(number))