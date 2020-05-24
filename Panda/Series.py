import pandas as pd
import numpy as np

#series:
obj = pd.Series([4,7,-5,3])

print(obj)
print(obj.values)
print(obj.index)
obj2 = pd.Series([4,7,-5,3], index= ['a','b','c','d'])
print(obj2)


print(obj2[obj2>0])
np.exp(obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
print(sdata)
obj3 = pd.Series(sdata)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())

print(obj3 + obj4)#Similar to join in database
obj.index = ["Bob","Steve", "Jeff", "Ryan"]
print(obj)
