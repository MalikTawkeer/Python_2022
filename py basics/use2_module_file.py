# Import From Module
# we can import parts of module by using 'from' keyword

from mymodule import multiplication as mul # importing only mul
print(mul(6, 900))

import mymodule as m
print(m.multiplication(90, 2))

# importing lst part of mymodule and print it as well as renaming it...
from mymodule import lst as l
print(l)




