def palindrome(s):
    rs = s[::-1]
    if s == rs:
        print("Palindrome")
    else:
        print("Not Palindrome!")