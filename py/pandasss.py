from pandas import *
d = {'one' :Series([1, 2, 3], index=['a', 'b', 'c']),
'two' : Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df=DataFrame(d)
print(df)
print(df.loc['c'])