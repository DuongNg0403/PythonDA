import numpy as np
import pandas as pd


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002, 2003],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

df = pd.DataFrame(data)
print(df)
print(df.head())

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],index=['one', 'two', 'three', 'four','five', 'six'])
print(frame2)

print(frame2.columns)

print(frame2['state'])
print(frame2.year)
frame2.debt = np.arange(6)
print(frame2.T)