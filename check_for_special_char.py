# chcek for special character in string
str=input("enter a string here:- ")
flag=False
special_chars=[]
for i in range(len(str)):
      value=str[i].isalnum()
      if(not value):
          flag=True
          special_chars.append(str[i])
if(flag):
    print(f"Special characters are found in a given string   {special_chars}")
else:
    print(f"No special characters are found in a given string   {str}")