#adding column 
from pandas import *
s={'one':Series([1,2,3,4],index=['a','b','c','d']),'two':Series([5,6,7,8,9],index=['a','b','c','d','e'])}
print("our DATA:")
df=DataFrame(s)
print(df)
df['third']=Series([11,22,33,44,55],index=['a','b','c','d','e'])
print('after adding new column:')
print(df)
print('adding column by adding one & third  columns:')
df['fourth']=df['third']+df['one']
print(df)
print('adding column by adding second & third  columns:')
df['sixth']=df['third']+df['two']
print(df)
print('third column:')
print(df['third'])
print('after deleting third column by "del function":')
del df['third']
print(df)
print('after deleting sixth column by "pop function":')
df.pop('sixth')
print(df)