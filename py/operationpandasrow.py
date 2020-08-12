#selection,adding,deleting rows of DataFrame
from pandas import *
s={'one':Series([1,2,3,4],index=['a','b','c','d']),'two':Series([5,6,7,8,9],index=['a','b','c','d','e'])}
df=DataFrame(s)
print('DataFrame is:')
print(df)
print('row selection:')
print(df.loc['e'])
print('row addition:')
s={'one':Series([11,22,33],index=['a','b','c']),'two':Series([88,77,66],index=['a','b','c'])}
df2=DataFrame(s)
df=df.append(df2)
print(df)
print('after deleting b row:')
print(df.drop('b'))