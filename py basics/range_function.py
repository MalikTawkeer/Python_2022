# returns a sequence of numbers starts from 0 (by default ), increments by 1(by default) and stops by givinh aany number
# SYNTAX: range(start, stop,increamnt )

# default

for i in range(10):
    print(i)

#changing start
for i in range(0,60):
    print(i)

# chingng default increment

for i in range(0,10,9):
    print(i)

#ELSE in for loop
for i in range(90):
    print(i)
else:
    print("end")


def fun1():
    x = 0
    def fun():
        x = 1
        print(x)
    fun()

fun1()