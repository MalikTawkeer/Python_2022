# IMPORTING MODULES FROM PACKAGES

import mypackage.module1
print(mypackage.module1.mod1())


import mypackage.module2
print(mypackage.module2.mod1())

# import specific function from module in pakages
from mypackage.module2 import mod1
from mypackage.module1 import lstt
print(mod1(), lstt)