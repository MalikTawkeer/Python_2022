# check for substring in string
str = input("Enter a string: ")
substring = input("Enter substring: ")

if substring in str:
    print("YES, substring found")
else:
    print("NO, substring not found")