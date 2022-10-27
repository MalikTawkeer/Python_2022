from audioop import reverse


str = input("Enter a string:- ")
revstr = str[::-1]

if (str == revstr):
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")
    
# using reverse() func.
revstr = str.reversed()
if (str == revstr):
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")