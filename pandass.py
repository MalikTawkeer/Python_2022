# all about pandas
import pandas as pd

mydataset = {
    'cars':['BMW','alto','ford'],
    'price':[20,40,60]
}
myvar = pd.DataFrame(mydataset)
print(myvar)