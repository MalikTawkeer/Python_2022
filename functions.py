# all about functions

#how to define a function
#SYNTAX: def function_name(parameter list if any): ........

#function defination
def my_function():
    print("this is my funtion")
#function call
my_function()

#function with parameters list
def function(name,address,pin):
    print("Name: ",name)
    print("Address: ",address)
    print("Pin: ",pin)
#function call
function('tawkeer','ringath','5452')


            #ARBITRARY INPUTS(if we don't know the no. of parameters use *before parameter)
def childs(*child):
    print("the younghst child is " + child[2])
#func. call
childs('malik','rayees','iniyat')

#we can also send arguments with the key = value syntax.

#define function
def childrens(c1,c2,c3):
    print(c1,c2,c3)
childrens(c1 = "x",c3="z",c2="y") #order does't matter

#if we dont know the no. of arguments passed in to func parameters use ** before parameter name
def func2(**kid):
    print("his last name is "+kid['lname'])
func2(fname='abc',lname='xyz')

        #DEFAULT PARAMETER VALUE
def func(country="norway"):
    print("I m from "+country)

func('kashmir')
func('turkey')
func() # function call without arguments so default will be used i.e norway
func('saudi aribia')
func()

            #PASSING A LIST AS AN FUNCTION ARGUMENTS
def func(fruits):
    fruits.append('abc') #changes made here will also occur in orginal list passed as an argument
    for x in fruits:
        print(x)
fruits = ['apple','orange','grapes','peair','mango']
func(fruits) #passing argument of type list
print(fruits)


            #RETURN VALUES
#to let the funtion return the value , use return keyword inside the function
def function(x):
    return 3*x
print(function(2))
print(function(3))
print(function(5))


            # PASS STATEMENT 
def  fn():
    pass    #if we have no contents for funtion definations use pass keyword to avoid errors

        #RECURSSION
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)