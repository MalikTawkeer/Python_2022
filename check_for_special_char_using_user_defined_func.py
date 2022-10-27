# check for special characters usin user defined func

#def isSpecialChar(x):

specialCharacters = ['~','`','!','@','#','$','%','^','&','*','(',')','-','_',
                     '=','+','{','}','[',']',"\\",'|',':',';','"',"'",'<','>',"?",
                     ',','.','/']

#count number of special symbols
count = 0
for i in specialCharacters:
    count = count+1
print(count)

print(specialCharacters)

str = input("Enter A string:- ")
specCharList = "" #empty string for storing special symbols if any in inputted string
flag = False # for checking special character

for i in str: #iterating outer loop for str
    for j in specialCharacters: #iterating inner loop for secialCharacters
        if (i == j):
            specCharList = specCharList + i
            flag = True
         
if(flag):
    print(f"Yes Special character found ,it is {specCharList} ")
else:
    print(f"No Special Character Found In {str}")
    