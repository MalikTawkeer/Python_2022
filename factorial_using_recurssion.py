# factorial usin recurssion

def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)

no = int(input("Enter a number:- "))
if no <= 0:
    print(f"factorial of {no} is 1")
else:
    print(f"factorial of {no} is ",factorial(no))