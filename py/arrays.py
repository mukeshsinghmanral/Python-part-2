from array import *
arr=array('i',[2,3,4,5,8,7])
arrnew=array(arr.typecode,[a*a*a for a in arr])
print('array: ',end=' ')
for i in arrnew:
	print(i,end=' ')
print()	
print('array element:',end='')	
for data in arr:
	print(data,end=' ')	
