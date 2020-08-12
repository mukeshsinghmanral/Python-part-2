from numpy import *
a1=array([23,4,5,5,63,2,3])
a2=array([4,5,6,3,2,8,6])
print(sum(a1))
print(sum(a2))
a=a1+a2
print(a)
a1=a2
print(a1)
print(a2)
print(id(a1))
print(id(a2))
a1[1]=43
print(a1)
print(a2)
a1=a2.view()
print(id(a1))
print(id(a2))
a2[3]=3432
print(a1)
print(a2)
a2=a1.copy()
print(id(a1))
print(id(a2))
a2[5]=4343
print(a1)
print(a2)
print(concatenate((a1,a2)))
print(a1)
print(a2)
b=array([2,3,4,5,6,7,'a'])
print(b)


