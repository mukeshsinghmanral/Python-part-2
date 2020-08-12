from numpy import *
try:
	r=int(input('enter no. of rows of 1st: '))
	c=int(input('enter no. of coloumns of 1st: '))
	arr1=array([],int)
	for i in range(r):
		for j in range(c):
			arr1=append(arr1,int(input()))
		print()	
	max1=matrix(arr1.reshape(r,c))
	print(max1)
	print()
	r=int(input('enter no. of rows of 2nd: '))
	c=int(input('enter no. of coloumns of 2nd: '))	
	arr2=array([],int)
	for i in range(r):
		for j in range(c):
			arr2=append(arr2,int(input()))
		print()	
	max2=matrix(arr2.reshape(r,c))
	print(max2)
	print()
	try :
		maxx=max1*max2
		print('mutiplied matrix:')
		print(maxx)
	except Exception:
		print('cannot multiply matrix of order',max1.shape,'with matrix of order',max2.shape,'!!')	
except Exception:
	print('please enter integer type value!!')	
