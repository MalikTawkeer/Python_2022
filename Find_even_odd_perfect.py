# Find even odd perfect numbers
number = int(input("Enter a number: "))

#checking for even - odd
if(number % 2 == 0): 
    print(f"{number} is EVEN ")
else:
    print(f"{number} is ODD")

#checking for perfect number
sum = 0
for i in range(1,number):# loop to get numbers from 1 to number for checking them in loop body
     if(number % i == 0):
       sum = sum + i #storeing sum of proper divisors
       
if(sum == number): #if proper divisor's sum is = number it is perfect no. else not perfect
     print(f"{number} is also perfect number")
else:
    print(f"{number} is not a perfect number")