# main program:
import User_Func.User_Math.Math_Oper as mo
import User_Func.User_Math.Even_Odd as eo
import User_Func.User_Math.Prime as p

import User_Func.User_String.Rev_Str as sr
import User_Func.User_String.Palindrome as pl

#even odd
print(eo.evenOdd(1))

#prime
print(p.prime(31))

#operations
print(mo.multiplication(2,2))
print(mo.modules(100,100))
print(mo.addition(100, 20))
print(mo.division(1, 1))
print(mo.subtraction(3, 3))

#string reverse
print(sr.revstr("malik"))
print(pl.palindrome("madams"))