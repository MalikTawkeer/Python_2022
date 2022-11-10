#even odd using lambda

number = int(input("enter a number"))

res = lambda x: number % 2 == 0

if res(number) == 1:
    print("Even")
else:
    print("odd")